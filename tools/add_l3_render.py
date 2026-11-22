# -*- coding: utf-8 -*-
"""为 gen_site.py 增加 L3 深度渲染：争议并列表（holder/basis）、数据表、复杂图示说明。
在 build_entry 的 L2 七节之后、相关条目之前插入 L3 深度块。"""
import io, os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","gen_site.py")
s=io.open(P,encoding="utf-8").read()

# 1) CSS 增加 L3 样式
css_anchor=".pending{background:var(--paper-2);border-left:3px solid var(--gold);padding:14px 18px;border-radius:0 8px 8px 0;font-size:.9rem;color:var(--ink-soft)}"
css_add=css_anchor+"""
.l3-block{background:var(--card);border:1px solid var(--accent-soft);border-radius:var(--radius);padding:22px;margin:0 0 34px}
.l3-block h2{font-size:1.3rem}
.controversy{border-left:3px solid var(--gold);padding:6px 0 6px 16px;margin:14px 0}
.controversy .issue{font-weight:600;color:var(--ink);margin-bottom:6px}
.controversy .view{font-size:.92rem;color:var(--ink-soft);margin:3px 0}
.controversy .view .holder{color:var(--accent);font-weight:600}
.data-table{margin:12px 0}
.badge-l3{background:var(--accent);color:var(--paper);padding:2px 8px;border-radius:4px;font-family:var(--mono);font-size:.7rem}"""
assert css_anchor in s
s=s.replace(css_anchor,css_add)

# 2) 在 L2 分支的 "相关条目" 之前插入 L3 深度块
anchor="""        if e.get(\"related\"):
            s.append(\"<div class='section-block'><h2><span class='num'>08</span>相关条目</h2><ul class='rel-list'>\")"""
assert anchor in s, "entry related anchor not found"
l3code="""        if lv=="L3" and e.get("l3"):
            l3=e["l3"]
            s.append("<div class='l3-block'><h2><span class='badge-l3'>L3 深度</span> 争议、数据与复杂图示</h2>")
            for c in l3.get("controversies",[]):
                s.append("<div class='controversy'><div class='issue'>%s</div>"%esc(c.get("issue","")))
                for v in c.get("views",[]):
                    s.append("<div class='view'><span class='holder'>%s：</span>%s</div>"%(esc(v.get("holder","")),esc(v.get("basis",""))))
                s.append("</div>")
            if l3.get("data"):
                s.append("<h3>关键数据（均有来源）</h3><table class='data-table'><thead><tr><th>项目</th><th>数值/事实</th><th>说明</th></tr></thead><tbody>")
                for d in l3["data"]:
                    s.append("<tr><td>%s</td><td>%s</td><td>%s</td></tr>"%(esc(d.get("label","")),esc(d.get("value","")),esc(d.get("note",""))))
                s.append("</tbody></table>")
            if l3.get("complex_diagram_note"):
                s.append("<p class='eyebrow'>复杂图示说明：%s</p>"%esc(l3["complex_diagram_note"]))
            s.append("</div>")
"""
s=s.replace(anchor, l3code+anchor)
io.open(P,"w",encoding="utf-8").write(s)
print("gen_site.py L3 rendering added")
