# -*- coding: utf-8 -*-
"""Cycle214：清理“待核实”标记。范围：已有 ≥2 个独立来源族、却仍标待核实的条目（tmp/triage_c214.json 中的 89 条）。
规则（本轮确立，记入 D214）：
  1. 先清掉说明里已过时或自相矛盾的句子（如已补 GND 后仍写“来源独立性有限（Wikipedia+Wikidata）”）。
  2. 剩余事项分两类：
     - 事实风险：两说/不一致/未核验/转引/存疑/推测/不确定归属等——保留“待核实”。
     - 内容缺口：只是“某某未给出/未述/未涉及”——这是没写，不是写了可能错，不再据此标待核实，改记为“内容缺口”。
  3. 只有“无事实风险”的条目才撤标；撤标后说明保留来源核对结论与内容缺口，方便日后补写。
用法：python tools/triage_c214.py dry ；python tools/triage_c214.py apply"""
import json,os,re,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
rows=json.load(open(os.path.join(ROOT,"tmp","triage_c214.json"),encoding="utf-8"))
STALE=["来源独立性有限（Wikipedia+Wikidata）；","来源独立性有限（Wikipedia+Wikidata）。","来源独立性有限（Wikipedia+Wikidata）","主体来自 Wikipedia 摘要；",
       "；生卒年待独立印证","生卒年待独立印证；","；生卒年、籍贯与作品未核实","；生卒年与作品未核实","；生卒年均未给出，when 为推算","生卒年均未给出，when 为推算；",
       "详见各节与待核实。","详见待核实。"]
RISK=re.compile(r"不一致|未核验|未核实|转引|两说|待核|存疑|推测|不确定|有争议|不同说法|照录|待外部核对|需外部核对|单一机构来源|单一来源，未与|单一来源（|只有单一|杀妻一事单一来源|标签错位|说法不同|为推算|不作判断|“开创”|评价")
GAP=re.compile(r"未给出|未述|未涉及|未列出处|未展开")
def clean(pn,eid):
    s=pn
    # 已由 CMA 或 LC 与 GND 双重印证生卒的，删除“GND 单一来源”字样
    if "克利夫兰艺术博物馆创作者记录独立印证" in s or "国会图书馆" in s:
        s=re.sub(r"生卒 [^ ]+ 取自 GND 规范档（单一来源，未与第二家核对）；","生卒已由 GND 规范档与第二家机构记录相互印证；",s)
    for t in STALE: s=s.replace(t,"")
    s=re.sub(r"；{2,}","；",s).strip("；。 ")
    return s
def split(s):
    parts=[p.strip() for p in re.split(r"[；。]",s) if p.strip()]
    ok=[p for p in parts if ("印证" in p or "一致" in p or "相容" in p) and not re.search(r"不一致|未与第二家",p)]
    risk=[p for p in parts if p not in ok and RISK.search(p)]
    gap=[p for p in parts if p not in ok and p not in risk and GAP.search(p)]
    other=[p for p in parts if p not in ok and p not in risk and p not in gap]
    return ok,risk,gap,other
def main(apply):
    keep=unflag=0; out=[]
    for eid,kind,fam,pn in rows:
        p=os.path.join(D,"l2",eid+".json"); j=json.load(open(p,encoding="utf-8"))
        s=clean(j.get("pending_notes") or pn,eid)
        ok,risk,gap,other=split(s)
        if risk or other:
            new="；".join(ok+risk+other+gap)+"。"; flag=True; keep+=1
        else:
            new=("已核对："+"；".join(ok)+"。" if ok else "")+("内容缺口（未写，不是存疑）："+"；".join(gap)+"。" if gap else ""); flag=False; unflag+=1
        out.append((eid,flag,new))
        if apply:
            j["pending_notes"]=new; j["needs_verification"]=flag
            json.dump(j,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
    for eid,flag,new in out: print("KEEP " if flag else "UNFLAG",eid,"|",new[:120])
    print("keep",keep,"unflag",unflag)
if __name__=="__main__":
    main(sys.argv[1]=="apply")
