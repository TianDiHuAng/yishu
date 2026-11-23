# -*- coding: utf-8 -*-
"""Cycle48 收尾：D051（含失败记录）+ METRICS/SATURATION/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D051 — Cycle48 三个新单元补导览条目（177 → 180）；并记录一次失败的"文本手术"式关系编辑
- **决定**：为 `art-africa` / `art-americas` / `art-oceania` 各补一条**导览条目**（做法同 `islamic-art`）：
  不写通史，只把现有两件藏品当「可核验节点」，并在正文中**明说该区块其余部分仍空**（约鲁巴/库巴/阿坎、安第斯/北美原住民、密克罗尼西亚/夏威夷/复活节岛）。条目 177 → **180**。
- **失败记录（重要，供后人避坑）**：我原想同时把器物条目的 `related` 反向指向新导览，采用「按行定位 + 字符串替换」的**文本手术**方式，结果**两次改错**：
  1. 第一次匹配到**元组首行的 id 字符串**，把 `('maya-el-peru-stela',` 改成了 `('maya-el-peru-stela,americas-art',`，导致 4 个条目的 id 被污染、`entries()` 里查不到；
  2. 第二次以为「sources 行的上一行就是 related」，但定位失败时 `rel_idx=start-1` 落到了**上一个元组的 sources 行**，把 `'cma-1938-6'` 改成 `'cma-1938-6,americas-art'`。
- **处置**：`git checkout -- tools/catalog.py` **整文件回退**到上次提交（177 条），再只做「追加 3 个元组」这一件安全的操作；`build_scope.py` 重新生成后 `check.py errors=0`、八步体检 8/8。
- **教训**：`catalog.py` 是**带注释的多行元组列表**，用正则按行改字段风险极高。正确做法是**改数据模型**（例如给 `entries()` 加一步对称化处理），而不是手改文本。已把「反向关联补全」记入 BACKLOG，留待用安全机制完成。
- **代价**：三个新单元的导览条目目前**只有单向关联**（导览→器物），器物页不指引导览；`oneway_audit` 仅作提示、不影响体检通过。
- **可逆方式**：删 3 条导览 overlay 与 catalog 元组，重跑 `build_scope.py`。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle48","date":"2026-11-23","status":"completed",
 "gap_methods":["单元对称性补全（导览条目）"],"network":"partial: museum APIs ok",
 "new_entries":3,"new_entry_ids":["african-art","americas-art","oceania-art"],
 "entries_total":180,"sources_total":322,"pages":215,"units_total":26,
 "incident":"文本手术式关系编辑两次改错（污染 id 与 sources），已 git checkout 回退并改为仅追加元组",
 "known_gap":"3 条导览仅单向关联（导览→器物），反向关联待用安全机制补",
 "check_result":"errors=0","check_links_result":"broken=0(215页)","audit_all":"8/8 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle48","date":"2026-11-23","methods_used":["单元对称性"],
 "gaps_found":{"entries":3},"network":"partial (museum APIs)",
 "verdict":"3 单元各补导览（180）；一次关系编辑事故已回退并记录；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle48"' not in t:
    block=('if cyc=="cycle48":\n'
           '    L.append("- 为三个新单元补**导览条目**（177 → **180**），写法同伊斯兰艺术：不写通史，只把现有藏品当可核验节点，'
           '并在正文**明说区块其余部分仍空**（约鲁巴/库巴/阿坎、安第斯/北美原住民、密克罗尼西亚/夏威夷/复活节岛）。'
           '本轮同时记录一次**失败**：想让器物反向指引导览，采用「按行定位+字符串替换」的文本手术，结果两次改错'
           '（先污染了元组 id，后误改了上一元组的 sources 行）。处置是 `git checkout` 整文件回退后**只做安全的追加**，'
           '重建后 check 0 错误、体检 8/8。教训已写入 D051：catalog.py 是带注释的多行元组列表，'
           '应改数据模型而非手改文本；反向关联的补全留待安全机制。站点 212 → 215 页。")\n')
    anchor='if cyc=="cycle47":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 177（L2 171 / L3 6 / L1 0） |","| 条目 | 180（L2 174 / L3 6 / L1 0） |"),
    ("| 页面 | 212，站内断链 **0** |","| 页面 | 215，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **177** | L2 171 / L3 6 / **L1 0** |","| 条目总数 | **180** | L2 174 / L3 6 / **L1 0** |"),
    ("| 站点页面 | **212** |","| 站点页面 | **215** |")])]:
    s2=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in s2: s2=s2.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(s2)

BK=os.path.join(ROOT,"BACKLOG.md"); b=io.open(BK,encoding="utf-8").read()
b+="""
## Cycle48 待办追加
### P1 【安全机制】为 3 条新单元导览补**反向关联**（器物→导览）：不得再用正则改 catalog 文本；
        建议在 build_scope.py 中加一步「related 对称化」（读 entries() 后双向补全，再写 entries.json）。
### P2 三张新单元的深度：非洲仅贝宁、美洲仅玛雅/阿兹特克、大洋洲仅毛利/阿斯马特
### P3 朝鲜/东南亚陶瓷、安第斯（莫切/纳西卡/印加）仍零覆盖
"""
io.open(BK,"w",encoding="utf-8").write(b)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])