# -*- coding: utf-8 -*-
"""Cycle30 体检（专项）：校验「待核实」渲染与数据一致 + HTML 结构健康。
A. 逐条比对：渲染出的 <li> 数量（未解决项）与 复核记录条数，是否与按同一规则从原文推出的预期一致；
B. 用 html.parser 解析全部页面，捕获结构性错误（标签未闭合等）；
C. 汇总异常清单，输出 reports/pending_render_audit_c30.json。"""
import json,os,re,glob,sys
from html.parser import HTMLParser
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
es={e["id"]:e for e in json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]}

def expect(text):
    if not text: return (0,0)
    t=text.strip()
    m=re.match(r"^(状态说明：[^。]*。)",t)
    if m: t=t[m.end():].strip()
    recs=re.findall(r"【已复核[^】]*】",t)
    open_txt=re.sub(r"【已复核[^】]*】(.*?)(?=【已复核|$)","",t,flags=re.S).strip()
    items=re.findall(r"（\d+）([^（]+)",open_txt)
    if not items:
        items=[x for x in re.split(r"[；;。]",open_txt) if len(x.strip())>4]
    return (len(items),len(recs))

class Chk(HTMLParser):
    VOID={"br","hr","img","meta","link","input","source","area","base","col","embed","track","wbr"}
    def __init__(self):
        super().__init__(); self.stack=[]; self.errors=[]
    def handle_starttag(self,tag,attrs):
        if tag not in self.VOID: self.stack.append(tag)
    def handle_endtag(self,tag):
        if tag in self.VOID: return
        if not self.stack: self.errors.append("多余闭合 </%s>"%tag); return
        if self.stack[-1]==tag: self.stack.pop()
        else:
            if tag in self.stack:
                while self.stack and self.stack[-1]!=tag:
                    self.errors.append("未闭合 <%s>"%self.stack.pop())
                if self.stack: self.stack.pop()
            else: self.errors.append("孤立闭合 </%s>"%tag)
    def close(self):
        super().close()
        for t in self.stack: self.errors.append("结尾未闭合 <%s>"%t)

viol=[]; struct=[]
for eid,e in es.items():
    p=os.path.join(ROOT,"entries",eid+".html")
    if not os.path.exists(p): continue
    h=open(p,encoding="utf-8").read()
    c=Chk(); c.feed(h); c.close()
    if c.errors: struct.append((eid,c.errors[:3]))
    # 渲染计数
    m=re.search(r"<div class='pending'>(.*?)</div>(?=<div|<section|</div>)",h,re.S)
    seg=m.group(1) if m else ""
    rendered_items=len(re.findall(r"<li>",seg.split("<details")[0])) if "<ol>" in seg else 0
    rendered_recs=int(re.search(r"复核记录（(\d+) 条",seg).group(1)) if "复核记录（" in seg else 0
    ei,er=expect(e.get("sections",{}).get("待核实",""))
    if rendered_items!=ei or rendered_recs!=er:
        viol.append({"id":eid,"rendered_items":rendered_items,"expect_items":ei,
                     "rendered_recs":rendered_recs,"expect_recs":er})
out={"pages":len(es),"render_mismatch":viol,"struct_errors":struct}
json.dump(out,open(os.path.join(ROOT,"reports","pending_render_audit_c30.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("待核实渲染比对：不一致 %d 条；HTML 结构错误页 %d 个"%(len(viol),len(struct)))
for v in viol[:8]: print("  ",v)
for s_ in struct[:5]: print("  STRUCT",s_)
sys.exit(1 if (viol or struct) else 0)
