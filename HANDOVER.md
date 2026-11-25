# 交接文档：艺术史与音乐史导读

> 截至 2026-11-25（cycle240）。在线地址：https://tiandihuang.github.io/yishu/

## 1. 项目是什么

一个数据驱动的静态知识库，覆盖西方艺术史、中国书画、西方音乐史、中国音乐史和摄影。它的特点：

- 零 JavaScript，可以离线阅读。
- 所有图示都是自绘的内联 SVG，不含任何作品图片、乐谱或歌词。
- 遵守“不编造”原则：来源没给的内容一律写“待核实”，不补写。

## 2. 当前规模

| 指标 | 数值 |
|---|---|
| 条目 | 918（L2 895 / L3 23） |
| 知识单元 | 28 |
| 来源 | 1699（全部 verified） |
| 站点页面 | 955 |
| 双源校验通过 | 195 / 918 |
| 标记待核实 | 723 |
| check.py / check_links.py | errors=0 / broken=0 |

## 3. 目录与数据流

```
tools/catalog.py        条目基础字段（单一事实源；带注释的多行元组列表）
data/sources.json       来源库
data/l2/<id>.json       各条目 L2/L3 正文覆盖层（sections、svg、sources、l3）
        │
tools/build_scope.py → scope.md / data/coverage.json / data/entries.json（related 对称化、悬空检查）
tools/merge_l2.py    → data/site_entries.json
tools/check.py       → 硬规则 R1–R22 校验
tools/gen_site.py    → index.html、entries/*.html、各索引页、sitemap.xml
tools/check_links.py → 全站断链检查
```

每一轮的标准流程如下，任何一步报错都不提交：

```bash
python tools/<本轮脚本>.py add
python tools/build_scope.py
python tools/<本轮脚本>.py write
python tools/merge_l2.py && python tools/check.py && python tools/gen_site.py && python tools/check_links.py
# 然后在 METRICS.json 追加一轮记录，在 DECISIONS.md 追加 Dxxx，再 git commit
```

## 4. 必须遵守的规则

1. **单一事实源**：基础字段（title、when、def、overview、related、sources）只能改 `catalog.py`。覆盖层不得携带这些字段，否则触发 R20。
2. **改 catalog 要按行定位**。字符串全局替换出过两次事故（D051、D229），所以修改前要断言目标串只出现一次，改完再看 diff。
3. **R2：`when` 必须含年代数字**。来源没有年代时，写“约 X 世纪起（本项目划分）”，并在正文注明是本项目的划分。
4. **只转述来源**。评价性说法（“最伟大”“最著名”）要标“评价性表述未核验”。来源之间不一致时，各说并列，不做裁决，也不改正文。
5. **L3 门槛**：只收核心条目，并且要有学界两方，双方都写明论者和依据。只有“仍有争论”一句话，或只是当年的风波，都不升级。
6. **GND id 末尾的校验位 X 一律小写**，否则触发 R22。

## 5. 外部来源（实测状态，2026-11-25）

| 来源 | 状态 | 用途 |
|---|---|---|
| Wikipedia REST summary / 中文维基 API | 可用 | 主内容来源（同源，独立性有限） |
| Wikidata | 可用 | QID、生卒 |
| GND（lobid.org） | 可用 | 人物第二来源，只按 sameAs 里的 QID 匹配 |
| MusicBrainz | 可用（请求间隔 ≥1 秒） | 音乐人物第二来源，按 Wikidata URL 反查 |
| Getty AAT SPARQL | 可用，偶尔返回 403，重试即可 | 风格与术语定义；很少收音乐体裁和中国术语 |
| 克利夫兰美术馆 Open Access | 可用 | 藏品记录 |
| 史密森尼 api.si.edu | 目前只用 DEMO_KEY | 图书馆人名标目；正式使用需申请 api.data.gov 密钥 |
| 大都会、芝加哥、哈佛博物馆 | 410 / 403 / 401 | 暂不可用（见 BLOCKERS.md） |

## 6. 遗留问题与建议的下一步

1. **待核实比例高（723/918）。** 新增条目大多只有百科一个来源，而 GND、MusicBrainz、AAT 只能印证生卒、身份或定义，撤不掉标记。真正降下来需要专门文献，例如 Grove 音乐辞典、故宫或台北故宫的研究文章。
2. **缺失的书画大家**：欧阳询、怀素、张旭、王献之、董源、李成、李唐、徐渭、吴镇。史密森尼标目已经给出年代（见 D235），但还没有能写正文的来源。
3. **生卒不一致待核定**：顾恺之、礼萨·阿巴西、范宽、夏圭（见 D232、D234、D235）。
4. **教材术语表的剩余缺口**：和声、节奏、力度、打击乐、即兴、音乐剧、反宗教改革（见 D239）。
5. **申请 api.data.gov 密钥后**，可以检索弗利尔美术馆的中国书画藏品。

## 7. 本次会话（cycle219—240）做了什么

- L3 深度：19 → 23 条，新增若斯坎、波洛克、乔托、威尔第、扬·凡·艾克、肖斯塔科维奇。
- 补缺口：新增 126 条，覆盖音乐（古典、中世纪、文艺复兴、教材术语）、中国书画与音乐、摄影、建筑、人物与时期概述。
- 第二来源：GND 38 人，MusicBrainz 45 人，AAT 7 个术语，史密森尼 4 人。
- 借鉴外部资源：对照开放教材 *Understanding Music: Past and Present*（CC BY-SA）的术语表找缺口。

逐轮的详细决策见 `DECISIONS.md` 里 D221—D240 各条。
