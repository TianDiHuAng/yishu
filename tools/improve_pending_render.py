# -*- coding: utf-8 -*-
"""Cycle29（重做，单脚本原子完成并自检）：待核实结构化渲染。
包含：import re、render_pending 函数、L2/L1 两处调用替换、CSS。"""
import io,os,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","gen_site.py")
s=io.open(P,encoding="utf-8").read()

# 0) import re
if not re.search(r"^import json, os, html, glob, re$", s, re.M):
    s=s.replace("import json, os, html, glob","import json, os, html, glob, re",1)

FN = '''def render_pending(text):
    """把待核实文本拆成：未解决项列表 + 复核记录（纯呈现，不改动字符串内容）。"""
    if not text: return ""
    parts=re.split(r"(【已复核[^】]*】)", text)
    open_txt=parts[0]
    records=[]
    i=1
    while i < len(parts):
        tag=parts[i]; body=parts[i+1] if i+1 < len(parts) else ""
        records.append((tag, body.strip())); i+=2
    items=re.findall(r"（\\d+）([^（]+)", open_txt)
    if not items:
        items=[x.strip() for x in re.split(r"[；;]", open_txt) if x.strip()]
    out=["<div class='pending'>"]
    if items:
        out.append("<strong>待核实（未解决）</strong><ol>")
        for it in items:
            out.append("<li>%s</li>"%esc(it.strip().rstrip("；;。 ")))
        out.append("</ol>")
    if records:
        out.append("<details class='rec'><summary>复核记录（%d 条）</summary><ol>"%len(records))
        for tag,body in records:
            out.append("<li><span class='eyebrow'>%s</span> %s</li>"%(esc(tag.strip("【】")),esc(body[:400])))
        out.append("</ol></details>")
    out.append("</div>")
    return "".join(out)

'''
if "def render_pending(" not in s:
    a="def build_entry(e,entries):"
    assert a in s
    s=s.replace(a, FN+a, 1)

old_l2='''            elif nm=="待核实":
                notes=sec.get(nm,"")
                s.append("<div class='pending'>%s</div>"%esc(notes))'''
new_l2='''            elif nm=="待核实":
                s.append(render_pending(sec.get(nm,"")))'''
assert old_l2 in s, "L2 branch not found"
s=s.replace(old_l2,new_l2)

old_l1='''            s.append("<div class='pending'><strong>待核实</strong><p>%s</p></div>"%esc(e.get("pending_notes","")))'''
new_l1='''            s.append(render_pending(e.get("pending_notes","")))'''
if old_l1 in s: s=s.replace(old_l1,new_l1)

css_anchor="details.rec{margin-top:10px}" if "details.rec" in s else ".badge-l3{"
if "details.rec{" not in s:
    old3=".badge-l3{background:var(--accent);color:var(--paper);padding:2px 8px;border-radius:4px;font-family:var(--mono);font-size:.7rem}"
    new3=old3+"""
details.rec{margin-top:10px}
details.rec summary{cursor:pointer;font-size:.86rem;color:var(--ink-soft)}
details.rec ol{margin:.5em 0 0;padding-left:1.4em;font-size:.84rem;color:var(--ink-soft)}
.pending ol{margin:.4em 0 0;padding-left:1.5em}
.pending li{margin:3px 0}"""
    assert old3 in s
    s=s.replace(old3,new3)
io.open(P,"w",encoding="utf-8").write(s)

# 自检
chk=io.open(P,encoding="utf-8").read()
print("has render_pending:", "def render_pending(" in chk)
print("L2 calls it:", chk.count("render_pending(sec.get") == 1)
print("L1 calls it:", chk.count('render_pending(e.get("pending_notes"') == 1)
print("has details.rec css:", "details.rec{" in chk)
print("import re:", "import json, os, html, glob, re" in chk)