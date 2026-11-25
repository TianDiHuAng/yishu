import json, re, os, sys, urllib.request, urllib.parse, glob
# 扫描下一批核心条目：取 enc- 来源对应的英文维基全文，抽出写到学界争议的句子
os.makedirs('tmp/l3', exist_ok=True)
done = {os.path.basename(p)[:-5] for p in glob.glob('tmp/l3/*.json')}
srcs = {}
for p in ['data/sources.json']:
    try:
        for s in json.load(open(p, encoding='utf-8'))['sources']:
            srcs[s['id']] = s
    except Exception:
        pass
ents = json.load(open('data/entries.json', encoding='utf-8'))['entries']
cands = []
for e in ents:
    lp = 'data/l2/%s.json' % e['id']
    lv = json.load(open(lp, encoding='utf-8')).get('level') if os.path.exists(lp) else e.get('level')
    if e.get('tier') != '核心' or lv == 'L3' or e['id'] in done:
        continue
    enc = [s for s in e.get('sources', []) if isinstance(s, str) and s == 'enc-' + e['id']]
    if enc:
        cands.append((e['id'], enc[0]))
N = int(sys.argv[1]) if len(sys.argv) > 1 else 25
cands = cands[:N]
print('candidates', len(cands))
PAT = re.compile(r'[^.]*\b(debated?|debates|controvers\w*|disputed?|contested|questioned|scholars (?:disagree|differ)|argued that|others (?:argue|believe|maintain))\b[^.]*\.')
out = {}
for eid, sid in cands:
    url = srcs.get(sid, {}).get('url', '')
    title = urllib.parse.unquote(url.rsplit('/', 1)[-1]) if 'wikipedia' in url else ''
    if not title:
        continue
    q = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&format=json&titles=' + urllib.parse.quote(title)
    try:
        req = urllib.request.Request(q, headers={'User-Agent': 'yishu/1.0'})
        d = json.load(urllib.request.urlopen(req, timeout=20))
        t = next(iter(d['query']['pages'].values())).get('extract', '')
    except Exception as ex:
        print('ERR', eid, ex); continue
    json.dump({'id': eid, 'title': title, 'text': t}, open('tmp/l3/%s.json' % eid, 'w', encoding='utf-8'), ensure_ascii=False)
    hits = [m.group(0).strip().replace('\n', ' ')[:300] for m in PAT.finditer(t)]
    out[eid] = hits
    print(eid, len(t), len(hits), flush=True)
json.dump(out, open('tmp/l3_scan_c219.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
