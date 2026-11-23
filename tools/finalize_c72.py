# -*- coding: utf-8 -*-
"""Cycle72 收尾：D076 + METRICS/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D076 — Cycle72 伊斯兰再补 4 条（236 → 240；伊斯兰 9 → 13）
- **决定**：新增 `khurasan-ewer`（呼罗珊多棱执壶，1300—1350，44.8cm）、`seljuq-bird-vessel`（鸟形水器，1100s，17.5×9.5cm）、`sultanabad-bowl`（飞鸟纹碗，1280—1400，11.2×22cm）、`safavid-steel-plaque`（钢制镂空铭文板，约1693，27×35cm）。
- **四处内容要点**：
  1. **「人首铭文只见于金属器」**：执壶下缘一圈铭文**带人首**，该馆明言这类人首**只出现在伊斯兰艺术的金属器上**——金属工艺的专属母题，条目照录其表述范围。
  2. **鸟形器是「会倒水的鸟」**：或为净手用 **aquamanile**；水自**胸前孔**注入、由**可动喙**倒出；鸟的象征有两层（信使／保护者；精神自由），蓝绿眼珠**可能**辟邪——三说并列。
  3. **外来母题被「翻译」而非照搬**：伊儿汗期引入中国**龙、凤、莲**；**莲花**易并入伊斯兰花卉传统，**凤凰**则被等同《列王纪》**西摩格**；平口沿受中国器形影响，器物外销自**中亚至埃及**。
  4. **材料决定形式上限**：萨法维钢板因**钢材抗拉强度与耐久**，才可能做出极繁**镂空**门饰；「曾属苏莱曼二世陵」该馆用 **is said to**，条目注明为传闻。
- **可逆方式**：删 4 条 overlay 与 catalog 元组、移除 4 条来源，重跑 `build_scope.py`。
- **代价**：4 条均单机构；伊斯兰 13 条已覆盖陶（伊兹尼克/卡尚）、金属（嵌银/青铜/钢），但**建筑与手抄本插图**仍缺。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle72","date":"2026-11-23","status":"completed",
 "gap_methods":["伊斯兰单元续深"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["khurasan-ewer","seljuq-bird-vessel","sultanabad-bowl","safavid-steel-plaque"],
 "islamic_total":13,
 "must_state":["人首铭文为金属器专属","鸟形器水路与三重解释","中国母题被翻译（凤凰=西摩格）","钢材决定镂空上限；陵墓归属为传闻"],
 "new_sources":4,"sources_total":371,"entries_total":240,"pages":276,
 "check_result":"errors=0","check_links_result":"broken=0(276页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle72","date":"2026-11-23","methods_used":["伊斯兰续深"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)",
 "verdict":"伊斯兰 9→13（总 240）；母题转译与材料—形式关系入正文；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle72"' not in t:
    block=('if cyc=="cycle72":\n'
           '    L.append("- 伊斯兰续深 **9 → 13 条（总 236 → 240）**：呼罗珊多棱执壶、塞尔柱鸟形水器、苏丹纳巴德飞鸟纹碗、'
           '萨法维钢制镂空铭文板。四处要点：①执壶下缘铭文**带人首**，该馆明言这类人首**只出现在伊斯兰金属器上**；'
           '②鸟形器是「会倒水的鸟」——水自**胸孔**入、由**可动喙**出，或为净手用 aquamanile，鸟的象征**两层并列**、'
           '蓝绿眼珠**可能**辟邪；③伊儿汗期引入中国**龙/凤/莲**，但**莲花并入既有花卉传统、凤凰被等同《列王纪》西摩格**'
           '——外来母题被**翻译而非照搬**，器物外销自中亚至埃及；④萨法维钢板因**钢材抗拉与耐久**才可能极繁镂空，'
           '「曾属苏莱曼二世陵」该馆用 **is said to**，条目注明为**传闻**。站点 272 → 276 页，体检 12/12。")\n')
    anchor='if cyc=="cycle71":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 236（L2 232 / L3 4 / L1 0） |","| 条目 | 240（L2 236 / L3 4 / L1 0） |"),
    ("| 来源 | 367（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | 371（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | 272，站内断链 **0** |","| 页面 | 276，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **236** | L2 232 / L3 4 / **L1 0** |","| 条目总数 | **240** | L2 236 / L3 4 / **L1 0** |"),
    ("| 来源库 | **367**（另 11 条预备来源未计入） |","| 来源库 | **371**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **272** |","| 站点页面 | **276** |")])]:
    s2=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in s2: s2=s2.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(s2)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])