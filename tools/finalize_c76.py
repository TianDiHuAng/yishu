# -*- coding: utf-8 -*-
"""Cycle76 收尾：D080 + METRICS/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D080 — Cycle76 日本陶瓷 4 条（252 → 256）：一条「技术转移」的完整链条
- **决定**：新增 `arita-sake-bottle`（有田伊万里风格酒瓶，17世纪）、`imari-jar`（伊万里花木纹大罐，1600s 末，高40.1cm）、`shino-mizusashi`（志野「绘」水指，16—17世纪）、`kakiemon-beauty`（柿右卫门美人立像，约1690，高38cm，**核心**）。
- **四处要点**：
  1. **技术转移链（据该馆叙述）**：丰臣秀吉 **1593/1597 年侵朝** → 军队**报告朝鲜的多室窑高温瓷技术** → 日本本无此技术，秀吉**令熟练陶工迁居日本** → 朝鲜陶工**在日发现高岭土** → **1600 年代中起**出现日本最早白瓷。条目**照录这条因果链**，并明确标注「为单一机构概述，关键环节未附文献」。
  2. **伊万里外销是「两条件叠加」**：①高岭土发现；②**明亡（1644）后中国外销中断** —— 二者共同为日本创造**供应欧洲**的机会；日本陶工又**仔细研究中国原型**，同时服务国内与海外受众。
  3. **志野水指属茶事**：`mizusashi` 为茶会备水之器；本件称「绘志野」，**一面似水墨芦苇小舟、一面几何纹**——器物因**摆放角度**呈现不同面貌；器形不规则、釉厚而莹，为**桃山茶人所偏好**；**漆盖为近代配换**。
  4. **柿右卫门的「袭名制」**：工房属**酒井田家族**，历代家长**袭名「柿右卫门」**，遂使「作者」成为**制度性主体**；该工房是日本**最早使用多彩釉上珐琅**者之一，并以**乳白瓷胎**著称。条目据此**不指认具体某代传人**。
- **可逆方式**：删 4 条 overlay 与 catalog 元组、移除 4 条来源，重跑 `build_scope.py`。
- **代价**：4 条均单机构；日本陶瓷 4 条（有田/伊万里/志野/柿右卫门），**九谷、锅岛、萨摩等仍缺**。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle76","date":"2026-11-23","status":"completed",
 "gap_methods":["日本陶瓷填补"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["arita-sake-bottle","imari-jar","shino-mizusashi","kakiemon-beauty"],
 "japanese_ceramics":4,
 "must_state":["侵朝→陶工迁日→高岭土的因果链（标注为单机构概述）","伊万里外销=高岭土+明亡断供两条件","志野水指两面不同与近代配盖","柿右卫门袭名制=制度性主体"],
 "new_sources":4,"sources_total":387,"entries_total":256,"pages":293,
 "check_result":"errors=0","check_links_result":"broken=0(293页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle76","date":"2026-11-23","methods_used":["日本陶瓷"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)",
 "verdict":"日本陶瓷 0→4（总 256）；技术转移链与袭名制入正文；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle76"' not in t:
    block=('if cyc=="cycle76":\n'
           '    L.append("- 日本陶瓷 **0 → 4 条（总 252 → 256）**：有田伊万里酒瓶、伊万里大罐、志野「绘」水指、柿右卫门美人立像。'
           '四处要点：①**完整的技术转移链**——秀吉1593/1597侵朝→军队报告朝鲜多室窑高温瓷→令陶工迁日→陶工在日**发现高岭土**'
           '→1600年代中起日本最早白瓷（条目标注「为单一机构概述、关键环节未附文献」）；'
           '②伊万里外销是**两条件叠加**：高岭土发现＋**明亡后中国外销中断**，日本乘势供欧；'
           '③志野水指属**茶事备水**，一面似水墨芦苇小舟、一面几何纹——因**摆放角度**呈现不同面貌，漆盖为**近代配换**；'
           '④柿右卫门属**酒井田家族袭名**，「作者」成为**制度性主体**，条目据**不指认具体代次**。站点 289 → 293 页，体检 12/12。")\n')
    anchor='if cyc=="cycle75":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 252（L2 248 / L3 4 / L1 0） |","| 条目 | 256（L2 252 / L3 4 / L1 0） |"),
    ("| 来源 | 383（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | 387（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | 289，站内断链 **0** |","| 页面 | 293，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **252** | L2 248 / L3 4 / **L1 0** |","| 条目总数 | **256** | L2 252 / L3 4 / **L1 0** |"),
    ("| 来源库 | **383**（另 11 条预备来源未计入） |","| 来源库 | **387**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **289** |","| 站点页面 | **293** |")])]:
    s2=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in s2: s2=s2.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(s2)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])