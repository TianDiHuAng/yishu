# DECISIONS.md — 决策记录

本文件记录无人值守模式下所有"不确定时选保守方案"的决定与理由。所有决定可被后续轮次复核。

## D001 — 无样板页，自建统一风格（依据 TASK 工作方式第1条）
- **决定**：项目文件夹内无样板页。自建一套"学术出版 / 博物馆图录"风格的 CSS 设计系统，写入 `site/assets/style.css`。
- **理由**：TASK 规定"如果没有样板页，就自行设计一套简洁统一的风格，并在 DECISIONS.md 记录"。
- **代价**：若日后出现样板页，需按 D002 的令牌集中原则替换变量值。

## D002 — 设计令牌集中化
- **决定**：所有配色/字号/间距通过 `:root` CSS 变量定义；深色模式用 `@media (prefers-color-scheme: dark)` 覆盖同名变量 + `html[data-theme="dark"]` 手动覆盖。内联 SVG 的文字使用 `fill="currentColor"` 或 CSS 变量类，保证浅深两色可读。
- **理由**：满足 TASK 关于"配色变量、深色模式、SVG 风格"的要求，且改一处即可全局换肤。
- **代价**：SVG 不能硬编码颜色，需统一走类。

## D003 — 输出位置：站点渲染到项目根目录（TASK 优先于 WORKFLOW）
- **决定**：`gen_site.py` 把静态站点渲染到项目根：`index.html` 为首页，条目页在 `entries/`，样式在 `site/assets/`（HTML 以 `site/assets/style.css` 引用）。源数据在 `data/`，工具在 `tools/`，报告在 `reports/`。GitHub Pages 部署根目录。
- **理由**：TASK 明确"网站首页用 index.html""所有文件都放在当前项目文件夹内"；WORKFLOW 的 `site/` 是通用约定，与 TASK 冲突时以本项目专用要求为准。
- **代价**：源数据与产出同处根目录，需在 README 中说明目录职责。

## D004 — 数据模型：条目统一为 JSON，按域分片
- **决定**：每个条目是 `data/entries_<域>.json` 中的一条记录，字段含 `id, title, kind(风格/时期/人物/作品/术语), era, region, medium, level(L1/L2/L3), tier(核心/重要/补充), def, when, overview, sections(L2+), svg, sources, needs_verification, pending_notes, related`。`data/coverage.json` 记录全量条目覆盖状态，`data/sources.json` 为全局来源库。
- **理由**：融合 TASK 的"层级写作 L1/L2/L3 + 条目页结构"与 WORKFLOW 的"JSON 数据层 + 机器校验 + 确定性渲染"。
- **代价**：需维护 coverage.json 与分片的一致性，由 check.py 强制。

## D005 — 双源规则与诚实标注
- **决定**：关键事实需 ≥2 个 `verified=true` 来源，否则该条目标 `needs_verification=true` 且 `pending_notes` 非空。查不到的年份/尺寸/收藏地一律不写或写"待补充"。
- **理由**：TASK 通用硬性规则与 WORKFLOW 双源规则。
- **代价**：`待核实` 比例可能偏高，属预期，批次复检需重点关注异常偏低的批次。

## D006 — 条目 id 规范
- **决定**：id 仅用 `a-z0-9-`，ASCII 引号/变音字母一律规避（ü→v），保证链接与文件名安全（沿用 WORKFLOW R16）。
- **理由**：避免引号截断 href、非 ASCII 文件名问题。
- **代价**：中文标题与 id 分离，需靠 title 字段展示。

## D007 — 每轮配额与续跑
- **决定**：每轮最多处理 40 个条目；写满配额后更新 coverage.json、输出覆盖报告、在 PROGRESS.md 记录下一轮起点并结束本轮。下轮先读 PROGRESS.md 续作。
- **理由**：TASK 分层写作"每轮最多处理40个条目"与"每次启动先读 PROGRESS.md"。
- **代价**：全流程跨多轮，需 goal 机制驱动自动续跑。

## D008 — L1 先行，禁止跳级深写
- **决定**：先把 scope 全部条目做到 L1（定义/时间或位置/一两句概述/相关条目），再按 核心→重要→补充 顺序升级 L2；L3 仅核心条目。L1 未全完成前不深写个别条目。
- **理由**：TASK 分层写作硬性要求。
- **代价**：首轮产出以广度为主，深度靠后续轮次补齐。

## D009 — 来源核验策略
- **决定**：`sources.json` 每条含 `id,title,author,year,url,type,verified,verified_note`。只有实际抓取页面并核对标题/作者/年份后置 `verified=true`；抓取失败或被反爬拒绝的保留 `verified=false` 并写 `pending`，不参与事实引用。
- **理由**：TASK 阶段1"打开页面核对标题、作者、年份后才能 verified=true"。
- **代价**：外部站点反爬会让部分来源长期 unverified，写作时需绕开这些来源或标待核实。

## D010 — 来源去重与校验器加固
- **决定**：sources 数组不得含重复 id（check.py R15），双源计数按唯一 id；新增4条已联网核验的权威百科来源（Cave painting / Venus figurine / Calligraphy / Ink wash painting），经 data/source_fixes.json 替换8个曾重复来源的条目。
- **理由**：第2批复检时发现8个条目把同一来源 id 写两次，旧校验器按出现次数计数导致"双源通过"的假阳性。这是机器校验诚实性的漏洞，必须堵上。
- **代价**：需维护 source_fixes.json 覆盖层；新增来源仍以百科为主，独立性限制（REPORT.md 已披露）未因此改变。

## D011 — Cycle1 新增5条中国艺术史条目（自治模式 B1）
- **决定**：新增 yangshao-painted-pottery、chinese-jade-art、shang-zhou-bronzes、dunhuang-art、six-dynasties-art 五条 scope 条目，归入 art-china-painting 单元。
- **理由**：缺口发现 B1 对照两份此前未用的权威大纲——国家高等教育智慧教育平台《中国艺术史》8章大纲（史前→晚清，含夏商周/魏晋南北朝/隋唐）与《中国美术史》教材目录（含彩陶艺术/玉器之美/早期岩画）——发现现有 scope 在中国史前—先秦—魏晋—隋唐的艺术门类覆盖薄弱。每条均有 ≥2 份已联网核验来源。新增5条 ≈ 现有109条的4.6%，低于10%单轮上限。
- **可逆方式**：删除 data/l2/ 下对应覆盖层，并从 catalog.py 移除这5行，重跑 build_scope.py + merge_l2.py 即可回退。
- **代价**：中国艺术史单元条目数增加，覆盖矩阵将新增若干格；来源仍以 Wikipedia 为主，独立性限制延续。


