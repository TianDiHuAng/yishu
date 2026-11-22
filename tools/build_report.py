# -*- coding: utf-8 -*-
"""生成 REPORT.md：总条目、各层级数量、验证通过数、待核实数、空白格子清单、独立性限制、批次复检结论。"""
import json, os, sys
from collections import defaultdict
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from catalog import UNITS
D=os.path.join(ROOT,"data")
es=json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]
cov=json.load(open(os.path.join(D,"coverage.json"),encoding="utf-8"))["entries"]
src=json.load(open(os.path.join(D,"sources.json"),encoding="utf-8"))["sources"]

n=len(es)
lv=defaultdict(int); tier=defaultdict(int)
for e in es: lv[e.get("level","L1")]+=1; tier[e["tier"]]+=1
verified_src=sum(1 for s in src if s["verified"])
nver=sum(1 for e in es if not e.get("needs_verification"))
nneed=sum(1 for e in es if e.get("needs_verification"))
nind=sum(1 for k,v in cov.items() if v.get("source_independence_ok"))

# 空白格子：时期×地区×媒介 三维网格中为0的组合（列出域内应覆盖但为空的）
def band(e):
    era=e["era"]
    import re
    if any(k in era for k in ["旧石器","新石器","古王国","古罗马","古希腊","公元前","战国","先秦","秦","汉","远古"]): return "古代"
    if any(k in era for k in ["中世纪","拜占庭","罗马式","哥特","5—15","5—14"]): return "中世纪"
    if any(k in era for k in ["14—16","15世纪","16世纪","唐代","宋代","元代","明代"]): return "文艺复兴/宋元明"
    if any(k in era for k in ["17","18","19","清"]): return "17—19世纪"
    if any(k in era for k in ["20","当代","至今","19末"]): return "20世纪—当代"
    return "跨期/术语"
grid=defaultdict(int)
for e in es:
    for m in e["medium"].split(","): grid[(band(e),e["region"],m)]+=1
bands=["古代","中世纪","文艺复兴/宋元明","17—19世纪","20世纪—当代","跨期/术语"]
regions=sorted({e["region"] for e in es})
media=sorted({m for e in es for m in e["medium"].split(",")})
blanks=[]
# 只列出"合理应覆盖"的空白：地区×媒介，与该地区已有媒介集合做对照（简化规则）
region_media=defaultdict(set)
for e in es:
    for m in e["medium"].split(","): region_media[e["region"]].add(m)
for r in regions:
    for m in media:
        if m not in region_media[r] and m in ("绘画","音乐体裁","书法","建筑","雕塑"):
            blanks.append((r,m))

L=[]
L.append("# REPORT.md — 《艺术史与音乐史导读》覆盖报告")
L.append("")
L.append("## 规模")
L.append("- 总条目数：**%d**"%n)
L.append("- 知识单元数：**%d**"%len(UNITS))
L.append("- 来源库条目：**%d**（已核验 verified=true：**%d**）"%(len(src),verified_src))
L.append("")
L.append("## 各层级数量（写作深度）")
L.append("| 层级 | 数量 | 说明 |")
L.append("|---|---|---|")
L.append("| L1 骨架 | %d | 定义/时间或位置/概述/相关条目 |"%lv["L1"])
L.append("| L2 标准 | %d | 完整七节结构 + 自绘 SVG 一图 |"%lv["L2"])
L.append("| L3 深度 | %d | 核心条目的争议/数据/复杂图示（后续轮次） |"%lv["L3"])
L.append("")
L.append("## 重要性分布")
L.append("- 核心：%d · 重要：%d · 补充：%d"%(tier["核心"],tier["重要"],tier["补充"]))
L.append("")
L.append("## 验证与诚实标注")
L.append("- 双源规则通过（≥2 个不同 verified 来源 id）：**%d / %d**"%(nver,n))
L.append("- needs_verification=true（来源不足）：**%d**"%nneed)
L.append("- **来源独立性限制**：仅 **%d / %d** 条目具备来自不同作者且不同域名的两个来源；其余条目虽满足“两个不同来源 id”的机器规则，但多为同一机构（Wikipedia）的不同词条。按 TASK“关键事实至少两个独立来源互相印证”的严格解读，这些条目的关键事实仍应视为**待第二独立来源复核**。已在 coverage.json 以 `source_independence_ok=false` 逐条标注，避免以机器通过掩盖来源集中问题。"%(nind,n))
L.append("- L2 条目正文的“待核实”节逐条列出了具体待补事项（作品年份、收藏地、首演场馆等），写作时查不到的细节一律未写入正文。")
L.append("")
L.append("## 覆盖矩阵空白格子清单")
L.append("以下为“时期×地区×媒介”三维矩阵中，某地区完全未覆盖某媒介的格子（非错误，标出以便后续补盲）：")
if blanks:
    L.append("")
    L.append("| 地区 | 未覆盖媒介 |")
    L.append("|---|---|")
    for r,m in blanks: L.append("| %s | %s |"%(r,m))
else:
    L.append("- （无完全空白的地区×媒介组合）")
L.append("")
L.append("## 批次复检")
L.append("- 每完成 20 个条目另起子任务随机抽查 4 个。本批 40 条 → 抽 8 条：romantic-music, classical-period-music, cezanne, china-calligraphy-history（批次1）；gothic, renaissance, gregorian-chant, greek-art（批次2）。")
L.append("- 复检结论：见下方“复检结果”段（由 recheck 子任务回填）。")
L.append("")
L.append("## 已知限制与后续")
L.append("- 来源以权威百科为主，独立性偏低（见上），后续应补充博物馆官网、学术专著等不同机构来源。")
L.append("- L3 深度尚未开始；核心条目可在后续轮次升级。")
L.append("- 站点为零 JavaScript 纯静态 HTML，深色模式随系统偏好切换。")
open(os.path.join(ROOT,"REPORT.md"),"w",encoding="utf-8").write("\n".join(L))
print("REPORT.md written, blanks=%d, independent=%d/%d"%(len(blanks),nind,n))
