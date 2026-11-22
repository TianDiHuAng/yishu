# -*- coding: utf-8 -*-
"""Cycle23：pass2 匹配——用条目 id（本身就是英文 slug）与实体英文标签比对。
规则：norm(id) 与 norm(label) 相等或互为子串，且描述含该类条目类型词 → 命中。
这能解决"实体有英文标签、条目是中文标题"的歧义组，同时天然排除学术论文（其标签与 id 不同）。"""
import json,os,re,subprocess,urllib.parse,time
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
UA="YishuBot/1.0 (educational; local)"
def curl_json(u,tries=4,timeout=25):
    for i in range(tries):
        p=subprocess.run(["curl","-sS","-m",str(timeout),"-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
        if p.returncode==0 and p.stdout.strip().startswith("{"):
            try: return json.loads(p.stdout)
            except Exception: pass
        time.sleep(0.4*(i+1))
    return None
def norm(t): return re.sub(r"[^a-z0-9]","",(t or "").lower())
TORMS={"人物":["painter","sculptor","composer","artist","architect","musician","polymath","calligrapher","pianist","violinist","conductor"],
 "作品":["painting","fresco","sculpture","musical work","ballet","composition","mural","opera","artwork"],
 "风格":["style","movement","school","genre","tradition","tendency","period"],
 "时期":["period","era","civilization","age","century","dynasty","art"],
 "术语":["term","technique","concept","notation","instrument","mode","system","theory","principle","practice"]}
d=json.load(open(os.path.join(ROOT,"reports","entity_map_c22.json"),encoding="utf-8"))
es={e["id"]:e for e in json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]}
# 收集所有 ambiguous + none 的候选
pool={}
for grp in ("ambiguous","none"):
    for x in d[grp]:
        pool[x["id"]]=[(c["qid"],c["label"],c["desc"]) for c in x.get("candidates",[])]
# none 组没有候选，重新检索一次（用 id 作为查询词）
def search(q,lang="en",limit=5):
    r=curl_json("https://www.wikidata.org/w/api.php?action=wbsearchentities&search=%s&language=%s&format=json&limit=%d"%(urllib.parse.quote(q),lang,limit))
    return [(x["id"],x.get("label",""),x.get("description","")) for x in (r or {}).get("search",[])]
for eid in list(pool):
    if not pool[eid]:
        q=es[eid]["id"].replace("-"," ")
        pool[eid]=search(q)
# 批量取实体描述（en）
ids=sorted({c[0] for cs in pool.values() for c in cs})
desc={}
for i in range(0,len(ids),50):
    ch=ids[i:i+50]
    r=curl_json("https://www.wikidata.org/w/api.php?action=wbgetentities&ids=%s&props=labels|descriptions&languages=en|zh&format=json"%("%7C".join(ch)))
    for qid,e in ((r or {}).get("entities",{}) or {}).items():
        labels={k:v["value"] for k,v in e.get("labels",{}).items() if k in ("en","zh")}
        desc[qid]={"labels":labels,"desc":((e.get("descriptions",{}).get("en") or {}).get("value") or "")}
    print("  batch",i//50+1,"desc cached",len(desc),"/",len(ids))
matched=[]
for eid,cs in pool.items():
    e=es[eid]; nid=norm(e["id"]); tw=TORMS.get(e["kind"],[])
    for qid,lbl,dd in cs:
        info=desc.get(qid,{"labels":{"en":lbl},"desc":dd or ""})
        lab=norm(info["labels"].get("en") or lbl)
        if not lab: continue
        same=(lab==nid) or (len(nid)>4 and (nid in lab or lab in nid))
        typ=any(t in (info["desc"] or "").lower() for t in tw)
        if same and typ:
            matched.append({"id":eid,"kind":e["kind"],"title":e["title"],"qid":qid,
                            "label":info["labels"].get("zh") or info["labels"].get("en") or lbl,
                            "desc":(info["desc"] or dd)[:60]})
            break
print("pass2 命中:",len(matched))
for m in matched[:15]: print("  ",m["id"],m["qid"],m["label"],"|",m["desc"][:45])
json.dump(matched,open(os.path.join(ROOT,"reports","entity_pass2_c23.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)