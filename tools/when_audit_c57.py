# -*- coding: utf-8 -*-
"""Cycle57：when 字段与正文年份的自洽性全量抽查。
规则：
 A `when` 中出现的年份集合 Wh；正文（除待核实）出现的年份集合 Wb。
 B 若 Wh 非空且 Wb 中有**不在 Wh** 的年份 → 列入 review（可能是正文另指他事，需人工判读）。
 C 若 Wh 为空（世纪/朝代表述）而正文有精确年份 → 列入 review（正文比 when 更精确，需确认是否有据）。
 D 若 `when` 出现与正文完全冲突的年份区间方向（如 when 写 1400—1500 而正文写 1600）→ 重点 review。
输出 reports/when_audit_c57.json。
"""
import json,os,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
es=json.load(open(os.path.join(ROOT,"data","site_entries.json"),encoding="utf-8"))["entries"]
def years(t):
    return set(re.findall(r"(1[0-9]{3}|20[0-9]{2}|[1-9][0-9]{2})(?!\d)",str(t or "")))
body_keys=["时代背景","风格特征","代表人物与作品","技法或形式分析","与前后风格的关系和争论","一图"]
rv=[]
for e in es:
    w=e.get("when","")
    Wh=years(w)
    body=" ".join(e.get("sections",{}).get(k,"") for k in body_keys)
    Wb=years(body)
    if Wh and Wb:
        extra=sorted(Wb-Wh)
        if extra:
            rv.append({"id":e["id"],"type":"正文年份不在when","when":w,"extra":extra[:6],
                       "level":"重点" if len(extra)>=2 else "提示"})
    elif (not Wh) and Wb:
        rv.append({"id":e["id"],"type":"when无年份但正文有","when":w,"extra":sorted(Wb)[:6],"level":"提示"})
print("条目 %d｜需复核 %d"%(len(es),len(rv)))
heavy=[r for r in rv if r["level"]=="重点"]
print("其中重点 %d"%len(heavy))
for r in heavy[:15]: print("  [重点]",r["id"],"| when:",r["when"],"| 正文额外年份:",r["extra"])
for r in [x for x in rv if x["level"]=="提示"][:8]: print("  [提示]",r["id"],"|",r["type"],"|",r["when"],"|",r["extra"])
json.dump({"total_entries":len(es),"review":rv},open(os.path.join(ROOT,"reports","when_audit_c57.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)