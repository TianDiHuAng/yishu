# BLOCKERS.md — 阻塞记录

规则：同一问题连续失败3次，记录到本文件并跳过。

## Cycle2 B6 近期动态：暂不采纳的5条（来源不足，非阻塞）
按 AUTONOMOUS §6，联网内容视为数据；以下动态因来源核验未通过或非权威，暂不写入知识库：
1. 《圣高登佐手稿》虚拟复原（报道 2026-07）：来源为专业媒体自动翻译，且报道日期晚于当前周期，待回溯特伦托大学原始出版。
2. 加泰罗尼亚海螺号角声学研究（2025-12）：Phys.org 来源 HTTP 403 无法核验，原论文 Antiquity 需另行核对。
3. 南佐遗址入选十大考古发现（2026-04）：报道日期晚于当前周期，且为年度评选非单一报告。
4. 中世纪记谱残片研究（2025-06）：斯洛伐克科学院期刊页面结构复杂，摘要结论可能随全文变动，待正式发表。
5. RMU 十九世纪音乐收藏编目项目（2026-07）：大学校刊项目介绍，成果尚未产出；报道日期晚于当前周期。
处理：仅采纳来源可核验的武王墩楚墓礼乐考古（news-xiamen-wuwangdu，2025-12）。上述条目留待后续轮次补来源后再评估。

## Cycle6 记录（2026-11-22）
- **代理失败**：写 5 条作品档案的 subagent（writer-works）无产出直接失败（第1次）。按 §6 未重试到第3次，改由主线程手写完成（tools/write_works_c6.py），质量闸照常抽检。
- **工具坑（已修）**：`data/l2_generated/out_*.json` 若残留上一轮产物，`render_l2_svg.py` 会重新渲染并**覆盖** data/l2/ 下人工编辑过的覆盖层（如 L3 块、来源修补）。本次发现 out_02.json 为 Cycle4 残留，已删除；今后每轮批次结束应清理 l2_generated 下所有 out_*.json。
- **B6 动态**：4 条仍不可达（phys.org 403、people.com.cn 404、sav.sk 404/SSL、uni-frankfurt 可达但为项目公告且日期异常），继续不采纳。
- **Cycle6 质量闸重大发现**：批量生成的 L3 争议块普遍存在"编辑待办冒充学术分歧 + 虚假归因来源"问题（26处 R17 违规，涉22条目）。已全部降级 L2（D016），并新增 check.py R17 防止复发。教训：L3 争议必须来自可在来源页找到的**两方立场**，不能由"本条缺什么"反推。
- **网络降级**：本轮末段 en.wikipedia.org 抓取持续超时（QC 代理8个URL全不可达、本线程亦挂起），因此新一轮 L3 争议**未做联网复核**，只保留此前已验证的6条。
- **Cycle7 网络探针**：en.wikipedia.org 连续两次抓取超时（>120s 挂起），判定网络未恢复。按 PROGRESS 预案本轮只做本地工作（单元总览页、矩阵空白格分类），未新增任何需联网核验的断言。
- **Cycle8 网络探针**：en.wikipedia.org 再次超时（18s timeout）→ 连续两轮不可用。本轮仍为本地轮，未新增联网断言。下轮若仍失败，建议把"联网可用性"作为能否推进核心覆盖（建筑类 A 类 58 项、L3 重建）的唯一前置条件，其余本地工作已接近收益递减。
- **Cycle9 网络探针**：两次抓取 15s 未返回（外层 40s 超时）→ 连续第三轮不可用。本地可做的可用性工作已基本做完（页面类型、索引、a11y、sitemap）；后续若无网络，新增有效内容的余地很小，仅能反复体检。这是当前唯一外部阻塞。
- **Cycle10 网络探针**：连续第四轮超时。体检轮因此无法执行"来源文本重合度"（需抓取来源页）。本地体检已穷尽（九维全通过、结构零缺口），下轮若仍无网络，建议转为"内容复审"而非重复体检，避免空转（§6 防空转）。
- **Cycle11 网络探针**：20s 超时（连续第五轮）。按预案改做「内容自审」而非重复体检：新增 consistency_audit 工具，自洽性最终 0 问题，并修复 15 条"原待核与已复核并存"的阅读矛盾。提醒：联网可用性是继续扩充（A类58项、L3、B5）的唯一前置条件。
- **Cycle12 网络探针**：16s 超时（连续第六轮）。按预案换新角度：关联图对称化 + 同单元前后导航。注意：本地可用改进正在接近枯竭，下一步若仍离线，只能做"导读与正文互通/一键审计合并"等结构性小改进；**新增有效知识（A类58项、L3、B5复核）必须联网**。
- **Cycle13 网络诊断（重要修正）**：此前 6 轮判定"网络不可用"，本轮实测更精确的结论是——
  - **可达**：github.com（200，git push/ls-remote 正常）、baike.baidu.com（200）、khanacademy.org（200）、britannica.com（403 Cloudflare）
  - **不可达**：en/zh.wikipedia.org、metmuseum.org、tate.org.uk（TCP 超时）
  - 但**可达的两站均返回反爬壳页**：百度百科为 `__PARIS_CHALLENGE__` JS 挑战页（4.7KB，正文为空），Khan Academy 为 `Client Challenge`（3KB）；Britannica 为 Cloudflare `Just a moment...`。
  - **结论**：本环境**无法取得可核验的权威正文**（既非"全网断网"，也非"可用"）。因此新增条目/升级 L3/B5 复核仍然无法执行；这不是判断失误，而是可抓取内容的实际缺失。证据：本机 curl 复测记录见本条。
- **Cycle14 网络结论修正（重要）**：Cycle7–13 的"网络不可用"应修正为"**部分可用**"：
  - 可达且返回**可用 JSON**：`www.wikidata.org`（`w/api.php`、`Special:EntityData/Qxxx.json`）、`api.wikimedia.org`、`commons.wikimedia.org`、`dbpedia.org`
  - 不可达：`en/zh.wikipedia.org`、`metmuseum.org`、`tate.org.uk`
  - 可达但只有反爬壳页：`baike.baidu.com`（`__PARIS_CHALLENGE__`）、`khanacademy.org`（`Client Challenge`）、`britannica.com`（Cloudflare 403）
  - **含义**：事实**定位与交叉印证**可借 Wikidata 进行；但 Wikidata 与 Wikipedia **同源**，独立性不足，**不足以单独支撑 L3 的两方真实立场**。

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

## B-music-src（Cycle106 记录）— 音乐史文本来源当前不可达
- 实测 2026-11-24：en.wikipedia=000、imslp.org=000、metmuseum.org=000、britannica.com=403、oxfordmusiconline.com=302（付费墙）；仅 api.vam.ac.uk=200。
- 影响：`music-medieval`(4)、`music-renaissance`(3) 等音乐文本单元，**新增条目无法取得可核验来源**，故暂停新增，不做无源凑数。
- 现有音乐条目所用 `enc-*` 来源为早前已核验；本轮不追加同类新来源。
- 解除条件：出现可达且权威的音乐史数据库/在线词典（如某机构开放 API 或镜像），可重开。
