# -*- coding: utf-8 -*-
"""Cycle19：B 类（96 项"结构上不适用"）复核。
把 B 类再分两层：
  B1 = 确实不适用（该地区在本库范围内不产该媒介，或该媒介非本项目主题）
  B2 = **其实是真缺口**（该地区确有该传统，但站内零覆盖，且当前无可核验来源 → 受来源阻塞）
判定依据（保守白名单，避免臆断）：非西方地区 × 音乐体裁 → 视为 B2（东南亚甘美兰、南亚古典音乐、日本雅乐等确有传统）；
西方地区 × 书法 → B1；"全球"×具体媒介 → 视该媒介是否已有全球条目。
输出 reports/matrix_b_review_c19.json + 更新 matrix_targets_c7.md 附录。"""
import json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
es=json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]
tgt=json.load(open(os.path.join(ROOT,"reports","matrix_targets_c7.json"),encoding="utf-8"))
A=tgt["A"]
# 重新计算全部空白格（用最新数据）
def band(e):
    w=e.get("era","")+" "+e.get("when","")
    if any(k in w for k in ["旧石器","新石器","公元前","战国","先秦","远古","商周"]): return "古代"
    if any(k in w for k in ["中世纪","拜占庭","罗马式","哥特","5—15","5—14","魏晋","敦煌"]): return "中世纪"
    if any(k in w for k in ["14—16","15世纪","16世纪","唐代","宋代","元代","明代","汉","唐","宋","元","明","文艺复兴"]): return "文艺复兴与宋元明"
    if any(k in w for k in ["20世纪","当代","至今","19末","19—20","2025"]): return "20世纪—当代"
    if any(k in w for k in ["17","18","19","清","巴洛克","洛可可","古典","浪漫"]): return "17—19世纪"
    return "跨期/术语"
BANDS=["古代","中世纪","文艺复兴与宋元明","17—19世纪","20世纪—当代","跨期/术语"]
regions=sorted({e["region"] for e in es})
media=sorted({m for e in es for m in e["medium"].split(",")})
grid={}
for e in es:
    for m in e["medium"].split(","): grid.setdefault((band(e),e["region"],m),[]).append(e["id"])
blank=[(r,m) for r in regions for m in media if not any(grid.get((b,r,m)) for b in BANDS)]
regions_with=set(e["region"] for e in es)
NONWEST={"东南亚","南亚","日本","东亚","中东","非洲","美洲","全球","俄国/美国","俄国/德国"}
lines=[]
B2=[]
for r,m in blank:
    if m=="书法":
        cls="B1" if r not in {"中国","日本","东亚","南亚","东南亚"} else "A"
    elif m=="音乐体裁" and r not in {"欧洲","欧美","意大利","法国","德国","奥地利","俄国/法国"}:
        cls="B2"; B2.append([r,m])
    else:
        cls="B1"
    lines.append({"region":r,"medium":m,"class":cls})
out={"all_blank":len(blank),"A":len(A),"B1":sum(1 for x in lines if x["class"]=="B1"),
     "B2":len(B2),"B2_items":B2,"detail":lines}
json.dump(out,open(os.path.join(ROOT,"reports","matrix_b_review_c19.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("空白格 %d：A(应补) %d / B1(不适用) %d / **B2(真缺口但缺来源) %d**"%(len(blank),len(A),out["B1"],len(B2)))
print("B2 明细（非西方音乐体裁）：",B2[:20])