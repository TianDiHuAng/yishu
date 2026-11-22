# -*- coding: utf-8 -*-
"""Cycle17 质量闸（本轮变更：2 条建筑条目 + 2 条 wd 来源）：
1) 抽查新增 wikidata 来源：URL HTTP 200 且 title 里的 QID 与 EntityData label 一致；
2) 检查条目正文是否出现"来源未支撑的精确年代"（若有，须已在待核実列明）；
3) 输出 reports/qc_c17.json。"""
import json,os,re,subprocess
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
UA="YishuBot/1.0 (educational; local)"
def curl_json(u,tries=4):
    import time
    for i in range(tries):
        p=subprocess.run(["curl","-sS","-m","20","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
        if p.returncode==0 and p.stdout.strip().startswith("{"):
            try: return json.loads(p.stdout)
            except Exception: pass
        time.sleep(0.6*(i+1))
    return None
src={s["id"]:s for s in json.load(open(os.path.join(D,"sources.json"),encoding="utf-8"))["sources"]}
es={e["id"]:e for e in json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]}
out={"new_sources":[],"entries":[],"issues":[]}
for sid in ["wd-gothic-architecture","wd-romanesque-architecture"]:
    s=src[sid]; qid=re.search(r"(Q\d+)",s["url"]).group(1)
    d=curl_json("https://www.wikidata.org/w/api.php?action=wbgetentities&ids=%s&props=labels&languages=zh|en&format=json"%qid)
    L=((d or {}).get("entities",{}).get(qid,{}) or {}).get("labels",{})
    zh=(L.get("zh") or {}).get("value"); en=(L.get("en") or {}).get("value")
    ok=bool(zh or en) and (qid in s["title"])
    out["new_sources"].append({"id":sid,"qid":qid,"zh":zh,"en":en,"title":s["title"],"ok":ok})
    print(sid,qid,"label=",zh or en,"| title一致:",qid in s["title"],"| OK" if ok else "| FAIL")
for eid in ["gothic-architecture","romanesque-architecture"]:
    e=es[eid]; body="".join(e["sections"][k] for k in ["时代背景","风格特征","代表人物与作品","技法或形式分析","与前后风格的关系和争论"])
    pend=e["sections"]["待核实"]
    years=set(re.findall(r"\d{2,4}",body))
    uncovered=[y for y in years if y not in pend and y not in e["when"]]
    rec={"id":eid,"years_in_body":sorted(years),"years_not_in_pending":sorted(uncovered),
         "sources":e["sources"],"level":e.get("level")}
    out["entries"].append(rec)
    print(eid,"| body years:",sorted(years),"| 未在待核实列明:",sorted(uncovered) or "无")
    if uncovered: out["issues"].append([eid,"正文年份未在待核实列明",sorted(uncovered)])
json.dump(out,open(os.path.join(ROOT,"reports","qc_c17.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("issues:",len(out["issues"]))