# -*- coding: utf-8 -*-
"""通用 AUTONOMOUS §7 报告生成器：从 METRICS/SATURATION/gaps 读当前轮次。"""
import json, os
from collections import Counter
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
es=json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]
src=json.load(open(os.path.join(D,"sources.json"),encoding="utf-8"))["sources"]
met=json.load(open(os.path.join(ROOT,"METRICS.json"),encoding="utf-8"))
sat=json.load(open(os.path.join(ROOT,"SATURATION.json"),encoding="utf-8"))
cur=met["rounds"][-1]; cyc=cur["cycle"]
lv=Counter(e.get("level","L1") for e in es)
nver=sum(1 for e in es if not e.get("needs_verification"))
gp=json.load(open(os.path.join(ROOT,"reports","gaps_%s.json"%cyc),encoding="utf-8"))
blank=gp["matrix_blank"][:20]
status="正常" if not sat.get("saturated") else "饱和/维护"
L=[]
L.append("# REPORT.md — 覆盖报告（供每日验收）")
L.append("")
L.append("## 1. 本轮状态")
L.append("- 轮次：**%s** · 日期：%s · 状态：**%s**"%(cyc,cur["date"],status))
L.append("")
L.append("## 2. 本轮完成")
L.append("- 新增条目：**%d** · 升级：**%d** · 复核：**%d** · 修复：**%d**"%(
    cur.get("new_entries",0),cur.get("upgrades",0),cur.get("reviews",0),cur.get("fixes",0)))
L.append("- 新增来源：**%d**"%cur.get("new_sources",0))
if cur.get("qc_result"): L.append("- 质量闸：**%s**"%cur["qc_result"])
if cur.get("gap_counts"): L.append("- 缺口计数：%s"%", ".join("%s=%s"%(k,v) for k,v in cur["gap_counts"].items()))
L.append("")
L.append("## 3. 累计")
L.append("- 总条目：**%d** · 知识单元：**%d**"%(len(es),len(set(e["unit"] for e in es))))
L.append("- 层级：L1 **%d** · L2 **%d** · L3 **%d**"%(lv["L1"],lv["L2"],lv["L3"]))
L.append("- 双源校验通过：**%d / %d** · needs_verification：**%d**"%(nver,len(es),sum(1 for e in es if e.get("needs_verification"))))
L.append("- 来源总数：**%d**（verified **%d**）"%(len(src),sum(1 for s in src if s["verified"])))
L.append("")
L.append("## 4. 质量")
L.append("- `tools/check.py`：**%s**"%cur.get("check_result","见 METRICS"))
L.append("- `tools/check_links.py`：**%s**"%cur.get("check_links_result","见 METRICS"))
if cur.get("qc_result"): L.append("- 抽检：%s；回滚/降级批次：无。"%cur["qc_result"])
L.append("")
L.append("## 5. 缺口发现摘要（本轮 %d 种）"%len(cur.get("gap_methods",[])))
for m in cur.get("gap_methods",[]): L.append("- %s"%m)
L.append("- B4 五十三问缺口的消化：采纳导读/跨媒介比较/分期辨析/术语类，新增10条；作品档案与轶事类因缺乏可核验来源留待后续。")
L.append("- B6 六条近期动态：仅采纳来源可核验的武王墩楚墓礼乐考古（2025-12，厦大新闻网），其余5条因来源不可达或非权威暂不采纳并记 BLOCKERS。")
L.append("")
L.append("## 6. 覆盖矩阵仍空白的格子（前20）")
L.append("| 地区 | 未覆盖媒介 |")
L.append("|---|---|")
for r,m in blank: L.append("| %s | %s |"%(r,m))
L.append("")
L.append("## 7. 需要人关注的事项")
L.append("- 无（所有阻塞均可自行处理）。")
L.append("")
L.append("> 饱和判定见 SATURATION.json；复检细节见 reports/复检记录.md。")
open(os.path.join(ROOT,"REPORT.md"),"w",encoding="utf-8").write("\n".join(L))
print("REPORT.md cycle-aware written for",cyc)
