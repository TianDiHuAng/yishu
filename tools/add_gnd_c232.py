# -*- coding: utf-8 -*-
"""Cycle210：给 103 个人物条目补 GND（德国国家图书馆规范档）来源，并把 GND 生卒年与站内年代逐条比对。
匹配：只用 GND 记录 sameAs 中含本条目 Wikidata QID 的命中（见 probe_gnd_c210.py，结果 tmp/gnd_c232.json）。
不改正文年代：一致的写“已由 GND 独立印证”；不一致的写出两种说法，留待核实。"""
import json,os,re,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
H=json.load(open(os.path.join(ROOT,"tmp","gnd_c232.json"),encoding="utf-8"))
E={e["id"]:e for e in json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]}
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
def yr(s):
    if not s: return None
    m=re.match(r"-?0*(\d{1,4})",s); return int(m.group(1)) if m else None
def site_years(e):
    t=" ".join([e.get("when") or "",e.get("def") or "",e.get("overview") or ""])
    m=re.search(r"(\d{3,4})(?:/\d{2,4})?\s*[—–-]\s*(\d{3,4})",t)
    return (int(m.group(1)),int(m.group(2))) if m else (None,None)
same=diff=nodate=0; report=[]
for eid,r in H.items():
    sid="gnd-"+r["gnd"]
    gb,gd=yr(r["birth"]),yr(r["death"])
    if sid not in have:
        sd["sources"].append({"id":sid,"title":"GND — %s, %s"%(r["name"],r["gnd"]),
            "author":"Deutsche Nationalbibliothek（Gemeinsame Normdatei，经 lobid.org）","year":"2026",
            "url":"https://d-nb.info/gnd/"+r["gnd"],"type":"国家图书馆人名规范记录（标目、生卒、职业）","verified":True,
            "verified_note":"2026-11-25 经 lobid.org 取回；该记录 sameAs 含 Wikidata %s，按编号与本条目匹配；标目“%s”，生 %s，卒 %s"%(r["qid"],r["name"],r["birth"],r["death"])})
        have.add(sid)
    p=os.path.join(D,"l2",eid+".json"); j=json.load(open(p,encoding="utf-8"))
    j["sources"]=list(dict.fromkeys(j.get("sources",[])+[sid]))
    sb,sdth=site_years(E[eid])
    gtxt="%s—%s"%(gb if gb else "?",gd if gd else "?")
    if gb is None and gd is None:
        note="（GND 对照，2026-11-25）德国国家图书馆规范档有此人记录（%s），但未给出生卒年，只印证标目与身份。"%r["gnd"]; nodate+=1; tag="无年代"
    elif sb is None:
        note="（GND 对照，2026-11-25）德国国家图书馆规范档（%s）给出生卒 %s；本条目未写具体生卒年，可据此补充。"%(r["gnd"],gtxt); nodate+=1; tag="站内无年"
    elif (gb in (None,sb)) and (gd in (None,sdth)):
        note="（GND 对照，2026-11-25）德国国家图书馆规范档（%s）生卒 %s，与本条目一致，已独立印证（只印证生卒与身份）。"%(r["gnd"],gtxt); same+=1; tag="一致"
    else:
        note="（GND 对照，2026-11-25）德国国家图书馆规范档（%s）生卒作 %s，本条目作 %s—%s，两者不一致；本条目暂不改动，待专门文献核定。"%(r["gnd"],gtxt,sb,sdth); diff+=1; tag="不一致"
    if "（GND 对照，2026-11-25）" not in j["sections"]["待核实"]: j["sections"]["待核实"]+=note
    pn=j.get("pending_notes","")
    if tag=="一致": head="生卒已由 GND 规范档独立印证；"
    elif tag=="不一致": head="生卒与 GND 规范档不一致（GND %s，本条目 %s—%s）；"%(gtxt,sb,sdth)
    elif tag=="站内无年": head="GND 规范档给出生卒 %s，本条目尚未写入；"%gtxt
    else: head="GND 规范档有记录但无生卒年；"
    if not pn.startswith(head): j["pending_notes"]=head+pn
    json.dump(j,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
    report.append((tag,eid,gtxt,"%s—%s"%(sb,sdth)))
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
for t in report:
    if t[0]!="一致": print(*t)
print("一致",same,"不一致",diff,"缺年",nodate,"sources",len(sd["sources"]))
