# -*- coding: utf-8 -*-
"""Cycle55 收尾：D059 + METRICS/SATURATION/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D059 — Cycle55 条目达 200（195 → 200）；朝鲜朝白瓷的殖民来源与刚果十字架的跨文化信仰写入正文
- **决定**：新增 5 条：`joseon-auspicious-jar`（白瓷四字纹罐）、`joseon-buncheong-flask`（粉青刻花酒壶）、`kongo-prestige-cap`（mpu ngola）、`kongo-crucifix`（刚果十字架）、`khmer-thai-fruit-jar`（泰东北窑果形罐）。
- **三处必须写进正文的「不舒服/非审美」内容**：
  1. **白瓷罐的来源史**：该馆写明本件**1981年购自东京古美术商「壶中居」**（1924年创立），并指出**许多重要韩国文物在日据时期（1910—45）被带往日本、留在私人收藏**，日本商家因而成为重要流通渠道。条目把「器物的美」与「它如何来到这里」并置。
  2. **刚果十字架不是复制品**：1491年国王 Nzinga a Nkuwu 改宗后，刚果天主教「独特地反映其环境」；此像**基督结刚果式发辫**，下方形像**因反复触摸而磨光**；腰布上的 **X 形**指涉很可能**先于基督教**的 **dikenga dia Kongo**（生命四节点）。条目照录该馆判断，不代其裁定两种传统的权重。
  3. **权贵帽的修复事实**：拉菲草**年久变硬**，该馆修复人员为这件脆化的帽子制作**直立支架**——修复不是隐形工作，而是器物当前状态的一部分。
- **两处如实保留「未知」**：泰东北窑果形罐的**所拟果种该馆明言难定**（可能为瓜）；刚果十字架下方形像**圣母或信徒**，该馆并列两说。
- **未覆盖并记录在案**：泰国素可泰/宋加洛窑、越南李陈窑**仍无条目**（本轮检索仅得 1 件高棉陶，已用；其余为干扰项）；埃塞俄比亚只检索到当代作品，未采用。
- **可逆方式**：删 5 条 overlay 与 catalog 元组、移除 5 条来源，重跑 `build_scope.py`。
- **代价**：5 条均单机构（`needs_verification`）；「200 条」是条目数里程碑，**不等于覆盖均衡**——非洲 9 条、大洋洲 2 条、东南亚 4 条，仍远薄于欧洲与中国。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle55","date":"2026-11-23","status":"completed",
 "gap_methods":["区块推进（朝鲜朝瓷/刚果/泰东北窑）"],"network":"partial: museum APIs ok",
 "new_entries":5,"new_entry_ids":["joseon-auspicious-jar","joseon-buncheong-flask","kongo-prestige-cap","kongo-crucifix","khmer-thai-fruit-jar"],
 "milestone":"条目达 200",
 "must_state":["朝鲜朝白瓷罐的日据期外流与1981年东京购藏","刚果十字架的本地化基督形象与 dikenga 符号","权贵帽的拉菲草脆化与直立支架修复"],
 "explicit_unknowns":["泰东北窑果形罐果种","刚果十字架下方形像身份"],
 "not_covered":["泰国素可泰/宋加洛窑","越南李陈窑","埃塞俄比亚历史时期"],
 "new_sources":5,"sources_total":331,"entries_total":200,"pages":235,
 "check_result":"errors=0","check_links_result":"broken=0(235页)","audit_all":"10/10 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle55","date":"2026-11-23","methods_used":["区块推进"],
 "gaps_found":{"entries":5},"network":"partial (museum APIs)",
 "verdict":"条目达 200；殖民来源与跨文化信仰入正文；两处未知保留；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle55"' not in t:
    block=('if cyc=="cycle55":\n'
           '    L.append("- 新增 5 条，**条目达 200**（195 → 200）：朝鲜朝白瓷四字罐与粉青刻花壶、刚果 mpu ngola 权贵帽、'
           '刚果十字架、泰东北窑果形罐。三处非审美内容入正文：①白瓷罐**1981 年购自东京「壶中居」**，'
           '该馆并写明**许多韩国文物在日据期（1910—45）被带往日本**、日本商家成为重要流通渠道；'
           '②刚果十字架**不是复制品**——1491 年改宗后本地化，基督结**刚果式发辫**，下方形像**因反复触摸而磨光**，'
           '腰布 **X 形** 指涉很可能先于基督教的 **dikenga dia Kongo**（生命四节点）；③权贵帽的拉菲草**年久变硬**，'
           '该馆为脆化帽体制作**直立支架**——修复即器物当前状态的一部分。'
           '两处未知照实保留（果形罐的果种、十字架下方形像身份）。站点 230 → 235 页，体检 10/10。")\n')
    anchor='if cyc=="cycle54b":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 195（L2 191 / L3 4 / L1 0） |","| 条目 | 200（L2 196 / L3 4 / L1 0） |"),
    ("| 来源 | 326（全部 verified；隔离区 5 条 + 预备 11 条） |","| 来源 | 331（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | 230，站内断链 **0** |","| 页面 | 235，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **195** | L2 191 / L3 4 / **L1 0** |","| 条目总数 | **200** | L2 196 / L3 4 / **L1 0** |"),
    ("| 来源库 | **326**（另 11 条预备来源未计入） |","| 来源库 | **331**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **230** |","| 站点页面 | **235** |")])]:
    s2=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in s2: s2=s2.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(s2)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50],(r.stderr or "").strip()[-120:])