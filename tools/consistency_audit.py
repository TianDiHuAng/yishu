# -*- coding: utf-8 -*-
"""内容自洽性审计 v2（Cycle11）：收紧 A 规则，避免把"生平年代/时期年代"误判为"作品年份"。
A 规则：仅当正文出现**条目自身年代区间之外**的年份（=额外的、可能指作品的年份），
且待核实声称"未给出作品年份/创作年份"时，才判为矛盾。
收藏地：仅当正文出现馆名且待核实明确说"未给出收藏地/馆藏"时记录为提示（不判错）。
B/C/D 规则同 v1。"""
import json,os,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
es=json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]
BODY=["时代背景","风格特征","代表人物与作品","技法或形式分析","与前后风格的关系和争论"]
def years(t): return set(int(x) for x in re.findall(r"\d{3,4}",t))
out={"A_claim_vs_pending":[],"A_collection_hint":[],"B_svg_digits":[],"C_review_mark_in_body":[],"D_empty_pending":[]}
for e in es:
    sec=e.get("sections",{})
    if not sec: continue
    body="".join(sec.get(k,"") for k in BODY)
    pend=sec.get("待核实","")
    # 仅用【已复核】之前的部分判断"尚未解决"的主张，避免把复核结论本身当成待核声明
    pend_open=pend.split("【已复核】")[0]
    own=years(e.get("when",""))
    extra=[y for y in years(body) if y not in own]
    claims_work_year=re.search(r"(未给出|未提供|未列出|待补充)[^。；]{0,30}(创作)?年份",pend_open) or re.search(r"作品[^。；]{0,20}(年份|年代)",pend_open)
    if extra and claims_work_year:
        out["A_claim_vs_pending"].append([e["id"],sorted(extra)[:5],claims_work_year.group(0)[:40]])
    claims_coll=re.search(r"(未给出|未提供|未列出|待补充)[^。；]{0,30}收藏地",pend_open)
    has_coll=re.search(r"(藏于|馆藏|博物馆|美术馆|艺术中心)",body)
    if claims_coll and has_coll:
        out["A_collection_hint"].append([e["id"],has_coll.group(0)])
    fig=sec.get("一图","")
    for num in set(re.findall(r"\d{2,4}",fig)):
        if num not in body and num not in e.get("when",""): out["B_svg_digits"].append([e["id"],num])
    if "【已复核】" in body: out["C_review_mark_in_body"].append(e["id"])
    if not pend.strip(): out["D_empty_pending"].append(e["id"])
json.dump(out,open(os.path.join(ROOT,"reports","consistency_audit.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("=== 内容自洽性审计 v2 ===")
for k,v in out.items(): print(" %-22s %d %s"%(k,len(v),v[:8]))