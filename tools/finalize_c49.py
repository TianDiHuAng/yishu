# -*- coding: utf-8 -*-
"""Cycle49 收尾：标签更新（R1–R19）+ D052 + METRICS/SATURATION/REPORT/PROGRESS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 标签
A=os.path.join(ROOT,"tools","audit_all.py"); a=io.open(A,encoding="utf-8").read()
a=a.replace("check.py（R1-R17 硬规则）","check.py（R1-R19 硬规则）")
io.open(A,"w",encoding="utf-8").write(a)

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D052 — Cycle49 找到「单向关联」的真凶：merge_l2 用 update() 覆盖 related（与 D021 的 sources 同型）
- **事实**：上轮我在 `build_scope.py` 里加了 related 对称化，`data/entries.json` **确实对称**；但 `oneway_audit` 仍报 **16 条**单向。逐条比对发现：`data/site_entries.json` 里 `impressionism` **没有** `degas`，而 `entries.json` 里有。
- **根因**：`merge_l2.py` 对每个条目执行 `merged[eid].update(ov)`，而 **63 个覆盖层都带 `related` 字段**——整段覆盖了底层的 related，把对称化结果与基础关联一并抹掉。**这正是 D021 修过的 sources 覆盖 bug 的同型复发**，只是换了个字段。
- **修复（三处）**：
  1. `merge_l2.py`：合并前记 `base_rel`，合并后 **related 取并集**（与 sources 并集同构）；
  2. `merge_l2.py`：合并完成、写出 `site_entries.json` 之前，**再跑一次 `_symmetrize`**，保证输出文件本身对称；
  3. `check.py` **新增 R19**：related 不得悬空、且必须双向 —— 任何一次漏补反向，构建直接失败。
- **验证**：`oneway_audit` 由 **16 → 0**（历史：Cycle12 曾 47 → 0，后因字段覆盖复发到 16）；R19 做**注入测试**：手动删掉 `impressionism → degas` 一条反向，check 立即报 `[R19] degas: 单向关联`，还原后恢复 0 错误。
- **附带修正**：上轮我把贝宁两件器物错连到 `islamic-art`（内容错误），已改为只连 `african-art` 与彼此。
- **可逆方式**：还原 merge_l2 合并逻辑并移除 R19。
- **代价**：R19 使"单向关联"从提示变为硬约束；今后新增关联必须在 catalog 中只写一侧，另一侧由构建自动补。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle49","date":"2026-11-23","status":"completed",
 "gap_methods":["根因排查（单向关联复发）"],"network":"partial",
 "new_entries":0,"fixes":3,
 "root_cause":"merge_l2 的 update() 覆盖 related（63 个 overlay 带该字段）——与 D021 sources 覆盖 bug 同型",
 "fixes_detail":["merge_l2 related 取并集","site_entries 写出前再对称化","check.py 新增 R19 对称性硬约束"],
 "oneway_before":16,"oneway_after":0,"guard_test":"注入删除反向 → R19 报错；还原 → 0 错误",
 "content_fix":"贝宁两件器物误连 islamic-art → 改为 african-art",
 "entries_total":180,"sources_total":322,"pages":215,
 "check_result":"errors=0","check_links_result":"broken=0(215页)","audit_all":"8/8 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle49","date":"2026-11-23","methods_used":["根因排查"],
 "gaps_found":{"bug":"related 被覆盖"},"network":"partial",
 "verdict":"修复字段覆盖复发的同类 bug；单向关联 16→0；新增 R19 硬约束；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle49"' not in t:
    block=('if cyc=="cycle49":\n'
           '    L.append("- **找到「单向关联」的真凶**：上轮加的对称化只作用于 `entries.json`，而 `merge_l2` 对每条执行 `update(ov)`，'
           '**63 个覆盖层都带 related 字段**，整段覆盖后把对称结果抹掉——`entries.json` 对称、`site_entries.json` 不对称，'
           '所以 oneway_audit 仍报 16 条。这是 **D021 修过的 sources 覆盖 bug 的同型复发**，只换了字段。'
           '修复三处：merge_l2 的 related **取并集**、写出前**再对称化**、check.py **新增 R19**（悬空或单向即构建失败）。'
           '结果 oneway **16 → 0**；R19 做注入测试（删一条反向 → 立即报错，还原 → 0 错误）。'
           '附带修正上轮把贝宁器物误连 islamic-art 的内容错误。")\n')
    anchor='if cyc=="cycle48":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

BK=os.path.join(ROOT,"BACKLOG.md"); b=io.open(BK,encoding="utf-8").read()
b=b.replace("### P1 【安全机制】为 3 条新单元导览补**反向关联**（器物→导览）：不得再用正则改 catalog 文本；\n        建议在 build_scope.py 中加一步「related 对称化」（读 entries() 后双向补全，再写 entries.json）。",
 "### P1 【已完成 Cycle49】related 对称化已进构建流程（build_scope + merge_l2 双向补全，并有 R19 硬约束）。")
io.open(BK,"w",encoding="utf-8").write(b)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])