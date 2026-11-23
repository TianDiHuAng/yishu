# -*- coding: utf-8 -*-
"""Cycle66：def/overview 与 when 的年份一致性抽查（只比短文本，噪声低）。
规则：
 A when 有年份、def+overview 出现的年份若**不在 when 年份集合**且**不是馆藏号形式**（形如 1918.328 / Q37562）→ 列出。
 B def 或 overview 为空 → 列出。
 C overview 与 def 完全相同（复制粘贴）→ 列出。
输出 reports/def_overview_c66.json。"""
import json,os,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
es=json.load(open(os.path.join(ROOT,"data","site_entries.json"),encoding="utf-8"))["entries"]
def yrs(t):
    out=set()
    for m in re.finditer(r"(1[0-9]{3}|20[0-9]{2}|[1-9][0-9]{2})(?![\d.])",str(t or "")):
        s=m.group(1)
        # 排除馆藏号/编号语境：前后有 '藏（' 或 '.' 数字串
        ctx=str(t)[max(0,m.start()-6):m.start()]
        if re.search(r"藏（|藏\(|No\.|INV|MR ",ctx): continue
        out.add(s)
    return out
A=[];B=[];C=[]
for e in es:
    w=e.get("when",""); d=e.get("def","") or ""; o=e.get("overview","") or ""
    if not d.strip() or not o.strip(): B.append(e["id"])
    if d.strip() and d.strip()==o.strip(): C.append(e["id"])
    Wh=yrs(w)
    if Wh:
        Wd=yrs(d)|yrs(o)
        extra=sorted(Wd-Wh)
        if extra: A.append({"id":e["id"],"when":w,"extra":extra[:5],"def":d[:60],"overview":o[:60]})
print("条目 %d" % len(es))
print("A 年份冲突：%d"%len(A))
for x in A[:12]: print("  ",x["id"],"| when:",x["when"],"| 额外:",x["extra"],"|",x["def"][:40])
print("B 空字段：%d %s"%(len(B),B[:6]))
print("C 复制粘贴：%d %s"%(len(C),C[:6]))
json.dump({"A":A,"B":B,"C":C},open(os.path.join(ROOT,"reports","def_overview_c66.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)