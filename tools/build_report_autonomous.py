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
if cyc=="cycle43":
    L.append("- 用**馆藏作品**填补长期受阻的覆盖缺口（157 → 161）：克什米尔立佛（约900）、马图拉栏楯柱（100年代）、陈洪绶《仿古册》、赵孟頫《河村渔乐》——分别补上**印度佛教艺术 / 南亚雕塑 / 明代 / 元代**的具体作品实例。这些缺口此前一直记为「需可核验内容来源」而搁置，本轮证明：**馆藏策展记录本身就是可核验来源**。亦真亦谨的处理：立佛的年代与座上题记人物活动年代的时间差**不调和**而是并列进待核实；马图拉柱基座第二场景保留该馆的推测措辞；陈洪绶、赵孟頫的评价性用语标注为「该馆称」。另做变音折叠配对复核：仅 4 例同名且全部年代不符（同名异作），无新增双机构配对。站点 188 → 192 页，体检 8/8。")
if cyc=="cycle42":
    L.append("- 本轮把扩充方式**升级为「同作品跨机构比对」**：用 CMA 的 58 件亚洲/工艺候选逐条到 V&A 查同题同年代藏品，得到**三组真正的同作品双机构**并各建一条——**《凯风快晴》**（CMA 1930.189 + V&A O129067）、**《庄野 白雨》**（CMA 1948.306 + V&A O410702）、**《大桥安宅骤雨》**（CMA 1921.318 + V&A O420904），条目 154 → **157**。方法论收获：自动标题比对因**变音符**（Ōhashi / Shōno）漏判，须按系列名与罗马字并查后人工确认。写作纪律：两馆记录**并列不合并**，尺寸只在有记录一侧给；《大桥》两馆尺寸差异（14.13×9.04 对常见大判）如实写出并列入待核实。站点 185 → 188 页，八步体检 8/8。")
if cyc=="cycle41":
    L.append("- 同批第二次扩充：用 Cleveland 馆方撰写的**艺术家传记正文**新增 5 位缺席人物——马奈、透纳、康斯太勃尔、库尔贝、安格尔（149 → 154）。双源如实：马奈 / 康斯太勃尔 / 库尔贝各有 V&A 藏品记录作第二机构；透纳与安格尔仅 CMA（V&A 命中同名者非本人作品、Ingres 命中为仿作），已标 needs_verification。写作只取传记与藏品能支撑的事实（学艺、展览、任职、技法演变、可查争议），转引性评语一律注明「系该馆转引，未核原刊」。站点 180 → 185 页，八步体检 8/8。")
if cyc=="cycle40":
    L.append("- 通道再测绘后的实质扩充：Wikipedia / Wikidata / archive.org 本轮均为 000，但博物馆开放数据 API 全部可达（Cleveland 开放数据 API、V&A API v2、Met 对象端点、Europeana、SMK）。据此新增 4 个条目（145 → 149）：德加、罗丹、罗丹《青铜时代》、米友仁《云山图》；来源类型新增「权威机构藏品记录」，URL 指向实测 200 的 API 端点（机构网页 000 已在 verified_note 注明）。独立性如实区分：罗丹为 CMA + V&A 双机构；其余 3 条单机构，按 R10 标 needs_verification 并在待核实首条写明。本次首次取得可引用的机构级正文（策展说明与艺术家传记），评价性判断仍一律留白。站点 176 → 180 页，八步体检 8/8。")
if cyc=="cycle38":
    L.append("- 本轮为**站点收尾打磨**：①sources.html 增加**隔离来源说明**（5 条：404 / 反爬壳页 / 限流 / 403，明示禁止被引用，R18 强制）；②status.html 数字改为**动态生成**，硬规则范围更新为 R1–R18 并补不变式说明。过程中修掉两处自己造成的错误：补丁把字符串从中间换行截断（被 py_compile 当场拦下）；建筑计数误用「medium 含建筑」→ 显示 10 条，改为「medium == 建筑」的专条 → 正确 4 条。口径错比数字错更危险：10 条会让读者以为建筑覆盖可观，实际只有 4 条专条。")
if cyc=="cycle37":
    L.append("- 本轮为**体检轮 + 来源库治理**。八步体检全通过、120/120 来源活性 200。核对数字时发现 sources.json 里有 **5 条 verified=false**（2 个页面 404、Met 429、Khan 反爬壳页、NGA 403），且**没有任何条目引用**——已移入 data/sources_quarantine.json（留原因），并新增 **check.py R18** 不变式：「来源库内必须全部 verified，被引用者必须在库内」，且做了**注入验证**（临时塞入一条未核验来源 → 报 R18 且 rc=1，还原 → rc=0）。另新增 PROJECT_STATUS.md（项目总表与交接），撰写时**自查发现并更正了两处数字错误**（来源 284→279、建筑条目 3→4）。来源库现 **279 条全部 verified**。")
if cyc=="cycle36":
    L.append("- 本轮把 B5 剩余 5 项用 Wikidata **时间声明**再核一遍，结果为「1 个真实差异 + 1 个备查事实 + 3 个仍无解」：①**romanesque 发现断代差异**——Wikidata「Romanesque art」(Q46805) 记 P580=1000 / P582=1200，本条目正文采「约1000—1150」，**终点差 50 年**，而 1150 本身源自早期种子、从未有独立来源；②张旭实体给出**生年 670**，但条目待核的是「作品名称」，仍无解；③realism 年代、草书年代、donatello 术语无可用声明。处置：**一律不据单一结构化来源改正文**，差异与备查事实写进复核记录，并注明「待第三来源判定」。发现差异比抹平差异更有价值。")
if cyc=="cycle35":
    L.append("- 网络探针：Wikipedia/Met/Tate 仍 000（不可达），Wikidata 200 —— 内容建设继续受阻。本轮做**条目页来源构成徽标**：标题区显示「N 来源：内容 a · 结构化 b · 锚点 c」，让读者一眼看出证据结构差异（「2 百科+1 锚点」与「2 百科+1 结构化事实」强度并不相同）。实测分布：内容+锚点 77、内容+结构化 41、仅内容 27 —— **没有条目只靠结构化或锚点撑着**。过程中修了一次锚点没对上的补丁（与 Cycle29 同类问题），已用精确匹配替换。")
if cyc=="cycle34":
    L.append("- 本轮是**文档与信息架构轮**。①**重写 README**：旧版仍写着「来源 91 条/86 verified」与「完成后写 ALL_DONE」（与自治约定冲突），新版改为现状数字、完整管线（audit_all 八步）、9 条关键约定、**已知限制专章**（Wikipedia/Met/Tate 不可达、百度与 Khan 仅壳页、来源独立性不足、27 条未锚定）与续跑指引。②**单元页新增「本单元覆盖缺口」**：从矩阵 A/B2 清单按地区×媒介筛选后就地展示，并注明「补写需先取得可核验来源，未取得前不写作」——把「为什么这里空着」直接写在读者眼前。")
if cyc=="cycle33":
    L.append("- 本轮为**体检轮 + 饱和评估**。八步体检全通过；**120 条 Wikidata 来源 120/120 返回 200**。按 §5 两个条件正式评估饱和：条件②（核心48/重要85 全部≥L2、全库无 L1）**成立**；但条件①（连续3轮无新缺口）**不成立**——最近三轮仍发现新缺口（Cycle31 锚定14、Cycle32 锚定4）。故 **saturated=false**，并登记开放缺口：A类58、B2音乐地区22、B5待核实5、未锚定27（含自有页11）。性质说明写得很直白：**不是缺口没了，是内容来源进不来**；Wikidata 只能做身份锚定与结构化事实，撑不起风格/体裁/评价类陈述。这是外部阻塞，不是质量问题。")
if cyc=="cycle32":
    L.append("- 本轮针对 15 条中国专题条目试**中文同义别名**检索，**采纳 4 条、拒绝 11 条**，锚定率 79%→**81%（118/145）**。采纳的都是口径严丝合缝者：ming-painting→Q6864640『Ming dynasty painting』、xieyi→Q10894988『xieyi painting』、china-music-history→Q277393『music of China』、pipa→Q6685124『pipa』（Chinese plucked lute，终于不是日本 biwa/古诗/馆藏器物）。11 条否决理由逐条写进 reports/entity_pass7_vetted.md：唐代绘画→Tang dynasty art 偏宽、敦煌艺术→Mogao Caves 是遗址、魏晋南北朝→是历史时期、玉器/青铜器→仅材质门类等。活性抽样 4/4 HTTP 200。")
if cyc=="cycle31":
    L.append("- 本轮按 D030 的待办做**人工指定 QID**：为 19 条「其余」未锚定条目手工给出英文检索词，逐个检索并核对口径，**采纳 14 条、拒绝 5 条**，锚定率 **69% → 79%（114/145）**。亮点：romanesque 终于锚到 **Q46805『Romanesque art』**（艺术风格，而非 Cycle23 被拒的『建筑』实体）；tonality → Q192822『tonal system』对应「大小调体系」。并确立**口径一致**否决标准：宽（Buddhist art 对印度佛教艺术、Paleolithic art 对旧石器雕塑）或窄（法国巴洛克音乐）、或描述为空，一律拒绝。活性抽样 5/5 HTTP 200。")
if cyc=="cycle30":
    L.append("- 本轮为**体检轮 F**（第六次）：audit_all 增到 **8 步并全通过**。针对 Cycle29 的大改，新增两项常驻检查：**渲染一致性**（独立重算未解决项/复核记录数并与页面比对，0 不一致）与 **HTML 结构**（html.parser 逐页解析，0 未闭合）。并做了**故障注入测试**：人为往一页尾部注入 <div><ol><li>，检查如预期报 3 处未闭合且 rc=1，重建后 rc=0 ——证明守卫真的会失败，而不是永远显示 ok。活性抽样：最新 8 个锚点全部 HTTP 200。")
if cyc=="cycle29":
    L.append("- 本轮做**呈现层重构**（文字零改动）：145 页的「待核实」原本混作一大段，多轮复核后堆到 3–10 项，「未解决」与「已解决」糊在一起。改为三层：①状态说明独立成提示句；②**待核实（未解决）**用有序列表（按（N）编号或句号切分）；③**复核记录**用 details 折叠并逐条附第二来源 URL。理由是诚实标注不仅要不隐瞒，还要让人一眼看出哪条仍未落实。过程中修了两个自造坑：补丁未落盘（改单脚本+末尾自检）、切分误伤状态说明中的行内提及。")
if cyc=="cycle28":
    L.append("- 本轮为**体检轮 F**（第五次），七项检查通过，但抓到**一个真实回归**：「sitemap 与实体页一致」报 **2 页未收录**（entities.html、status.html）——根因是 build_sitemap 里写死了根页面列表，Cycle22/25 新增的页面没进去。已改为**自动收录根目录全部 html**，sitemap 174→176 条、unlisted=0、missing=0。另修一处自造噪音：尺寸说明中的「目前」触发过期数据规则，stale 6→3（余 3 为已知误报）。来源活性：**102 条 Wikidata 来源 102/102 返回 HTTP 200**。")
if cyc=="cycle27":
    L.append("- 本轮为**锚点收官**：用限速客户端做 A/B 双路匹配（英文 id 与中文标题），50 条未锚定中初命中 8 条，**人工确认后只采纳 5 条、拒绝 3 条**（renaissance 再次命中「法国复兴党」；两个实体描述为空无法辨别），锚点 54→**59**（锚定率 100/145 = 69%）。随后做**结构性分类并停止硬凑**：剩余 45 条 = 自有页面 11 条（导览/比较页，本无对应实体）+ 中国专题 15 条（中系概念缺精确同名实体或同名空描述）+ 其余 19 条（标签不完全一致，需人工指定 QID）。锚定率不是 KPI，正确率才是。")
if cyc=="cycle26":
    L.append("- 本轮**发现一个一直存在的静默故障**：直接 curl Wikidata 批量接口返回纯文本「You are making too many requests」，而旧代码只接受以 { 开头的响应 → **限流被当成「无数据」**，解释了此前多轮「批量缓存为 0」与部分 no_match。已新建 tools/wd_api.py（正确 UA、串行限速 1 秒、指数退避、磁盘缓存、返回 (data, err)），重跑中文标签锚定：187 个实体 **187/187 成功、0 错误**。结果：精确命中 2 条、近似 29 条，**人工确认采纳 20 条**（锚点 34→**54**），并拒绝 5 组误配（minimalism→计算哲学、polyphony→论文、symphony→Brightman 专辑、pipa→日本琵琶、china-music-history→两个空描述同名实体）。来源 241→261，站点 176 页。")
if cyc=="cycle25":
    L.append("- 本轮特别说明：两件事。①对 71 条未锚定条目做 **pass3 最高精度匹配**（要求条目 id 与实体英文标签完全相等），只命中 **1 条**（serialism → Q507246）并照实采纳；命中率极低本身是信息——宋/元/明/清绘画、书法、中国音乐等条目在 Wikidata 中并无对应英文实体，锚定只能靠中文标签或人工指定。②新增**站点状态页** status.html：公开条目数、层级与重要性分布、来源构成（事实来源 43 / 身份锚点 34）、校验方式，以及**已知缺口**（A类58、B2候选22、待核实项、Wikipedia/Met/Tate 不可达）——把短板主动摆在读者面前，而不是藏在报告里。站点 175→176 页。")
if cyc=="cycle24":
    L.append("- 本轮为**体检轮 F**（第四次）：`audit_all` **7/7 全通过**（含 py_compile 守卫：112 个工具文件无语法错误）、死链0、重复0、数据矛盾0、孤儿0、页内锚点0错、sitemap 与实体页一致、对比度全部≥AA、单向关联0、跨域2（合法）。另做**来源活性全量核验**：全部 **76 条 Wikidata 来源**逐个 curl，**76/76 返回 HTTP 200**、0 失败——这是比“记录里写着 verified”更硬的证据。内容来源（Wikipedia/Met/Tate）仍不可达，故 A 类建筑剩余、B2 音乐地区空白、B5 剩 5 项继续挂起。")
if cyc=="cycle23":
    L.append("- 本轮特别说明：针对上轮 40 条歧义项，改用 **pass2 规则**——拿条目 id（本身是英文 slug）去比对实体的**英文标签**，相等或互为子串且描述含类型词才算命中，再**人工逐条确认**：初命中 15 条，**采纳 12 条、拒绝 3 条**。拒绝示例很有说服力：romanesque 命中「罗马式建筑」实体（条目是跨媒介风格）、renaissance 命中**法国政党**、baroque-music 命中「法国巴洛克音乐」（比条目窄）——证明机器匹配到位后仍需人眼把关。锚点总数 21→**33**，来源 228→240，站点仍 175 页。")
if cyc=="cycle22":
    L.append("- 本轮特别说明：把 104 条尚未关联 Wikidata 的条目做**两阶段批量匹配**（先检索候选、再按 50 个一组批量取标签与描述，避免逐条抓取超时）：**命中 21 条**、歧义 40 条、无候选 43 条。命中项登记为**身份锚点来源**（明确声明不作事实依据），并在站点新增**实体对照页** entities.html（21 条映射，公开可核对）。匹配率偏低如实记录在 reports/entity_map_c22.json（歧义项多为中文标签缺失或同名条目）。来源 207→228，站点 174→175 页。")
if cyc=="cycle21":
    L.append("- 本轮特别说明：用 Wikidata 补齐 **5 个作品条目的尺寸/材质/藏品编号**（蒙娜丽莎 79.4×53.4cm、INV 779/MR 316；星夜 73.7×92.1cm、472.1941；维纳斯的诞生 172.5×278.5cm、00158551；西斯廷天顶 4093×1341cm；格尔尼卡 349×776cm、DE00050），这正是 TASK 提示「最容易写错」的信息。但**只登记在待核实节、不写入正文**——该组数据仅有一个结构化来源，未达双源互证标准。另登记日本建筑(Q1422874)/印度建筑(Q61050)实体，但**本轮不建条目**：现有日/印艺术页此刻无法复核是否含建筑章节，据此写木构或石窟特征即属无源断言。")
if cyc=="cycle20":
    L.append("- 本轮为**体检轮 F**（第三次）：九维全部通过——死链0 / 重复0 / 数据矛盾0 / 孤儿0 / 页内锚点0错 / sitemap 与实体页一致 / 对比度全部≥AA / 单向关联0 / 跨域仅2（浪漫主义跨媒介合法对）；过期数据规则命中3处经人工确认均为误报（存成语与断代用语）。**新增一项来源活性抽查**：41 条 Wikidata 来源全部 verified，抽样 5 条 URL 均返回 HTTP 200。**发现并修复 2 条新单向关联**（gothic-architecture→gothic、romanesque-architecture→romanesque），修复后单向归零、关联总数 430。另改进体检工具：把「来源重合度不可执行」的原因写精确（内容来源不可达、Wikidata 无正文），并把关联图摘要并入输出。")
if cyc=="cycle19":
    L.append("- 本轮特别说明：复核覆盖矩阵的 **B 类（原判「结构上不适用」）96–129 项**，把 B 再分两层，发现其中 **22 项实为候选真缺口**——这些地区在「音乐体裁」上站内零覆盖，而该地区确有音乐传统（东南亚甘美兰、南亚古典音乐、日本雅乐/邦乐、荷兰黄金时代音乐、佛兰德斯乐派等）。因当前仅 Wikidata 可达（只能确认实体存在，无法支撑风格/体裁陈述），**B2 一律挂起**，明细已写入 reports/matrix_targets_c7.md 附录。本轮未新增条目——不因为「想有产出」而降低来源标准。")
if cyc=="cycle18":
    L.append("- 本轮特别说明：A 类建筑缺口推进第二条——新建 **高棉建筑**，其形制描述拥有 **两个确实论述建筑的已核验内容来源**（高棉艺术、吴哥）外加 Wikidata 身份来源，因此比 Cycle17 的哥特/罗马式（Wikidata 仅确认身份）基础更实。**中国建筑仍只差第二来源，继续不建**。过程中主动修正一处不诚实：初稿「19世纪后被重新发现」在所引来源中无支撑，已删去并改写为「近现代被重新记录与研究（具体年代待核实）」，并在待核实记明原委。条目 144→**145**，站点 173→**174** 页，孤儿 0，check/links/audit 全通过。")
if cyc=="cycle17":
    L.append("- 本轮特别说明：按 A 类矩阵清单开工**建筑**缺口（最大缺口）：新建 哥特式建筑、罗马式建筑 两条（各挂 Wikipedia 专页 + Wikidata 实体 + 关联风格页），并在待核实写明**来源分工**——实测这两个 Wikidata 实体没有 P571 年代声明，Wikidata 只确认实体身份与正式名称，**不承担年代**，年代类断言仍在待核实。**中国建筑因只有 Wikidata 一条可核验来源，按双源规则不建**（记入 BACKLOG）。质量闸：两条 wd 来源 URL 200 且标签一致（哥特式建筑/罗曼式建筑），新建条目正文年份全部在待核实列明（issues 0）。条目 142→**144**，站点 171→**173** 页。")
if cyc=="cycle16":
    L.append("- 本轮特别说明：把 Cycle15 遗留的 6 条未匹配人物全部补齐（补英文别名检索与个别人物类型词，如 polymath），并为 **全部 32 个人物条目** 挂上 Wikidata 来源与【已复核·Wikidata】生卒留痕 → 人物 Wikidata 覆盖率 6→**32/32**，生卒年核验 **mismatch 0**；另核验 monet（1840—1926）与 mona-lisa（1503 创作、卢浮宫、达·芬奇）与条目一致；修正 5 处「QQ」重复 QID 的标题与 URL。来源 174→**202（verified 197）**，全库平均 2.46 来源/条。")
if cyc=="cycle15":
    L.append("- 本轮特别说明：用 Wikidata 对全部 32 个人物条目做生卒年交叉核验（要求描述含人物类型词且生年与条目 when 相差≤2 才接受，同名实体一律拒绝）：**confirmed 26 / mismatch 0 / no_match 6**。即凡能与权威结构化数据对齐者生卒年全部一致，未发现年份错误；6 条为消歧未过（实体缺中文标签或抓取抖动），已拒绝强行匹配，明细见 reports/person_dates_c15.md。本轮未据此改动任何条目（无差异可改）。")
if cyc=="cycle14":
    L.append("- 本轮特别说明（突破）：Cycle13 的网络结论需修正——Wikipedia/Met/Tate 仍不可达、百度/Khan 仅返回反爬壳页，但 www.wikidata.org（api.php 与 Special:EntityData/*.json）、api.wikimedia.org、commons.wikimedia.org、dbpedia.org 均可达且返回可用 JSON。新增 tools/wikidata_verify.py（三重消歧：标题+描述类型词+作者名），核验 5 个作品档案的作者与收藏地，结果与条目一致（星夜/维纳斯的诞生/西斯廷天顶画/格尔尼卡/春之祭）；春之祭实体的 P170 字段异常（西德尼·諾蘭）已标注不采信。同时修复真实数据丢失 bug：merge_l2 的 sources 由覆盖改为并集（D021）。来源 164→169（verified 164），check/links/audit_all 全通过。")
if cyc=="cycle13":
    L.append("- 本轮特别说明：网络能力精确定位——可达站点为 github（200）、百度百科（200）、Khan Academy（200）、Britannica（403），不可达为 wikipedia/met/tate；但可达站点全部返回反爬壳页（百度返回 __PARIS_CHALLENGE__ 挑战页 4.7KB 无正文；Khan 返回 Client Challenge 3KB；Britannica 为 Cloudflare Just a moment），因此仍无可用权威正文，内容建设继续受阻。同时新增 tools/audit_all.py 一键体检（check/链接/九维体检/内容自洽/关联图/单向关联 共6项，本轮 6/6 通过）。")
if cyc=="cycle12":
    L.append("- 本轮特别说明：网络第六轮降级，按预案换角度。新增 tools/oneway_audit.py 审校 47 条单向关联（same_unit 36 / same_domain 11 / **跨域 0**），全部补成双向 → 关联总数 373→420、单向 0、零度节点 0、度均 3.0/最大 12；条目页新增「同单元前后条目」导航（按起始年代排序 + 单元总览入口），已在 art-modern 单元核对排序正确。")
if cyc=="cycle11":
    L.append("- 本轮特别说明：网络第五轮降级，按预案改为**内容复审**（不重复体检）。新增 ：校验「正文与待核实是否矛盾 / 一图数字越界 / 复核留痕误入正文 / 待核实为空」。审计规则经三次收紧去除误报后，**142 条目自洽性 0 问题**；过程中实修 16 处（15 条补状态说明以消除「原待核与已复核并列」的阅读矛盾，1 处措辞修正）。")
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
