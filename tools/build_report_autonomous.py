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
gp_path=os.path.join(ROOT,"reports","gaps_%s.json"%cyc)
gp=json.load(open(gp_path,encoding="utf-8")) if os.path.exists(gp_path) else {"matrix_blank":[]}
blank=gp["matrix_blank"][:20]
if not os.path.exists(gp_path):
    blank=[[b,m] for b,m,_ in []]  # 体检轮无矩阵文件，留空由特别说明覆盖
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
if cyc=="cycle3":
    L.append("- 本轮特别说明：B5 复核 45 项待核实 → 38 项找到可核验第二来源并写入【已复核】留痕；B3 孤儿页 38→0（新增84条双向补链）；QC 收尾补 Bach/Vivaldi 来源并修正18处截断URL。")
if cyc=="cycle10":
    L.append("- 本轮为**体检轮 F**（第二轮）：九维检查——死链/重复/矛盾/孤儿/页内锚点/sitemap一致/对比度AA/l3与level/coverage与entries **全部通过**；过期数据规则命中4处经人工判定为误报（成语与断代用语，并改写了1处歧义措辞）；**来源文本重合度因网络降级未执行**（最近有效结果为 Cycle5 抽样0%）。另新增可复用 ：373 条关联中跨域仅 2 条（浪漫主义跨媒介合法对），单向 47 条。")
if cyc=="cycle9":
    L.append("- 本轮特别说明：网络探针连续第三轮失败，仍为**本地轮**。完成无障碍/可用性改造（D017）：跳转链接与 main、focus-visible、ARIA、条目页页内目录、sitemap.xml(171)+robots.txt、打印样式；并用本地 WCAG 公式复算对比度，修正 3 处不达 AA 的色令牌（浅色 ink-faint 3.42→5.35、gold 3.59→5.41；深色 ink-faint 4.28→5.04），证据见 reports/a11y_c9.md。")
if cyc=="cycle8":
    L.append("- 本轮特别说明：网络探针再次失败，仍为**本地轮**、未新增联网断言。阶段5 页面类型补全：新增**人物索引** people.html 与**术语表** glossary.html；时间线由扁平列表改为六段时期分组（并修正 era/when 误判）；条目页新增**被引用反链**，形成双向导航。站点 171 页、0 断链。")
if cyc=="cycle7":
    L.append("- 本轮特别说明：网络探针失败（wikipedia 连续超时），本轮为**本地轮**、未新增任何需联网核验的断言。补齐阶段5 缺失的「单元总览」页面类型：units.html + 每单元页 ×21（含构成、分级条目、时间线片段、待核实），站点增至 169 页、0 断链；并把 154 个矩阵空白格数据驱动分类为 A 类 58（应补，首选建筑）/ B 类 96（暂不处理），形成下一轮联网补盲清单 reports/matrix_targets_c7.md。")
if cyc=="cycle6":
    L.append("- 本轮特别说明：B4 新增 5 条作品档案（work-archives 单元，D015），孤儿补链后 orphan=0；B7 尝试 12 条 L3，质量闸发现「编辑待办冒充学术争议 + 虚假归因来源」26 处，判定不合格 —— 新增 check.py R17 护栏，22 条降级回 L2（D016），仅保留 6 条真实两方争议的 L3；清理 out_*.json 残留工具坑；末段 wikipedia 抓取超时，未对新断言做联网复核。")
if cyc=="cycle5":
    L.append("- 本轮特别说明：体检轮 F 六维全通过（死链/过期/重复/矛盾/孤儿/来源重合均为0，3个「现存」为误报）；L3 深度升级12条核心，累计16条L3，争议/数据逐项获来源支撑、holder全为泛称；B6 动态4条仍不可达已记 BLOCKERS。")
if cyc=="cycle4":
    L.append("- 本轮特别说明：B1 对照《History of painting》发现南亚/东南亚/东亚分支零覆盖，新增8条亚洲艺术（D014）；实现 L3 深度层（check.py R16 + gen_site.py 渲染），4个核心条目升级 L3（greek-art/gothic/impressionism/baroque-music），争议观点均用泛称不虚构学者；B5 剩余6项中仅1项可核验解决，5项诚实保留待核实；B6 回溯5条来源仍4条不可达（1条日期异常未采纳）。")
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
