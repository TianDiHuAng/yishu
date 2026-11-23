# -*- coding: utf-8 -*-
"""Cycle59 收尾：D063 + METRICS/SATURATION/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D063 — Cycle59 再补 4 条（204 → 208）：非洲 11 → 15；两条项链「无尺寸」如实处理
- **决定**：新增 `ethiopian-amulet-necklace`（银护符项链）、`ethiopian-harar-necklace`（muriya 新娘项链）、`kongo-nkisi-nkondi`（灵力像）、`kongo-corpus`（刚果基督像）。
- **四处必须原样保留的内容**：
  1. **nkisi 的「去力量」**：该馆说明这件灵力像**已失去大部分赋灵材料**；原因有两解——仪式用途终结后由 ng祭司取走，**或刚果人在欧洲人夺取前作为反殖民抵抗**而自行解除其灵力。该馆明言「**我们不知道为什么它被去力量**」，并称此雕刻**如今不再具有灵力**。条目把不确定与反殖民可能性一并保留，不择一。
  2. **埃及以外的跨信仰工艺**：银护符（tälsäm）的护符逻辑与**伊斯兰实践**相关，而同类镂空/珠化工艺同时见于**正教**圣城阿克苏姆——**工艺与信仰并非一一对应**。
  3. **性别分工**：Harar 项链由**男性银匠**制作、**顾客通常为女性**；条目照录，不把它简化为「女性工艺」。
  4. **两种基督转译**：与既有 `kongo-crucifix`（本地发辫）并置，`kongo-corpus` 以**几何化形式**转译受难图像——同过程的两条路径，均非复制。
- **「无尺寸」的处理**：两条埃塞俄比亚项链的馆藏记录**没有 measurements 字段**（API 返回 None），条目**不写尺寸**，并在技法节与待核实明确「该记录未给出尺寸」。这是对「记录有什么就写什么」的严格执行，不据经验补数。
- **可逆方式**：删 4 条 overlay 与 catalog 元组、移除 4 条来源，重跑 `build_scope.py`。
- **代价**：4 条均单机构（`needs_verification`）；非洲由 11 升至 **15** 条，仍集中于西非/中非/东非少数族群，撒哈拉以南其他地区仍空白。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle59","date":"2026-11-23","status":"completed",
 "gap_methods":["非洲区深度推进"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["ethiopian-amulet-necklace","ethiopian-harar-necklace","kongo-nkisi-nkondi","kongo-corpus"],
 "must_state":["nkisi 去力量的两种解释（含反殖民抵抗）","护符的跨信仰工艺","银匠性别分工","两种基督转译路径"],
 "no_dimension_records":["cma-2025-152","cma-2025-155"],
 "africa_entries":15,"new_sources":4,"sources_total":339,"entries_total":208,"pages":243,
 "check_result":"errors=0","check_links_result":"broken=0(243页)","audit_all":"10/10 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle59","date":"2026-11-23","methods_used":["非洲区推进"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)",
 "verdict":"非洲 11→15（总 208）；nkisi 去力量与跨信仰工艺入正文；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle59"' not in t:
    block=('if cyc=="cycle59":\n'
           '    L.append("- 非洲区再推进，新增 **4 条（204 → 208）**，非洲 **11 → 15**：埃塞俄比亚银护符项链与 Harar 新娘项链、'
           '刚果 nkisi nkondi 灵力像与刚果基督像。四处内容原样保留：①**nkisi 的「去力量」**——该馆明言「**我们不知道为什么它被去力量**」，'
           '两种可能是仪式用途终结后祭司取走，**或刚果人在欧洲人夺取前作为反殖民抵抗自行解除**，条目把不确定与反殖民可能一并保留；'
           '②护符逻辑属**伊斯兰**实践，而同类镂空/珠化工艺同见于**正教**圣城阿克苏姆——**工艺与信仰并非一一对应**；'
           '③Harar 项链由**男性银匠**制作、**顾客多为女性**，不简化为「女性工艺」；④与本地发辫的木十字架并置，'
           '`kongo-corpus` 以**几何化形式**转译受难图像——两种转译路径，均非复制。'
           '另：两条项链的馆藏记录**无 measurements 字段**，条目**不写尺寸**并明确说明——「记录有什么就写什么」。站点 239 → 243 页。")\n')
    anchor='if cyc=="cycle58":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 204（L2 200 / L3 4 / L1 0） |","| 条目 | 208（L2 204 / L3 4 / L1 0） |"),
    ("| 来源 | 335（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | 339（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | 239，站内断链 **0** |","| 页面 | 243，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **204** | L2 200 / L3 4 / **L1 0** |","| 条目总数 | **208** | L2 204 / L3 4 / **L1 0** |"),
    ("| 来源库 | **335**（另 11 条预备来源未计入） |","| 来源库 | **339**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **239** |","| 站点页面 | **243** |")])]:
    s2=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in s2: s2=s2.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(s2)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])