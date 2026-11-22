# -*- coding: utf-8 -*-
"""Cycle34：单元页新增「本单元覆盖缺口」区块。
数据来自 reports/matrix_targets_c7.json（A 类）与 matrix_b_review_c19.json（B2），
按该单元涉及的地区×媒介筛选；文件缺失时静默跳过。"""
import io,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","gen_site.py"); s=io.open(P,encoding="utf-8").read()

helper = '''def load_gap_targets():
    """读取矩阵缺口清单（A 类应补 / B2 候选），缺失则返回空。"""
    import json as _j
    out={"A":[],"B2":[]}
    try:
        a=_j.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","reports","matrix_targets_c7.json"),encoding="utf-8"))
        out["A"]=[[r["region"],r["medium"]] for r in a.get("A",[])]
    except Exception: pass
    try:
        b=_j.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","reports","matrix_b_review_c19.json"),encoding="utf-8"))
        out["B2"]=[[r[0],r[1]] for r in b.get("B2_items",[])]
    except Exception: pass
    return out

'''
if "def load_gap_targets(" not in s:
    a="def build_unit_pages(entries,units,cov):"
    assert a in s
    s=s.replace(a, helper+a, 1)

old='''        s.append("</div>"+FOOT)
        open(os.path.join(OUT,"units",uid+".html"),"w",encoding="utf-8").write("".join(s))'''
new='''        # 本单元覆盖缺口（来自矩阵清单，仅提示，不代表可立即补写）
        gaps=GAPS
        regs={e["region"] for e in g}
        meds={m for e in g for m in e["medium"].split(",")}
        relA=[x for x in gaps.get("A",[]) if x[0] in regs and x[1] in meds]
        relB=[x for x in gaps.get("B2",[]) if x[0] in regs and x[1] in meds]
        if relA or relB:
            s.append("<div class='section-block'><h2><span class='num'>05</span>本单元覆盖缺口</h2>")
            s.append("<p class='eyebrow'>以下缺口来自覆盖矩阵分析；补写需先取得可核验来源，未取得前不写作。</p>")
            if relA:
                s.append("<p><strong>A 类（该地区本域已有条目、缺此媒介）：</strong>%s</p>"%esc("、".join("%s×%s"%(a,b) for a,b in relA[:8])))
            if relB:
                s.append("<p><strong>B2 类（候选缺口，需权威大纲确认）：</strong>%s</p>"%esc("、".join("%s×%s"%(a,b) for a,b in relB[:8])))
            s.append("</div>")
        s.append("</div>"+FOOT)
        os.makedirs(os.path.join(OUT,"units"),exist_ok=True)
        open(os.path.join(OUT,"units",uid+".html"),"w",encoding="utf-8").write("".join(s))'''
assert old in s, "unit page footer anchor missing"
s=s.replace(old,new)
# 在 build_unit_pages 开头定义 GAPS
old2='''    os.makedirs(os.path.join(OUT,"units"),exist_ok=True)
    dom=defaultdict(list)
    for e in entries: dom[e["unit"]].append(e)
    order={"核心":0,"重要":1,"补充":2}'''
new2='''    os.makedirs(os.path.join(OUT,"units"),exist_ok=True)
    GAPS=load_gap_targets()
    dom=defaultdict(list)
    for e in entries: dom[e["unit"]].append(e)
    order={"核心":0,"重要":1,"补充":2}'''
assert old2 in s, "unit page init anchor missing"
s=s.replace(old2,new2)
io.open(P,"w",encoding="utf-8").write(s)
print("unit pages: gap section added")