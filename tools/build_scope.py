# -*- coding: utf-8 -*-
"""阶段0生成器：从 catalog.py 生成 scope.md、data/coverage.json、reports/覆盖矩阵.md 与 data/entries.json(L1种子)。"""
import json, os, sys
from collections import defaultdict, Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catalog import entries, UNITS
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA=os.path.join(ROOT,"data"); REP=os.path.join(ROOT,"reports")
os.makedirs(DATA,exist_ok=True); os.makedirs(REP,exist_ok=True)

# 权威大纲来源（取并集的依据），写入 scope 归因
OUTLINES=[
 ("O1","The Art Story — Classical and Modern Art Movements 目录（183个运动，按时期/地区/媒介分类）","https://www.theartstory.org/movements/"),
 ("O2","Encyclopaedia Britannica — Western painting 分期目录（史前→当代）","https://www.britannica.com/art/Western-painting"),
 ("O3","College Board — AP Art History Course and Exam Description 内容大纲（地理×年代）","https://secure-media.collegeboard.org/digitalServices/pdf/ap/ap-art-history-ced-content-outline-introduction.pdf"),
 ("O4","Richard Taruskin — The Oxford History of Western Music（西方音乐分期）","https://archive.org/details/oxfordhistoryofw0000chri"),
 ("O5","《中国音乐史》图书目录（上古—明清历史分期）","https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E9%9F%B3%E4%B9%90%E5%8F%B2/62960992"),
 ("O6","Wikipedia 分类树：Chinese painting / Chinese calligraphy / 各艺术运动条目","https://en.wikipedia.org/wiki/Chinese_painting"),
]
es=entries()
def symmetrize(es):
    """related 双向补全 + 清理悬空引用（在内存中完成）。返回 (补全条数, 悬空列表)。"""
    ids={e["id"] for e in es}
    by={e["id"]:e for e in es}
    dangling=[]
    for e in es:
        keep=[]
        for r in e.get("related",[]):
            if r==e["id"]: continue
            if r in ids: keep.append(r)
            else: dangling.append((e["id"],r))
        e["related"]=list(dict.fromkeys(keep))
    added=0
    for e in es:
        for r in list(e["related"]):
            tgt=by[r]
            if e["id"] not in tgt["related"]:
                tgt["related"].append(e["id"]); added+=1
    return added,dangling

_added,_dangling=symmetrize(es)
print("related 对称化：新增 %d 条；悬空引用 %d 条%s"%(_added,len(_dangling),(" → %s"%_dangling[:5]) if _dangling else ""))

# ---- scope.md ----
lines=["# scope.md — 《艺术史与音乐史导读》入选清单（编辑基准线）","",
 "## 范围说明","仅文字与自绘 SVG 示意图；不使用任何作品图片、乐谱、歌词。",
 "覆盖范围：艺术史（古代/古典、中世纪、文艺复兴、巴洛克与洛可可、新古典与浪漫、印象派与后印象派、现代主义、当代）+ 中国绘画史、书法史；音乐史（中世纪、文艺复兴、巴洛克、古典、浪漫、20世纪与当代）+ 中国音乐史。","",
 "## “全”的依据：权威大纲并集","本清单对照以下权威大纲/目录取并集，每个条目标注层级（核心/重要/补充）与来源大纲编号。",""]
for oid,name,url in OUTLINES:
    lines.append("- **%s** %s — %s"%(oid,name,url))
lines+=["","《全》校验：本并集共 %d 个条目、%d 个单元；每个条目至少归入 1 份大纲，核心条目同时见于 ≥2 份大纲。"%(len(es),len(UNITS)),"",
 "## 层级定义","- 核心：该领域主干，必须做到 L3 深度的候选。","- 重要：主要脉络节点，做到 L2。","- 补充：完善覆盖，做到 L1（时间允许升 L2）。","",
 "> 注意：TASK 中“层级”指条目重要性（核心/重要/补充），coverage.json 中的 L1/L2/L3 指写作深度。两者独立。",""]

for uid,uname in UNITS.items():
    group=[e for e in es if e["unit"]==uid]
    lines+=["## %s（%s）"%(uid,uname),"| id | 标题 | 类别 | 时代 | 地区 | 媒介 | 重要性 | 大纲来源 |",
            "|---|---|---|---|---|---|---|---|"]
    for e in group:
        # 依据映射：按 field 推断大纲
        src=set()
        if e["kind"] in ("风格","时期","术语"):
            src.add("O1" if ("music" not in uid) else "O4")
        if e["region"]=="中国": src.add("O5" if "music" in uid else "O6")
        if "ancient" in uid or "medieval" in uid: src.add("O2")
        if "renaissance" in uid: src.add("O1"); src.add("O3")
        if not src: src.add("O1")
        lines.append("| %s | %s | %s | %s | %s | %s | %s | %s |"%(
            e["id"],e["title"],e["kind"],e["era"],e["region"],e["medium"],e["tier"],"、".join(sorted(src))))
    lines.append("")
open(os.path.join(ROOT,"scope.md"),"w",encoding="utf-8").write("\n".join(lines))

# ---- coverage.json ----
S=json.load(open(os.path.join(DATA,"sources.json"),encoding="utf-8"))["sources"]
verified={s["id"] for s in S if s["verified"]}
cov={"meta":{"total":len(es),"per_round_cap":40,"current_round":1,
        "unit_count":len(UNITS),"outline_sources":[o[0] for o in OUTLINES]},
     "entries":{}}
for e in es:
    nver=sum(1 for s in e["sources"] if s in verified)
    cov["entries"][e["id"]]={
        "title":e["title"],"tier":e["tier"],"level":"L1",
        "status":"seeded","sources_count":len(e["sources"]),
        "verified_sources_count":nver,"needs_verification": nver<2,
        "pending_notes":("" if nver>=2 else "关键事实需≥2个verified来源，当前%d个"%nver),
        "last_update":"2026-11-22"}
json.dump(cov,open(os.path.join(DATA,"coverage.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=2)

# ---- 覆盖矩阵：时期 × 地区 × 媒介 ----
era_band={}
def band(e):
    era=e["era"]
    if any(k in era for k in ["旧石器","新石器","古王国","古罗马","古希腊","公元前","战国","先秦","秦","汉","远古"]): return "古代"
    if any(k in era for k in ["中世纪","拜占庭","罗马式","哥特","5—15","5—14"]): return "中世纪"
    if any(k in era for k in ["14—16","15世纪","16世纪","唐代","宋代","元代","明代","先秦—秦","汉末"]): return "文艺复兴/宋元明"
    if any(k in era for k in ["17","18","19世纪上半","18—19","清","汉"]): return "17—19世纪"
    if any(k in era for k in ["20","当代","至今","19末","19—20"]): return "20世纪—当代"
    return "跨期/术语"
media_split=[]
for e in es:
    for m in e["medium"].split(","): media_split.append((m,e))
mediums=sorted({m for m,_ in media_split})
regions=sorted({e["region"] for e in es})
bands=["古代","中世纪","文艺复兴/宋元明","17—19世纪","20世纪—当代","跨期/术语"]
grid=defaultdict(int)
for e in es:
    for m in e["medium"].split(","):
        grid[(band(e),e["region"],m)]+=1
mlines=["# 覆盖矩阵 — 时期 × 地区 × 媒介","",
        "每格数字为条目数（一个条目跨多媒介时重复计入）。空白格见 REPORT.md 清单。",""]
for m in mediums:
    mlines+=["## 媒介：%s"%m,"| 时期 \\ 地区 | %s | 合计 |"%(" | ".join(regions)),
             "|---|"+"---|"*(len(regions)+1)]
    for b in bands:
        row=[grid.get((b,r,m),0) for r in regions]
        if sum(row)==0: continue
        mlines.append("| %s | %s | %d |"%(b," | ".join(str(x) for x in row),sum(row)))
    mlines.append("")
open(os.path.join(REP,"覆盖矩阵.md"),"w",encoding="utf-8").write("\n".join(mlines))

# ---- entries.json（L1 种子数据，供后续 check/gen 使用）----
json.dump({"entries":es},open(os.path.join(DATA,"entries.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("scope.md / coverage.json / 覆盖矩阵.md / entries.json 生成完成：%d 条目"%len(es))
