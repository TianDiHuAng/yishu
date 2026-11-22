# -*- coding: utf-8 -*-
"""check.py — 全站质量守门员。
校验：R1必填/R2年代合法/R3生卒逻辑/R4来源合法且verified/R5重复/R6 SVG合法与不出界/
R7层级深度规则/R8数字合法/R9 id唯一/R10完整性联动/R11 coverage一致/R12 scope一致/R13站内链接。
用法: python tools/check.py  -> errors=0 时退出码0
"""
import json, os, re, sys
import xml.etree.ElementTree as ET
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")

def load(p):
    with open(p,encoding="utf-8") as f: return json.load(f)

E=[]
def err(rule,eid,msg): E.append((rule,eid,msg))

def main():
    S=load(os.path.join(D,"sources.json"))["sources"]
    sm={s["id"]:s for s in S}
    ENTRIES=load(os.path.join(D,"site_entries.json"))["entries"]
    COV=load(os.path.join(D,"coverage.json"))
    ids={e["id"] for e in ENTRIES}
    errors=[]

    # R1 必填 / R9 id唯一 / R5 重复
    required=["id","title","kind","unit","era","region","medium","tier","def","when","overview","sources"]
    seen_ids=set(); seen_titles={}
    for e in ENTRIES:
        eid=e.get("id","?")
        for k in required:
            if k not in e or e[k] in (None,"",[]): err("R1",eid,"缺必填字段 %s"%k)
        if not re.fullmatch(r"[a-z0-9-]+",eid): err("R9",eid,"id含非法字符")
        if eid in seen_ids: err("R9",eid,"重复id")
        seen_ids.add(eid)
        t=e.get("title","")
        if t in seen_titles: err("R5",eid,"标题重复(与%s)"%seen_titles[t])
        seen_titles[t]=eid
        if e.get("kind") not in ("风格","时期","人物","作品","术语"): err("R1",eid,"kind非法:%s"%e.get("kind"))
        if e.get("tier") not in ("核心","重要","补充"): err("R1",eid,"tier非法:%s"%e.get("tier"))

    # R2 年代合法 / R8 数字合法（区分公元前/公元后/万/历代）
    for e in ENTRIES:
        eid=e["id"]; w=e["when"]
        #  dynasty/时代词也是合法时间标注（如 汉代、汉—唐、唐代、先秦）
        if re.search(r"历代|不考|待考|不详|传说|至今|先秦|战国|秦|汉|唐|宋|元|明|清|商周|共和|帝国|世纪|年代",w):
            pass  # 术语或跨期条目的合法时间描述
        else:
            # 抽取所有"数[万年]"片段，判断其前后是否为公元前语境
            for m in re.finditer(r"(\d{1,5})\s*(万)?\s*年?",w):
                n=int(m.group(1)); is_wan=bool(m.group(2))
                ctx=w[max(0,m.start()-3):m.start()]
                is_bc = ("前" in ctx) or ("公元前" in w and w.find("公元前")<=m.start())
                if is_wan:
                    if n<1 or n>100: err("R2",eid,"万年数越界:%s"%m.group(0))
                elif is_bc:
                    if n<1 or n>5000: err("R2",eid,"公元前年份越界:%s"%m.group(0))
                else:
                    if n>2100: err("R2",eid,"公元年份越界:%s"%m.group(0))
            if not re.search(r"\d|不考|待|历代|不详|传说|世纪|年代|秦|汉|唐|宋|元|明|清|商周|共和|帝国|先秦|战国",w):
                err("R2",eid,"when无年代信息:%s"%w)

    # R3 人物生卒逻辑
    for e in ENTRIES:
        if e.get("kind")!="人物": continue
        m=re.search(r"(\d{4})\s*[—\-~至]\s*(\d{4})",e["when"])
        if m:
            b,d=int(m.group(1)),int(m.group(2))
            if b>=d: err("R3",e["id"],"生年>=卒年:%s"%e["when"])
            if d-b>120: err("R3",e["id"],"生卒间隔异常:%s"%e["when"])

    # R4 来源合法且verified / R10 双源联动
    for e in ENTRIES:
        eid=e["id"]
        if not isinstance(e["sources"],list) or len(e["sources"])==0:
            err("R4",eid,"无任何来源"); continue
        for s in e["sources"]:
            if s not in sm: err("R4",eid,"来源id未定义:%s"%s)
            elif not sm[s]["verified"]: err("R4",eid,"引用未核验来源:%s"%s)
        # R15 来源去重：重复id不能当作两个来源
        if len(e["sources"])!=len(set(e["sources"])):
            err("R15",eid,"sources含重复id:%s"%e["sources"])
        nver=sum(1 for s in set(e["sources"]) if s in sm and sm[s]["verified"])
        if nver<2:
            if not e.get("needs_verification") or not e.get("pending_notes"):
                err("R10",eid,"仅%d个verified来源却未标needs_verification/pending_notes"%nver)

    # R6 SVG 合法与不出界（仅对已写 svg 的条目）
    white={"svg","g","text","tspan","rect","circle","ellipse","line","polyline","polygon","path","defs","marker","title","desc"}
    svg_count=0
    for e in ENTRIES:
        if not e.get("svg"): continue
        svg_count+=1
        eid=e["id"]
        try:
            root=ET.fromstring(e["svg"])
        except Exception as ex:
            err("R6",eid,"SVG XML解析失败:%s"%str(ex)[:60]); continue
        if root.tag.split("}")[-1]!="svg": err("R6",eid,"根元素非svg")
        vb=root.attrib.get("viewBox")
        if not vb: err("R6",eid,"SVG缺viewBox")
        else:
            try:
                parts=[float(x) for x in re.split(r"[\s,]+",vb.strip())]
                if len(parts)!=4: err("R6",eid,"viewBox字段数≠4")
                else:
                    _,_,W,H=parts
                    for node in root.iter():
                        tag=node.tag.split("}")[-1]
                        if tag not in white: err("R6",eid,"非法SVG元素:%s"%tag); continue
                        if "onclick" in node.attrib or "onload" in node.attrib: err("R6",eid,"SVG含脚本")
                        # 检查矩形/圆/文本坐标是否明显越界
                        try:
                            if tag=="rect":
                                x=float(node.attrib.get("x",0)); y=float(node.attrib.get("y",0))
                                w=float(node.attrib.get("width",0)); h=float(node.attrib.get("height",0))
                                if x<-2 or y<-2 or x+w>W+2 or y+h>H+2: err("R6",eid,"rect出界")
                            if tag in ("text",):
                                x=float(node.attrib.get("x",0)); y=float(node.attrib.get("y",0))
                                if x<-2 or y<-2 or x>W+2 or y>H+2: err("R6",eid,"text出界")
                            if tag=="circle":
                                cx=float(node.attrib.get("cx",0)); cy=float(node.attrib.get("cy",0))
                                if cx<-2 or cy<-2 or cx>W+2 or cy>H+2: err("R6",eid,"circle出界")
                        except (ValueError,TypeError): pass
            except ValueError: err("R6",eid,"viewBox非数值")

    # R7 层级深度规则：L2需含完整七节；补充条目不得L3
    sec_names=["时代背景","风格特征","代表人物与作品","技法或形式分析","与前后风格的关系和争论","一图","待核实"]
    for e in ENTRIES:
        lv=e.get("level","L1"); sec=e.get("sections",{})
        covlv=COV["entries"].get(e["id"],{}).get("level","L1")
        if lv!=covlv: err("R11",e["id"],"level与coverage不一致:%s/%s"%(lv,covlv))
        if lv in ("L2","L3"):
            for sn in sec_names:
                if sn not in sec or not sec[sn]: err("R7",e["id"],"L2缺节:%s"%sn)
            if not e.get("svg"): err("R7",e["id"],"L2缺SVG一图")
        if lv=="L3" and e["tier"]!="核心": err("R7",e["id"],"非核心条目不得L3")
        if lv=="L3":
            l3=e.get("l3",{})
            cs=l3.get("controversies",[])
            if not cs: err("R16",e["id"],"L3缺争议并列表")
            for c in cs:
                vs=c.get("views",[])
                if len(vs)<2: err("R16",e["id"],"争议观点不足2方:%s"%c.get("issue",""))
                for v in vs:
                    if not v.get("holder") or not v.get("basis"): err("R16",e["id"],"争议观点缺holder/basis")
            if len(l3.get("data",[]))<2: err("R16",e["id"],"L3关键数据不足2项")
            if not l3.get("complex_diagram_note"): err("R16",e["id"],"L3缺复杂图示说明")
            # R17 争议必须真实：禁止把"编辑待办/材料缺失/本条目未提供"包装成学术分歧
            BANNED=("未给出","未提供","未列出","缺失","材料未","待补充第二来源","暂不","以免误写","信息不足","条目未")
            for c in cs:
                blob=c.get("issue","")+"".join(v.get("basis","")+v.get("holder","") for v in c.get("views",[]))
                for b in BANNED:
                    if b in blob:
                        err("R17",e["id"],"争议含编辑待办措辞[%s]，非真实学界分歧"%b); break

    # R11 coverage一致
    for eid,c in COV["entries"].items():
        if eid not in ids: err("R11",eid,"coverage有而entries无")
    if COV["meta"]["total"]!=len(ENTRIES): err("R11","meta","coverage.total与条目数不符")

    # R12 scope一致：每个unit在scope.md出现
    scope=open(os.path.join(ROOT,"scope.md"),encoding="utf-8").read()
    for e in ENTRIES:
        if e["id"] not in scope: err("R12",e["id"],"scope.md缺此条目")

    # R13 站内链接：related指向存在
    for e in ENTRIES:
        for r in e.get("related",[]):
            if r not in ids: err("R13",e["id"],"related指向不存在:%s"%r)

    # R14 数字纪律：作品条目when含年份但sources<2需待核实(已在R10覆盖)；检测正文占位英文残留
    for e in ENTRIES:
        for f in ("def","overview"):
            if re.search(r"\b(placeholder|TODO|FIXME|placeholder)\b",e.get(f,""),re.I):
                err("R14",e["id"],"正文含占位英文:%s"%f)

    print("check.py: entries=%d svg=%d errors=%d"%(len(ENTRIES),svg_count,len(E)))
    for r,eid,msg in E[:80]: print("  [%s] %s: %s"%(r,eid,msg))
    if len(E)>80: print("  ... 另有 %d 条"% (len(E)-80))
    return 0 if not E else 1

if __name__=="__main__":
    sys.exit(main())
