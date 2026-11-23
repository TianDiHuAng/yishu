# -*- coding: utf-8 -*-
"""Cycle65：enc-* 来源条目的结构层复核（低噪声四项）。
A 来源数分布；
B 仅 1 个来源的条目必须 needs_verification=True；
C 正文/待核实里出现的 URL 必须存在于 sources.json；
D 【已复核】留痕必须能对应到库内来源 id。
输出 reports/enc_audit_c65.json。"""
import json,os,re,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
es=json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]
src={s["id"]:s for s in json.load(open(os.path.join(D,"sources.json"),encoding="utf-8"))["sources"]}
urls={s["url"] for s in src.values()}
enc=[e for e in es if any(s.startswith("enc-") for s in e.get("sources",[]))]
print("enc-* 条目：%d（全库 %d）"%(len(enc),len(es)))
from collections import Counter
print("来源数分布：",dict(Counter(len(e.get("sources",[])) for e in enc)))
issues=[]
for e in enc:
    n=len(e.get("sources",[]))
    if n==1 and not e.get("needs_verification"):
        issues.append((e["id"],"B: 仅1个来源却未标待核实"))
    body=" ".join(e.get("sections",{}).values())
    for u in set(re.findall(r"https?://[^\s　，。；：！？（）【】「」』]+",body)):
        if u not in urls:
            issues.append((e["id"],"C: 正文引用 URL 不在来源库: %s"%u[:60]))
    for m in re.finditer(r"【已复核[^】]*】",body):
        seg=body[m.end():m.end()+200]
        ids=re.findall(r"\b(enc|wd|inst|web|cma|vam)-[a-z0-9-]+",seg)
        for i in ids:
            found=[k for k in src if re.match(r"%s"%re.escape(i),k)]
            if not found:
                issues.append((e["id"],"D: 复核留痕引用的来源 id 不存在: %s"%i))
print("问题：%d"%len(issues))
for i in issues[:15]: print("  ",i)
json.dump({"enc_entries":len(enc),"issues":issues,
           "source_count_dist":dict(Counter(len(e.get("sources",[])) for e in enc))},
          open(os.path.join(ROOT,"reports","enc_audit_c65.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
sys.exit(1 if issues else 0)
