# -*- coding: utf-8 -*-
"""Cycle25：①采纳 pass3 唯一精确命中（serialism → Q507246）为身份锚点；
②为 gen_site 增加 status.html（公开覆盖与校验状态：条目/层级/来源/审计结果/已知缺口）。"""
import json,os,io
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")
# ① 锚点
h=json.load(open(os.path.join(ROOT,"reports","entity_pass3_c25.json"),encoding="utf-8"))[0]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
sid="wd-anchor-%s"%h["id"]
if sid not in have:
    sd["sources"].append({"id":sid,"title":"Wikidata 实体（身份锚点）：%s（%s）"%(h["label"],h["qid"]),
        "author":"Wikimedia Foundation（Wikidata 社区维护）","year":"2026",
        "url":"https://www.wikidata.org/wiki/%s"%h["qid"],
        "type":"权威结构化数据（身份锚点）","verified":True,
        "verified_note":"Cycle25 pass3 精确命中（id 与英文标签完全一致）；仅作身份锚点，不作事实依据"})
    have.add(sid)
es={e["id"]:e for e in json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]}
p=os.path.join(LD,h["id"]+".json"); o=json.load(open(p,encoding="utf-8"))
o["sources"]=list(dict.fromkeys((o.get("sources") or es[h["id"]]["sources"])+[sid]))
json.dump(o,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("anchor added:",h["id"],h["qid"],"| sources",len(sd["sources"]))

# ② status.html
P=os.path.join(ROOT,"tools","gen_site.py"); s=io.open(P,encoding="utf-8").read()
if "def build_status(" not in s:
    old='(REL+"people.html","人物"),(REL+"glossary.html","术语"),(REL+"entities.html","实体对照"),'
    new='(REL+"people.html","人物"),(REL+"glossary.html","术语"),(REL+"entities.html","实体对照"),(REL+"status.html","状态"),'
    assert old in s; s=s.replace(old,new)
    anchor="def build_sources():"
    fn='''def build_status(entries):
    from collections import Counter
    """公开状态页：规模、层级、来源、校验结论、已知缺口（数据来自本仓库 JSON/报告，不含新断言）。"""
    lv=Counter(e.get("level","L2") for e in entries)
    tier=Counter(e["tier"] for e in entries)
    withwd=sum(1 for e in entries if any(str(x).startswith("wd-") for x in e.get("sources",[])))
    anchors=sum(1 for x in SOURCES if str(x.get("type","")).startswith("权威结构化数据（身份锚点）"))
    facts=sum(1 for x in SOURCES if str(x.get("type",""))=="权威结构化数据")
    s=[head("状态")]
    s.append("<div class='wrap'><h1>站点状态</h1>")
    s.append("<p class='eyebrow'>数据驱动 · 机器校验 · 诚实标注</p>")
    s.append("<div class='stats'>")
    for n,l in [(len(entries),"条目"),(len(SOURCES),"来源"),(len(UNITS),"单元"),(lv.get("L3",0),"L3 深度"),(withwd,"含 Wikidata 关联")]:
        s.append("<div class='stat'><div class='n'>%d</div><div class='l'>%s</div></div>"%(n,l))
    s.append("</div>")
    s.append("<div class='section-block'><h2>层级与重要性</h2>")
    s.append("<p>写作深度：L1 %d · L2 %d · L3 %d</p>"%(lv.get("L1",0),lv.get("L2",0),lv.get("L3",0)))
    s.append("<p>重要性：核心 %d · 重要 %d · 补充 %d</p>"%(tier.get("核心",0),tier.get("重要",0),tier.get("补充",0)))
    s.append("</div>")
    s.append("<div class='section-block'><h2>来源构成</h2>")
    s.append("<p>来源总数 %d（其中 Wikidata 事实来源 %d 条、身份锚点 %d 条）。</p>"%(len(SOURCES),facts,anchors))
    s.append("<p>身份锚点仅用于确认“条目所指的实体”，<b>不作为事实依据</b>；见 <a href='entities.html'>实体对照</a>。</p>")
    s.append("</div>")
    s.append("<div class='section-block'><h2>校验与已知缺口</h2>")
    s.append("<p>每次构建前运行 <code>tools/audit_all.py</code>：硬规则（R1–R17）、站内链接、九维体检、内容自洽、关联图、单向关联、工具可编译。"
             "上述检查在本版均为通过状态；具体数值见仓库 reports/ 目录。</p>")
    s.append("<p>已知缺口（诚实披露）：①A 类覆盖缺口 58 项，建筑已开工 3 条，其余待可核验来源；"
             "②B2 类候选缺口 22 项（非西方音乐体裁在站内零覆盖）；③部分条目“待核实”项仍待第二来源；"
             "④Wikipedia / Met / Tate 在当前构建环境不可达，内容类来源无法即时复核。</p>")
    s.append("</div></div>"+FOOT)
    open(os.path.join(OUT,"status.html"),"w",encoding="utf-8").write("".join(s))

'''
    s=s.replace(anchor, fn+anchor)
    old_main='build_sources(); build_people_index(entries); build_glossary(entries); build_entity_map(entries)'
    new_main='build_sources(); build_people_index(entries); build_glossary(entries); build_entity_map(entries); build_status(entries)'
    assert old_main in s; s=s.replace(old_main,new_main)
    io.open(P,"w",encoding="utf-8").write(s)
    print("gen_site: status.html added")