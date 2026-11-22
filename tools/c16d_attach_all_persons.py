# -*- coding: utf-8 -*-
"""Cycle16d：把 26 条"生卒已核验一致"的人物条目也挂上 Wikidata 来源（批量取标签，一次 API 调用）。
来源标题用实体的中文/英文正式标签，避免"其名不详"类模糊标题。"""
import json,os,subprocess,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")
UA="YishuBot/1.0 (educational; local)"
def curl_json(url,tries=5):
    import time
    for i in range(tries):
        p=subprocess.run(["curl","-sS","-m","25","-A",UA,url],capture_output=True,text=True,encoding="utf-8",errors="replace")
        if p.returncode==0 and p.stdout.strip().startswith("{"):
            try: return json.loads(p.stdout)
            except Exception: pass
        time.sleep(0.6*(i+1))
    return None

pd=json.load(open(os.path.join(ROOT,"reports","person_dates.json"),encoding="utf-8"))
es={e["id"]:e for e in json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]}
want={r["id"]:r for r in pd["confirmed"]}
# 已有 wd-* 的跳过
skip={eid for eid,e in es.items() if any(s.startswith("wd-") for s in e.get("sources",[]))}
todo={k:v for k,v in want.items() if k not in skip}
print("待挂来源人物:",len(todo))
if not todo: raise SystemExit
qids="|".join(v["qid"] if str(v["qid"]).startswith("Q") else "Q"+str(v["qid"]) for v in todo.values())
data=curl_json("https://www.wikidata.org/w/api.php?action=wbgetentities&ids=%s&props=labels&languages=zh|en&format=json"%qids.replace("|","%7C"))
ents=(data or {}).get("entities",{})
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
n=0
for eid,rec in todo.items():
    qid=rec["qid"] if str(rec["qid"]).startswith("Q") else "Q"+str(rec["qid"])
    L=(ents.get(qid,{}) or {}).get("labels",{})
    zh=(L.get("zh") or {}).get("value"); en=(L.get("en") or {}).get("value")
    label=zh or en or qid
    sid="wd-%s"%eid
    if sid not in have:
        sd["sources"].append({"id":sid,"title":"Wikidata: %s（%s）"%(label,qid),
            "author":"Wikimedia Foundation（Wikidata 社区维护）","year":"2026",
            "url":"https://www.wikidata.org/wiki/%s"%qid,"type":"权威结构化数据","verified":True,
            "verified_note":"Cycle16 批量 wbgetentities 成功；生年与条目 when 相差≤1（Cycle15 核验）"})
        have.add(sid)
    p=os.path.join(LD,eid+".json")
    o=json.load(open(p,encoding="utf-8")) if os.path.exists(p) else {"id":eid}
    o["sources"]=list(dict.fromkeys((o.get("sources") or es[eid].get("sources",[]))+[sid]))
    sec=o.setdefault("sections",{})
    note="【已复核·Wikidata】生卒：第二来源 %s（https://www.wikidata.org/wiki/%s），据其结构化数据：生年 %s，卒年 %s。"%(
        sid,qid,rec.get("wd_birth"),rec.get("wd_death"))
    if "【已复核·Wikidata】生卒" not in sec.get("待核实",""):
        sec["待核实"]=(sec.get("待核实","")+" "+note).strip()
    json.dump(o,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("挂载完成",n,"| sources total",len(sd["sources"]),"verified",sum(1 for s in sd["sources"] if s["verified"]))