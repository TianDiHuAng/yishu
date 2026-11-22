# -*- coding: utf-8 -*-
"""给 person_dates_c15.py 启用中文检索（language=zh），失败再回退英文。"""
import io,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","person_dates_c15.py")
s=io.open(P,encoding="utf-8").read()

old_search = 'def search(name,limit=8):\n    d=get("https://www.wikidata.org/w/api.php?action=wbsearchentities&search=%s&language=en&format=json&limit=%d"%(urllib.parse.quote(name),limit))'
new_search = 'def search(name,limit=8,lang="zh"):\n    d=get("https://www.wikidata.org/w/api.php?action=wbsearchentities&search=%s&language=%s&format=json&limit=%d"%(urllib.parse.quote(name),lang,limit))'
assert old_search in s, "search def not found"
s=s.replace(old_search,new_search)

old_call = '    titles=search(e["title"],6)'
new_call = ('    titles=search(e["title"],6)\n'
            '    if not titles: titles=search(e["title"],6,lang="en")')
assert old_call in s, "call site not found"
s=s.replace(old_call,new_call)

io.open(P,"w",encoding="utf-8").write(s)
print("patched: zh search + en fallback")