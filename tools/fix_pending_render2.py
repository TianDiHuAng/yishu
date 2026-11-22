# -*- coding: utf-8 -*-
"""Cycle29 修正 render_pending：
① 先把开头的「状态说明：…以【已复核】为准。」整句摘出，作为独立提示（不当列表项）；
② 其余文本按「【已复核…】<正文至下一个【或结尾>」切分为复核记录；
③ 剩余开头部分按（N）编号或分号拆为未解决项。"""
import io,os,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","gen_site.py")
s=io.open(P,encoding="utf-8").read()
start=s.index("def render_pending(")
end=s.index("def build_entry(e,entries):")
NEW='''def render_pending(text):
    """待核实结构化呈现：状态说明 / 未解决项列表 / 复核记录。只改呈现，不改内容。"""
    if not text: return ""
    t=text.strip()
    note=""
    m=re.match(r"^(状态说明：[^。]*。)", t)
    if m:
        note=m.group(1); t=t[m.end():].strip()
    # 复核记录：以【已复核…】开头，正文到下一个【为止
    recs=[]
    pattern=re.compile(r"(【已复核[^】]*】)(.*?)(?=【已复核|$)", re.S)
    for mm in pattern.finditer(t):
        recs.append((mm.group(1), mm.group(2).strip()))
    open_txt=pattern.sub("", t).strip()
    items=re.findall(r"（\\d+）([^（]+)", open_txt)
    if not items:
        items=[x.strip() for x in re.split(r"[；;]", open_txt) if x.strip()]
    out=["<div class='pending'>"]
    if note:
        out.append("<p class='note'>%s</p>"%esc(note))
    if items:
        out.append("<strong>待核实（未解决）</strong><ol>")
        for it in items:
            out.append("<li>%s</li>"%esc(it.strip().rstrip("；;。 ")))
        out.append("</ol>")
    if recs:
        out.append("<details class='rec'><summary>复核记录（%d 条，均已找到来源）</summary><ol>"%len(recs))
        for tag,body in recs:
            out.append("<li><span class='eyebrow'>%s</span> %s</li>"%(esc(tag.strip("【】")),esc(body[:400])))
        out.append("</ol></details>")
    out.append("</div>")
    return "".join(out)

'''
s=s[:start]+NEW+s[end:]
io.open(P,"w",encoding="utf-8").write(s)
# 补 CSS（.note）
if ".pending .note{" not in s:
    s2=io.open(P,encoding="utf-8").read()
    old=".pending ol{margin:.4em 0 0;padding-left:1.5em}"
    if old in s2:
        s2=s2.replace(old, old+"\n.pending .note{font-size:.82rem;color:var(--ink-faint);margin:0 0 8px}")
        io.open(P,"w",encoding="utf-8").write(s2)
print("render_pending rewritten")
chk=io.open(P,encoding="utf-8").read()
print("has note css:", ".pending .note{" in chk)