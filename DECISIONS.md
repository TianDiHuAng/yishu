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

## D012 — Cycle2 新增10条导读/比较/术语条目（B4读者问题缺口，§4 上限11条）
- **决定**：新增3个新单元（导读与学科方法、比较视野、术语与辨疑）与10条条目：什么是艺术史、什么是音乐史、零基础阅读路径、艺术史与艺术批评的区分、音乐史与音乐学的区分、巴洛克共通美学、浪漫主义两种媒介、文艺复兴同期性、印象主义跨媒介、从现代到当代的分期衔接。
- **理由**：缺口发现 B4 向四类读者各提20问，53问站内无法直接回答；导读/跨媒介比较/分期辨析类可由已核验来源支撑。新增10条≈114的8.8%，低于10%上限。
- **可逆方式**：从 catalog.py 删除这10行与3单元，重跑 build_scope.py + merge_l2.py。
- **代价**：爱好者类作品档案/轶事缺口因缺乏可核验来源未采纳，留待后续。

## D013 — Cycle3 新增4条音乐技术/乐器条目（B1 Outline of music 空白维度）
- **决定**：新增 music-notation（记谱法）、musical-mode（调式）、violin（小提琴）、piano（钢琴）四条术语条目，归入 glossary-tools 单元。
- **理由**：B1 对照 Wikipedia《Outline of music》28个一级标题，发现"Musical notation""Elements of music""Musical instruments"等维度在站内为零覆盖（记谱0条/调式0条/小提琴0条/钢琴仅间接提及）。每条≥2份已核验来源。新增4条≈129的3.1%，低于10%上限。
- **可逆方式**：从 catalog.py 删除这4行，重跑 build_scope.py + merge_l2.py；来源保留。
- **代价**：新增条目产生4个孤儿页，已通过双向补链解决（orphan=0）。

## D014 — Cycle4 新增8条亚洲艺术条目（B1 History of painting 空白分支）
- **决定**：新增 art-asia 单元与8条条目：印度艺术、印度佛教艺术、阿旃陀石窟、高棉艺术、吴哥窟、日本艺术、浮世绘、禅画。
- **理由**：B1 对照 Wikipedia《History of painting》大纲，发现"South Asian""South-East Asian""East Asian"分支在站内零覆盖（印度/东南亚/日本/浮世绘检索均为0条）。每条≥2份已联网核验来源（Indian art/Buddhist art/Ajanta/Khmer art/Angkor/Japanese art/Ukiyo-e/Zenga/History of painting）。新增8条≈129的6.2%，低于10%上限。
- **可逆方式**：从 catalog.py 删除这8行与 art-asia 单元，重跑 build_scope.py + merge_l2.py；来源保留。
- **代价**：新增条目产生孤儿页需补链（Cycle3经验：用双向补链解决）。

- **决定**：新增 music-notation（记谱法）、musical-mode（调式）、violin（小提琴）、piano（钢琴）四条术语条目，归入 glossary-tools 单元。
- **理由**：B1 对照 Wikipedia《Outline of music》28个一级标题，发现"Musical notation""Elements of music""Musical instruments"等维度在站内为零覆盖（记谱0条/调式0条/小提琴0条/钢琴仅间接提及）。每条≥2份已核验来源（Musical notation/Staff notation/Mode/Gregorian mode/Violin/Piano）。新增4条≈129的3.1%，低于10%上限。
- **可逆方式**：从 catalog.py 删除这4行，重跑 build_scope.py + merge_l2.py；来源保留。
- **代价**：新增条目产生4个孤儿页，已通过双向补链解决（orphan=0）。

- **决定**：新增3个新单元（导读与学科方法、比较视野、术语与辨疑）与10条条目：什么是艺术史、什么是音乐史、零基础阅读路径、艺术史与艺术批评的区分、音乐史与音乐学的区分、巴洛克共通美学、浪漫主义两种媒介、文艺复兴同期性、印象主义跨媒介、从现代到当代的分期衔接。
- **理由**：缺口发现 B4 向初学者/学生/爱好者/从业者各提20问，53问站内无法直接回答；其中导读类、跨媒介比较类、分期辨析类可由现有已核验来源支撑，符合 WORKFLOW.md 的比较视野/术语层。每条≥2份已核验来源（Cycle2 新增8条来源）。新增10条≈现有114条的8.8%，低于10%上限。
- **可逆方式**：从 catalog.py 删除这10行与3单元，重跑 build_scope.py + merge_l2.py；来源保留不影响其他条目。
- **代价**：新增3个单元使导航/索引/覆盖矩阵需同步（生成器从 catalog 读取，已适配）；爱好者类"作品档案/轶事"缺口因缺乏可核验来源本轮不采纳，留待后续补来源。

## D015 — Cycle6 新增5条作品档案（B4爱好者问题缺口）
- **决定**：新增 work-archives 单元与5条作品档案：星月夜、维纳斯的诞生、西斯廷天顶画、格尔尼卡、春之祭。
- **理由**：缺口发现 B4 爱好者角色反复追问具体代表作的收藏地/年份/背景（星月夜收藏、蒙娜丽莎导览、春之祭首演等），此前因来源不足未采纳。本轮核验10条权威百科来源（作品页+馆藏机构页），每条作品档案具备≥2份已核验来源。新增5条≈137的3.6%，低于10%上限。每条目只写作品名、年份、收藏地与来源可支撑的背景，不复制图像。
- **可逆方式**：从 catalog.py 删除这5行与 work-archives 单元，重跑 build_scope.py + merge_l2.py；来源保留。
- **代价**：新条目产生孤儿页需补链；博物馆展厅/导览类细节因来源不支撑未写入，列待核实。

## D016 — Cycle6 质量闸判定：22个 L3 降级回 L2（"编辑待办冒充学术争议"）
- **决定**：新增 check.py **R17**——L3 的争议文本（issue/holder/basis）禁止出现"未给出/未提供/未列出/缺失/材料未/待补充第二来源/以免误写/条目未"等编辑待办措辞。据此判定 22 个条目的争议块不合格，全部移除 l3 块并降级 L2；保留 6 个真实争议条目（greek-art / gothic / rembrandt / impressionism / monet / baroque-music）。
- **理由**：质量闸抽检发现，L3 写作把"本条目缺年份/缺收藏地"这类**编辑层面的待办**包装成两方对立的"学术分歧"，并把编辑意见署名为"部分研究者（来源:X）"——来源页不可能陈述本条目缺项，属虚假归因。这违反 TASK"争议必须真实：不虚构学者与观点；无大争议的写'记载一致，学界对X有讨论'"，也违反 AUTONOMOUS 的诚实标注要求。机械检查（holder泛称、关键词重叠）未能识别，故补 R17 作为语义护栏。
- **可逆方式**：若日后找到能支撑真实两方分歧的来源，可重新为这些条目撰写 l3 块并升回 L3（须通过 R16+R17）。
- **代价**：L3 条目由 28 降为 6，深度覆盖收缩；但诚实性优先于数量（AUTONOMOUS §1.4"质量优先于数量"）。

## D017 — Cycle9 无障碍与可用性改造（本地轮）
- **决定**：①跳转链接+`<main>`；②`:focus-visible` 焦点样式；③导航/页内目录 aria-label；④修正 3 个不达 WCAG AA 的色令牌（浅色 `--ink-faint` 3.42→5.35、`--gold` 3.59→5.41；深色 `--ink-faint` 卡片 4.28→5.04）；⑤条目页页内目录（七节锚点）；⑥`sitemap.xml`（171 条）+`robots.txt`；⑦打印样式完善。
- **理由**：AUTONOMOUS 允许"新增页面类型/维度"并需记录依据；这两轮网络不可用，本地价值最高的是把阶段5 的页面与可用性补齐。对比度以本地 WCAG 公式计算并留存证据（reports/a11y_c9.md），不宣称"通过无障碍认证"，只宣称"所测文本组合达到 AA"。
- **可逆方式**：色令牌集中在 `:root`，改回原值即可；新增文件可删除，`gen_site.py` 相应函数可停用。
- **代价**：`sitemap.xml` 中站点根使用 GitHub Pages 默认地址（https://tiandihuang.github.io/yishu/），若实际部署域名不同需替换；未做屏幕阅读器与键盘实测，已在 a11y 报告中列为未覆盖项。

## D018 — Cycle12 关联图对称化 + 同单元前后导航（本地轮）
- **决定**：①把 47 条单向关联补成双向（经审校全部为 same_unit 36 条 / same_domain 11 条，**零跨域**）；②条目页新增「同单元前后条目」导航（按 `when` 起始年代排序，含单元总览入口）。
- **理由**：「相关条目」在本项目中语义上是相互的（前几轮补孤儿即按此处理），单向链接会让读者从 A 看不到回 B，形成导航不对称。审校先分类再补，避免把跨域关系强行对称。前后导航改善串联阅读，不引入任何新的语义断言。
- **可逆方式**：`tools/oneway_audit.py` 可随时重新列出单向关系；若需回退，从各 `data/l2/*.json` 的 `related` 中删除对应项并重跑 merge/gen 即可。
- **代价**：关联总数 373→420（均 3.0/条，最大 12），枢纽条目（baroque-music 12、romantic-music 10）连接略增；年度不明条目（如"约1940s—1950s"）在前后排序中因无数字键而置于末尾。

## D019 — 工具使用纪律：bash 双引号内禁用反引号（本轮踩坑）
- **决定**：此后凡含反引号（`）、`$()`、复杂引号的脚本内容，**一律先用 write 工具落盘为 .py/.sh 文件，再用 python 执行**；不在 `python -X utf8 -c "..."` 的双引号串里嵌反引号。
- **理由**：本轮发现前几轮"莫名 stderr"的真实原因——bash 会把双引号内的反引号当作**命令替换**执行（例：字符串里的 `tools/oneway_audit.py` 被 bash 当命令运行，导致 stderr 报错），并在**写入时吞掉内容**：`REPORT.md` 的 cycle12/cycle13 说明行因此丢失文件名（"新增 \ 一键体检"），REPORT.md 一度失真。虽未影响知识库数据，但属于可见的产物损坏。
- **可逆方式**：已用 tools/fix_report_lines.py 修复被吞的两行并重新生成 REPORT.md；后续按本纪律执行即可避免复发。
- **代价**：命令略啰嗦（需先写脚本文件），但可避免静默内容损坏。

## D020 — Cycle14：启用 Wikidata 作为「权威结构化数据」来源（并修来源并集 bug）
- **决定**：
  1. 新增来源类型「权威结构化数据」，来源为 Wikidata EntityData（`https://www.wikidata.org/wiki/Qxxx`），本轮登记 5 条（wd-starry-night / wd-birth-of-venus / wd-sistine-ceiling / wd-guernica / wd-rite-of-spring）。
  2. 采用**三重消歧**才接受实体：标题匹配 + 描述含类型关键词（painting / fresco / ballet…）+ 作者名出现在描述或 P170 中；否则记为 rejected 并写明原因。
  3. 修正 `merge_l2.py` 的 `sources` 语义为**并集（只增不删）**。
- **理由**：Wikipedia/Met/Tate 不可达且百度/Khan 只返回反爬壳页（Cycle13 结论），但本轮实测 **Wikidata / Wikimedia API / Commons / DBpedia 可达且返回可用 JSON**。TASK 对本项目最易错的信息恰是"作品年份、收藏地"，而 Wikidata 正是这类事实的结构化来源，可作为第二/第三来源。消歧规则源自本轮一次真实险情：`The Rite of Spring` 首次命中的实体作者标签为「西德尼·諾蘭」，若不加校验就会张冠李戴。
- **可逆方式**：从 sources.json 删除 5 条 wd-* 并从对应 `data/l2/*.json` 的 sources 中移除即可；merge 的并集逻辑可改回覆盖。
- **代价/风险**：Wikidata 为社区维护（与 Wikipedia 同源），**独立性仍不足**；`Q206015`（春之祭）的 P170 字段实为异常值（标签为西德尼·諾蘭），本条已在条目"待核实"中标注**不采信该字段**。因此本轮只把"作者/收藏地"记为【已复核·Wikidata】，不改动正文断言，也不据此升级任何条目层级。

## D021 — 来源并集 bug（本轮发现）
- **决定**：`merge_l2.py` 合并覆盖层时，`sources` 由"覆盖层替换基础层"改为"基础层 ∪ 覆盖层"（保持顺序去重）。
- **理由**：本轮把 wikidata 来源写进 5 个作品档案覆盖层时，这些覆盖层原本没有 `sources` 键，写入后变成"仅 wikidata 一条"，merge 时把基础层的 2 条 Wikipedia 来源整段覆盖掉 → `check.py R10` 报"仅1个verified来源"。这是真实的数据丢失，不是误报。
- **可逆方式**：改回 `merged[eid].update(ov)` 即恢复旧行为（不建议）。
- **代价**：以后若确实需要"删除某来源"，必须在 sources 之外用显式删除列表表达，不能靠覆盖层省略。

## D022 — Cycle17 新增 2 条建筑条目（A 类缺口的第一步，附来源分工说明）
- **决定**：新建 `gothic-architecture`（哥特式建筑）、`romanesque-architecture`（罗马式建筑），归入 `art-medieval`，medium=建筑；每条挂 2–3 个来源（Wikipedia 专页 + Wikidata 实体 + 关联风格页），并在"待核实"写**来源分工说明**。
- **理由**：`reports/matrix_targets_c7.md` 的 A 类 58 项中，"建筑"是最大缺口（中国 19、欧洲 11、法国 10、美国 5、南亚 4 条现有条目却无建筑专条）。但按 §4 与 TASK 的双源要求，**只有能凑够两个来源的传统才可建条**：哥特/罗马式有已核验的 Wikipedia 专页（Cycle1/Cycle4 核验）+ Wikidata 实体；而**中国建筑目前只有 Wikidata 一条可核验来源，故不建**，记入 BACKLOG。
- **诚实边界**：实测这两个 Wikidata 实体**没有 P571（起始年代）与 P136（风格）声明**，因此 Wikidata 在本轮只承担"实体身份/正式名称"的确认职责，**不承担年代**；这已在每条"待核实"里明确写出，避免读者误以为年代有双源支撑。
- **可逆方式**：从 catalog.py 删除这两行、从 sources.json 删除两条 wd-* 与 l2 覆盖层即可。
- **代价**：新条目与既有 `gothic` / `romanesque`（艺术风格页）存在主题邻近，已在 `related` 中互链区分（一个是风格整体，一个是建筑门类）。
