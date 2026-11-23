# -*- coding: utf-8 -*-
"""Cycle80 收尾：D084（印度绘画 4 条 + R22 + id 事故）+ METRICS/REPORT/PROGRESS/STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D084 — Cycle80 印度绘画 4 条（264 → 268）＋ R22 id 格式硬规则（点号 id 第三次复发）
- **决定（内容）**：新增 `shri-raga-mewar`（《室利拉格》Ragamala，梅瓦尔，c.1695，**核心**）、`sursagar-krishna`（《黑天诞生》，1705—10，**核心**）、`jagat-singh-hunting`（狩猎图，1747）、`kausa-ragaputra`（帕哈里 Ragamala，c.1750）。
- **四处要点**：
  1. **Ragamala＝「旋律花环」**：该组画表现「**听者听相应音乐时的感受**」；`kausa-ragaputra` 之名**同时也是印度古典音乐的一种调式**——绘画与音乐在此结构性对应（正合本站艺＋音的范围）。
  2. **赞助人入画**：`shri-raga-mewar` 的原型王者被**阿马尔·辛格二世以其本人肖像替换**；该组画亦标志梅瓦尔宫廷绘画**引入莫卧儿要素**（穹顶建筑、纵深）**而保留水平分栏**。
  3. **名与色**：`sursagar-krishna` 中黑天「**因肤色深而得名，故画为蓝**」——解释了蓝肤神像的直接来由。
  4. **围猎的程序**：`jagat-singh-hunting` 中仆役**施放爆竹**驱兽至中央射台；**背面题记列出参与者（含大君兄弟）**——文字与图像互为索引。
- **【工程】点号 id 第三次复发，故立 R22**：
  - 复发记录：`cma-1921.914`（Cycle70）、`cma-1998.102`（本轮）、`cma-1972.9`（本轮）。
  - **R22**：条目 id 与来源 id 必须匹配 `^[a-z0-9-]+$`（禁点号、大写、下划线）。**注入测试**：塞一个 `cma-1972.9` → 同时报 R22 与 R18，还原后 0 错误。
  - **另记一处我自己的失误**：用 `re.sub(r'\\.(\\d+)$','-\\1', ...)` 批量规范化时，`\\1` 在 shell 传参链条里被当成**八进制转义**，把 id 改成了含 `\\x01` 控制字符的 `cma-1972-\\x01`；已用脚本显式修复。**教训**：批量正则改写 id 这类主键操作，必须落盘为脚本并**逐个打印改动**，不在命令行拼接。
- **可逆方式**：删 4 条 overlay 与 catalog 元组、移除 4 条来源；R22 可移除。
- **代价**：4 条均单机构；印度绘画 4 条（拉杰普特/帕哈里/梅瓦尔），**莫卧儿宫廷细密画与德干画派仍有候选未用**。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle80","date":"2026-11-23","status":"completed",
 "gap_methods":["印度绘画填补","id 格式治理"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["shri-raga-mewar","sursagar-krishna","jagat-singh-hunting","kausa-ragaputra"],
 "indian_paintings":4,"new_rule":"R22 id 格式（^[a-z0-9-]+$），注入测试通过",
 "incidents":["点号 id 第三次复发（cma-1998.102 / cma-1972.9）",
   "批量正则改写 id 时 \\1 被当八进制转义，产生 \\x01 控制字符，已脚本修复"],
 "checks_r":22,"new_sources":4,"sources_total":399,"entries_total":268,"pages":305,
 "check_result":"errors=0","check_links_result":"broken=0(305页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle80","date":"2026-11-23","methods_used":["印度绘画","id 治理"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)",
 "verdict":"印度绘画 0→4（总 268）；R22 立规；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle80"' not in t:
    block=('if cyc=="cycle80":\n'
           '    L.append("- **印度绘画几乎空白**，本轮补 4 条（264 → 268）：《室利拉格》（梅瓦尔 Ragamala, c.1695）、'
           '《黑天诞生》（1705—10）、《贾加特·辛格二世狩猎图》（1747）、帕哈里《考萨拉格普特拉》（c.1750）。'
           '四处要点：①**Ragamala＝「旋律花环」**，组画表现「听者听相应音乐时的感受」，而 `kausa-ragaputra` 之名'
           '**同时也是印度古典音乐的一种调式**——绘画与音乐结构性对应；②`shri-raga-mewar` 的原型王者被**赞助人阿马尔·辛格二世'
           '以其本人肖像替换**，该组画引入**莫卧儿穹顶与纵深**却**保留水平分栏**；③黑天「**因肤色深而得名，故画为蓝**」；'
           '④围猎图中仆役**放爆竹驱兽至中央射台**，**背面题记列出参与者**。'
           '**【工程】点号 id 第三次复发**，故立 **R22**（id 须匹配 `^[a-z0-9-]+$`），注入测试通过；'
           '并记录我自己的一处失误：批量正则改写 id 时 `\\\\1` 被当八进制转义，产生控制字符，已脚本修复——'
           '**主键类批量改写必须落盘为脚本并逐条打印**。站点 301 → 305 页，体检 12/12，硬规则增至 R1–R22。")\n')
    anchor='if cyc=="cycle79":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 264（L2 260 / L3 4 / L1 0） |","| 条目 | 268（L2 264 / L3 4 / L1 0） |"),
    ("| 来源 | 395（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | 399（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | 301，站内断链 **0** |","| 页面 | 305，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **264** | L2 260 / L3 4 / **L1 0** |","| 条目总数 | **268** | L2 264 / L3 4 / **L1 0** |"),
    ("| 来源库 | **395**（另 11 条预备来源未计入） |","| 来源库 | **399**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **301** |","| 站点页面 | **305** |")])]:
    s2=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in s2: s2=s2.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(s2)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])