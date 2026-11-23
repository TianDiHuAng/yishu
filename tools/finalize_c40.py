# -*- coding: utf-8 -*-
"""Cycle40 收尾：D043 + BLOCKERS 通道更新 + PROGRESS/PROJECT_STATUS 数字 + METRICS/SATURATION/REPORT。"""
import json,os,io
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D043 — Cycle40 新通道：博物馆开放数据 API 可达，新增 4 条目（145 → 149）
- **事实（2026-11-23 实测）**：`en/zh.wikipedia.org`、`metmuseum.org`、`tate.org.uk`、`web.archive.org`、`api.wikimedia.org`、`commons`、`wikidata.org` 全部 **HTTP 000（不可达）**；而以下通道可用：
  - **Cleveland Museum of Art 开放数据 API**（`openaccess-api.clevelandart.org`）：200，含 title/dates/technique/measurements/accession/credit/provenance/**策展说明正文**/`creators`（含生卒与传记）。
  - **V&A API v2**（`api.vam.ac.uk`）：200，藏品检索与对象记录、材料与尺寸、部分艺术家信息。
  - **Met object API**：**仅按对象 ID 可取**（436535 等），**检索接口已下线（410）**，无法按关键词发现藏品。
  - **Europeana API**（demo key）：200，但针对本批作品命中的都是**无关记录**（同名图书、苔藓标本等），不可作第二来源。
  - **DBpedia**：SPARQL 与 /data/ 均可访问，但该实例**不含英文 abstract**（仅短 description），不能当正文来源。
- **决定**：
  1. 新增来源类型「**权威机构藏品记录**」，URL 一律指向**实测 200 的 API 端点**；机构公网页（如 `clevelandart.org/art/…`）在本环境 000，故写入 `verified_note` 备注而非直接引用。
  2. **新增 4 条目**：`degas`（1834—1917）、`rodin`（1840—1917）、`rodin-age-of-bronze`（罗丹《青铜时代》，CMA 1918.328）、`mi-youren-cloudy-mountains`（米友仁《云山图》，CMA 1933.220）。条目 145 → **149**。
  3. **独立性如实标注**：`rodin` 有 2 个**不同机构**来源（CMA + V&A）；`degas`、`rodin-age-of-bronze`、`mi-youren-cloudy-mountains` 仅**单机构**，已按 R10 标 `needs_verification` 并在待核实首条写明「单一机构来源」。
  4. 只用机构记录能支撑的内容写作：**事实**（题名/纪年/材质/尺寸/藏品号/来源/题记/铭文）与**明确署名的策展说明**；评价性、谱系性判断一律留白进待核实。
- **理由**：这是本会话**第一次拿到可引用的机构级正文**（CMS 策展说明 + 艺术家传记），质量高于此前只能用的结构化数据；但同样必须守住"不据单一来源下断言"的红线，故单机构条目一律标记待核实，而不是靠"两条同馆文档"伪装双源。
- **可逆方式**：删除 4 条 overlay 与 catalog 元组、移除 4 条来源；`build_scope.py` 重跑即回到 145。
- **代价**：3 条条目带 `needs_verification`（本就如此，非新增缺陷）；Met 检索下线意味着无法系统发现 Met 藏品，只能被动获得对象 ID。
""")

io.open(os.path.join(ROOT,"BLOCKERS.md"),"a",encoding="utf-8").write("""
## Cycle40 通道再测绘（2026-11-23）

| 主机/端点 | 状态 | 说明 |
|---|---|---|
| en/zh.wikipedia.org | 000 | 不可达（此前亦如此） |
| api.wikimedia.org / commons / wikidata.org | 000 | **本轮新增不可达**（此前 Wikidata 可用） |
| web.archive.org | 000 | 存档读取亦不可用 |
| dbpedia.org（/data/、/sparql） | **200** | 可查，但**无英文 abstract**，仅短 description |
| openaccess-api.clevelandart.org | **200** | 完整藏品记录 + 策展说明 + creators 传记 ✅ |
| clevelandart.org（网页） | 000 | API 可用但网页不可达 |
| api.vam.ac.uk | **200** | 藏品检索/对象/材料/尺寸 ✅ |
| collections.vam.ac.uk/item/... | **200** | 对象页可达 ✅ |
| collectionapi.metmuseum.org（objects/{id}） | **200** | 仅按 ID；**search 已 410** |
| api.europeana.eu（demo key） | **200** | 命中多为无关记录 |
| api.smk.dk | **200** | 丹麦国立美术馆藏品 |
| gutenberg / smarthistory / metmuseum.org / tate / nga / moma / unesco / persee | 000/403/503 | 不可用 |
| WikiArt | 200 | 可达但非权威，未采用 |

**结论**：内容来源从"仅 Wikidata"升级为"**博物馆 API + V&A + Europeana + SMK**"，可支撑作品级事实与策展说明；仍无法获取百科/专著级别的通史叙述。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle40","date":"2026-11-23","status":"completed",
 "gap_methods":["通道再测绘","机构藏品记录来源"],"network":"partial: museum APIs ok, wikipedia/wikidata 000",
 "new_entries":4,"upgrades":0,"reviews":4,"fixes":2,
 "new_entry_ids":["degas","rodin","rodin-age-of-bronze","mi-youren-cloudy-mountains"],
 "new_sources":4,"sources_total":283,
 "entries_total":149,"pages":180,
 "single_institution_flagged":["degas","rodin-age-of-bronze","mi-youren-cloudy-mountains"],
 "dual_institution":["rodin"],
 "check_result":"errors=0","check_links_result":"broken=0(180页)","audit_all":"8/8 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle40","date":"2026-11-23","methods_used":["博物馆API","通道再测绘"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)",
 "verdict":"新通道打开：新增 4 条目（149）；1 条双机构、3 条单机构已标记；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle40"' not in t:
    block=('if cyc=="cycle40":\n'
           '    L.append("- **通道再测绘后的实质扩充**：Wikipedia/Wikidata/archive.org 本轮均为 000，'
           '但发现 **博物馆开放数据 API 全部可达**（Cleveland 开放数据 API、V&A API v2、Met 对象端点、Europeana、SMK）。'
           '据此新增 **4 个条目（145 → 149）**：德加、罗丹、罗丹《青铜时代》、米友仁《云山图》；'
           '来源类型新增「**权威机构藏品记录**」，URL 指向实测 200 的 API 端点（机构网页 000 已在 verified_note 注明）。'
           '独立性如实区分：罗丹为 **CMA + V&A 双机构**；其余 3 条为单机构，已按 R10 标 needs_verification 并在待核实首条写明。'
           '本次首次取得可引用的**机构级正文**（策展说明与艺术家传记），但评价性判断仍一律留白。'
           '站点 176 → **180 页**，八步体检 8/8。")\n')
    anchor='if cyc=="cycle39":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

# PROGRESS 数字
PP=os.path.join(ROOT,"PROGRESS.md"); s2=io.open(PP,encoding="utf-8").read()
s2=s2.replace("| 条目 | 145（L2 139 / L3 6 / L1 0） |","| 条目 | 149（L2 143 / L3 6 / L1 0） |")
s2=s2.replace("| 来源 | 279（全部 verified；隔离区 5 条不可核验） |","| 来源 | 283（全部 verified；隔离区 5 条不可核验） |")
s2=s2.replace("| 页面 | 176，站内断链 **0** |","| 页面 | 180，站内断链 **0** |")
s2=s2.replace("- 当前轮次：**Cycle 39/40 收尾已完成（结构完成 → 维护模式待命）**",
              "- 当前轮次：**Cycle 40 已完成（新增 4 条目 145→149）**")
io.open(PP,"w",encoding="utf-8").write(s2)
print("progress updated")