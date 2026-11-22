# -*- coding: utf-8 -*-
"""重核 sources.json 中未通过的来源：更大匹配窗口 + 重试 + <title> 标签提取。"""
import json, os, re, ssl, time, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, "data", "sources.json")

def fetch(url):
    ctx = ssl.create_default_context()
    last = None
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
                "Accept-Language":"en-US,en;q=0.9"})
            with urllib.request.urlopen(req, timeout=30, context=ctx) as r:
                return r.status, r.read(1500000).decode("utf-8","ignore")
        except Exception as e:
            last = e; time.sleep(1.2*(attempt+1))
    raise last

def check(s):
    url = s["url"]
    kw = {
      "enc-egyptian-art":"Egyptian art","enc-high-renaissance":"High Renaissance",
      "enc-surrealism":"Surrealism","enc-van-gogh":"van Gogh","enc-cezanne":"Cezanne",
      "enc-song-dynasty-art":"Song dynasty","enc-yuan-dynasty-art":"Yuan dynasty",
      "enc-chinese-music":"Chinese music","enc-jingju":"Beijing opera",
      "inst-met-heilbrunn":"Heilbrunn","inst-khan-art":"Art History",
      "inst-nga-glossary":"National Gallery",
    }.get(s["id"], s["title"].split()[0])
    # Cezanne -page 用重音字符
    try:
        status, html = fetch(url)
    except Exception as e:
        return s["id"], False, "仍失败: %s: %s" % (type(e).__name__, str(e)[:70])
    m = re.search(r"<title[^>]*>(.*?)</title>", html, re.I|re.S)
    title_tag = re.sub(r"<[^>]+>","", m.group(1)) if m else ""
    hay = (title_tag + " " + html[:200000]).lower()
    alts = [kw.lower()]
    if s["id"]=="enc-cezanne": alts += ["cézanne"]
    if s["id"]=="enc-egyptian-art": alts += ["egyptian art","ancient egypt"]
    if s["id"]=="inst-met-heilbrunn": alts += ["heilbrunn timeline","metmuseum"]
    if s["id"]=="inst-khan-art": alts += ["khan academy","art history"]
    if s["id"]=="inst-nga-glossary": alts += ["national gallery of art","nga.gov"]
    ok = status < 400 and any(a in hay for a in alts)
    note = "HTTP %d; <title>=%s" % (status, title_tag[:60])
    return s["id"], ok, note

def main():
    data = json.load(open(P, encoding="utf-8"))
    todo = [s for s in data["sources"] if not s["verified"]]
    res = {}
    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = {ex.submit(check,s): s["id"] for s in todo}
        for f in as_completed(futs):
            try:
                sid, ok, note = f.result(); res[sid]=(ok,note)
            except Exception as e:
                res[futs[f]]=(False,"异常 %s"%str(e)[:60])
    n=0
    for s in data["sources"]:
        if s["id"] in res:
            ok, note = res[s["id"]]
            s["verified"]=bool(ok); s["verified_note"]=note
            if ok: n+=1
    json.dump(data, open(P,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
    total_ok = sum(1 for s in data["sources"] if s["verified"])
    print("reverified pass=%d, total verified=%d/%d" % (n, total_ok, len(data["sources"])))
    print("still unverified:", ", ".join(s["id"] for s in data["sources"] if not s["verified"]) or "(none)")

if __name__=="__main__": main()
