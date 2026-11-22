# -*- coding: utf-8 -*-
"""Wikidata API 客户端（遵守速率限制 + 本地缓存）。

本轮发现：之前的批量取实体一直静默失败，根因是触发了 Wikimedia 速率限制，
返回纯文本 "You are making too many requests"，而旧的 curl_json 只接受以 "{" 开头的响应 → 静默变空。

本模块修正：
1) 正确 User-Agent（含用途与联系占位，符合 Wikimedia 政策）；
2) 串行限速：默认每请求间隔 >= 1.0 秒；
3) 429/限流时指数退避（5s/15s/45s）；
4) 磁盘缓存（data/_cache/wd/*.json），命中不再请求 —— 避免重复消耗配额；
5) 返回 (data, error) 元组，**绝不把限流当作“无数据”**。

用法：
    from wd_api import api_get, entity
    data, err = api_get({"action":"wbsearchentities","search":"印象派","language":"zh","limit":5})
"""
import json,os,re,time,hashlib,ssl,subprocess,urllib.parse

ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE=os.path.join(ROOT,"data","_cache","wd")
os.makedirs(CACHE,exist_ok=True)
UA="YishuBot/1.0 (educational art-history knowledge base; local-only build; contact: local-maintainer)"
API="https://www.wikidata.org/w/api.php"
MIN_INTERVAL=1.0
_last=[0.0]

def _throttle():
    dt=time.time()-_last[0]
    if dt<MIN_INTERVAL: time.sleep(MIN_INTERVAL-dt)
    _last[0]=time.time()

def _cache_path(key):
    h=hashlib.sha1(key.encode("utf-8")).hexdigest()[:16]
    return os.path.join(CACHE,h+".json")

def api_get(params,use_cache=True,retries=4):
    """返回 (dict|None, err|None)。err 为字符串（含 'rate_limited' / 'http_xxx' / 'bad_json'）。"""
    qs=urllib.parse.urlencode(params,safe="|",quote_via=urllib.parse.quote)
    url=API+"?"+qs
    cp=_cache_path(url)
    if use_cache and os.path.exists(cp):
        try: return json.load(open(cp,encoding="utf-8")), None
        except Exception: pass
    delay=[5,15,45,90]
    for i in range(retries):
        _throttle()
        p=subprocess.run(["curl","-sS","-m","25","-A",UA,url],capture_output=True,text=True,encoding="utf-8",errors="replace")
        out=(p.stdout or "").strip()
        if out.startswith("{"):
            try:
                d=json.loads(out)
                json.dump(d,open(cp,"w",encoding="utf-8"),ensure_ascii=False)
                return d, None
            except Exception:
                return None,"bad_json"
        low=out.lower()
        if "too many requests" in low or "rate limit" in low:
            if i<retries-1: time.sleep(delay[min(i,len(delay)-1)]); continue
            return None,"rate_limited"
        if p.returncode!=0:
            time.sleep(delay[min(i,len(delay)-1)]); continue
        # 其它非 JSON 文本（可能是 HTML 错误页）
        time.sleep(delay[min(i,len(delay)-1)])
    return None,"failed"

def entity(qid,use_cache=True):
    d,err=api_get({"action":"wbgetentities","ids":qid,"props":"labels|descriptions|claims",
                   "languages":"zh|en","format":"json"},use_cache=use_cache)
    if err or not d: return None,err
    return (d.get("entities",{}) or {}).get(qid),None

def search(q,lang="zh",limit=6,use_cache=True):
    d,err=api_get({"action":"wbsearchentities","search":q,"language":lang,"limit":limit,"format":"json"},use_cache=use_cache)
    if err or not d: return [],err
    return [(x["id"],x.get("label",""),x.get("description","")) for x in d.get("search",[])],None

if __name__=="__main__":
    # 自检：一次搜索 + 一次实体
    r,err=search("印象派")
    print("search:",len(r),"err:",err)
    e,err2=entity("Q40415")
    print("entity:", (e or {}).get("labels",{}).get("zh",{}).get("value"), "err:",err2)
    print("cache files:",len(os.listdir(CACHE)))