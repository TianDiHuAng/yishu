# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle136"; DATE="2026-11-24"
IDS=["lefem-commemorative-figure","chi-wara-headdress","esu-dance-staff","kuofo-prestige-stool"]
ET,ST,PG=472,598,509
DECIS="""## D139 — Cycle136 非洲 4 条（468 → 472）
`lefem-commemorative-figure`（Bangwa 王室纪念像，**核心**；生前雕造作替身、Lefem 会社保管、王室神龛见证祖颅献祭）、
`chi-wara-headdress`（Bamana chi wara，**核心**；农耕兽＝人/羚羊/食蚁兽、成对男女舞于农赛与婚礼）、
`esu-dance-staff`（约鲁巴 Èṣù 舞杖，**核心**；跨界神性：成对男女喻性别互转/化死为生、礼笛、货贝＝财富）、
`kuofo-prestige-stool`（Bamileke 珠饰「行凳」，**核心**；王室库藏、豹纹喻王化身猛兽）。
art-africa 32→36。写前查重通过。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（CMA）。
"""
REPORT=("- 非洲 4 条（468 → 472，CMA）：Bangwa lefem 纪念像（**生前雕造作替身**、Lefem 会社、王室神龛献祭）、"
 "Bamana chi wara（**农耕兽＝人/羚羊/食蚁兽**、成对男女舞于农赛/婚礼）、约鲁巴 Èṣù 舞杖（**跨界神性**：性别互转/化死为生、礼笛、货贝财富）、"
 "Bamileke 珠饰行凳（王室库藏、**豹纹喻王化身猛兽**）。art-africa 32→36。站点 505 → 509 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["非洲（CMA）"],"network":"CMA ok",
 "new_entries":4,"new_entry_ids":IDS,"new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["非洲"],"gaps_found":{"entries":4},"network":"CMA","verdict":"art-africa 32→36（总472）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle135":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle135":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **468**（L2 464 / L3 4 / L1 0） |","| 条目 | **472**（L2 468 / L3 4 / L1 0） |"),("| 来源 | **594**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **598**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **505**，站内断链 **0** |","| 页面 | **509**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **468** | L2 464 / L3 4 / **L1 0** |","| 条目总数 | **472** | L2 468 / L3 4 / **L1 0** |"),("| 来源库 | **594**（另 11 条预备来源未计入） |","| 来源库 | **598**（另 11 条预备来源未计入） |"),("| 站点页面 | **505** |","| 站点页面 | **509** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **468**（L2 464 / L3 4，**无 L1**） |","| 条目 | **472**（L2 468 / L3 4，**无 L1**） |"),("| 来源 | **594**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **598**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **505** |","| 站点页面 | **509** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)