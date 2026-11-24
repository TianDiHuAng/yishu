# -*- coding: utf-8 -*-
"""Cycle134：项目级一致性深度审计（不改内容，只诊断）。"""
import json,os,glob,re,subprocess,sys,collections
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
es=json.load(open('data/site_entries.json',encoding='utf-8'))['entries']
src=json.load(open('data/sources.json',encoding='utf-8'))['sources']
srcids={s['id'] for s in src}
units=json.load(open('data/coverage.json',encoding='utf-8'))
pages=glob.glob('*.html')+glob.glob('entries/*.html')+glob.glob('units/*.html')
print('== 基本 ==')
print('entries',len(es),'sources',len(src),'pages',len(pages))
problems=[]
# 1) 每条 sources 均在库
for e in es:
    for s in e.get('sources',[]):
        if s not in srcids: problems.append(('missing-source',e['id'],s))
# 2) 每来源至少被引用一次
used={s for e in es for s in e.get('sources',[])}
unused=[s['id'] for s in src if s['id'] not in used]
if unused: problems.append(('unused-sources',len(unused),unused[:5]))
# 3) overlay 与 entries 对齐
ov=set()
for p in glob.glob('data/l2/*.json'):
    ov.add(os.path.splitext(os.path.basename(p))[0])
entids={e['id'] for e in es}
orphan_ov=ov-entids
if orphan_ov: problems.append(('orphan-overlays',len(orphan_ov),list(orphan_ov)[:5]))
# 4) sitemap 条目数
sm=open('sitemap.xml',encoding='utf-8').read() if os.path.exists('sitemap.xml') else ''
urls=re.findall(r'<loc>',sm)
print('sitemap <loc> 数:',len(urls))
# 5) 每页 <title> 非空
bad_title=0
for p in pages:
    t=open(p,encoding='utf-8',errors='replace').read()
    m=re.search(r'<title>(.*?)</title>',t,re.S)
    if not m or not m.group(1).strip(): bad_title+=1
print('空<title>页:',bad_title)
# 6) entries 页文件数 vs es 数
ent_pages=glob.glob('entries/*.html')
print('entries/*.html:',len(ent_pages))
# 7) 单元分布与 coverage 一致性
cu=collections.Counter(e['unit'] for e in es)
print('units used:',len(cu))
# 8) 检查 svg 均存在且非空
nosvg=[e['id'] for e in es if not e.get('svg')]
if nosvg: problems.append(('empty-svg',len(nosvg),nosvg[:5]))
# 9) needs_verification 统计
nv=sum(1 for e in es if e.get('needs_verification'))
print('needs_verification:',nv,'/',len(es))
# 10) 层级分布
print('levels:',collections.Counter(e.get('level','L2') for e in es))
print('== 问题 ==',problems if problems else '无')
