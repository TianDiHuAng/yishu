# -*- coding: utf-8 -*-
"""Cycle22：gen_site 增加 entities.html（条目↔Wikidata 实体对照），并加入导航。"""
import io,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","gen_site.py"); s=io.open(P,encoding="utf-8").read()
# 导航
old='(REL+"people.html","人物"),(REL+"glossary.html","术语"),'
new='(REL+"people.html","人物"),(REL+"glossary.html","术语"),(REL+"entities.html","实体对照"),'
assert old in s; s=s.replace(old,new)
# 生成函数
anchor="def build_sources():"
assert anchor in s
fn='''def build_entity_map(entries):
    rows=[]
    for e in entries:
        for sid in e.get("sources",[]):
            s=SM.get(sid)
            if s and s.get("type","").startswith("权威结构化数据（身份锚点）"):
                rows.append((e,s))
    rows.sort(key=lambda t:t[0]["title"])
    s=[head("实体对照")]
    s.append("<div class='wrap'><h1>实体对照（Wikidata 身份锚点）</h1>")
    s.append("<p class='eyebrow'>%d 条 · 仅用于身份锚定，不作为事实依据</p>"%len(rows))
    s.append("<p>说明：本页列出条目与其对应的 Wikidata 实体，便于读者跳转到结构化数据核对；"
             "条目的年代、风格与评价仍以各自条目页标注的来源为准。</p>")
    s.append("<table><thead><tr><th>条目</th><th>Wikidata 实体</th><th>实体描述</th></tr></thead><tbody>")
    for e,src in rows:
        s.append("<tr><td><a href='entries/%s.html'>%s</a></td><td><a href='%s'>%s</a></td><td>%s</td></tr>"%(
            esc(e["id"]),esc(e["title"]),esc(src["url"]),esc(src["title"].split("：")[-1]),esc(src.get("verified_note","")[60:120])))
    s.append("</tbody></table></div>"+FOOT)
    open(os.path.join(OUT,"entities.html"),"w",encoding="utf-8").write("".join(s))

'''
s=s.replace(anchor, fn+anchor)
# main 调用（根页面段）
old_main='build_sources(); build_people_index(entries); build_glossary(entries)'
new_main='build_sources(); build_people_index(entries); build_glossary(entries); build_entity_map(entries)'
assert old_main in s; s=s.replace(old_main,new_main)
io.open(P,"w",encoding="utf-8").write(s)
print("gen_site: entities.html added")