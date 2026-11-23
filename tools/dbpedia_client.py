# -*- coding: utf-8 -*-
"""DBpedia 客户端（本轮发现的可用通道）。

为什么重要：DBpedia 是 Wikipedia 的结构化抽取，`dct:abstract` 含**英文摘要正文**，
可在 Wikipedia 本体不可达时用来核对既有条目的事实表述（并可作为可点击来源 URL）。

限制（必须诚实标注）：
- DBpedia 与 Wikipedia **同源**，不构成"独立第二来源"；只能用于复核 Wikipedia 已述内容、
  或作为同一事实的另一可访问出处。
- 摘要通常只有首段，不含细节章节。
"""
import json,os,subprocess,urllib.parse,hashlib,time
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE=os.path.join(ROOT,"data","_cache","dbpedia")
os.makedirs(CACHE,exist_ok=True)
UA="YishuBot/1.0 (educational art-history knowledge base; contact: local-maintainer)"
BASE="https://dbpedia.org/data/%s.json"

def _cp(key):
    return os.path.join(CACHE,hashlib.sha1(key.encode()).hexdigest()[:16]+".json")

def resource(name,use_cache=True):
    """取一个 DBpedia 资源的 JSON（name 形如 'Gothic_architecture'）。返回 (dict|None, err)。"""
    url=BASE%urllib.parse.quote(name)
    cp=_cp(url)
    if use_cache and os.path.exists(cp):
        try: return json.load(open(cp,encoding="utf-8")), None
        except Exception: pass
    for i in range(3):
        p=subprocess.run(["curl","-sS","-m","25","-A",UA,url],capture_output=True,text=True,encoding="utf-8",errors="replace")
        out=(p.stdout or "").strip()
        if out.startswith("{"):
            try:
                d=json.loads(out)
                json.dump(d,open(cp,"w",encoding="utf-8"),ensure_ascii=False)
                return d,None
            except Exception: return None,"bad_json"
        time.sleep(1.5*(i+1))
    return None,"failed"

def abstract(name,lang="en",use_cache=True):
    """返回 (摘要文本, 资源URL) 或 (None, None)。"""
    d,err=resource(name,use_cache)
    if not d: return None,None
    key="http://dbpedia.org/resource/"+name
    node=d.get(key) or {}
    for pred in ("http://dbpedia.org/ontology/abstract","http://purl.org/dc/terms/description"):
        for v in node.get(pred,[]):
            if v.get("lang")==lang:
                return v.get("value"), key
            if lang!="en" and v.get("lang")=="en":
                return v.get("value"), key
    return None,None

if __name__=="__main__":
    txt,url=abstract("Gothic_architecture")
    print("URL:",url)
    print("LEN:",len(txt) if txt else 0)
    print((txt or "")[:600])