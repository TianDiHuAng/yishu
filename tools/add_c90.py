# -*- coding: utf-8 -*-
"""Cycle90：中国青铜礼器 4 条。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-2005-54","Cleveland Museum of Art — Wine Vessel (Jia), Shang, c. 1250–1046 BCE, acc. 2005.54",
  "https://openaccess-api.clevelandart.org/api/artworks/2005.54","2026-11-23 API HTTP 200；青铜 50.8cm；说明含安阳王都与祖先祭祀"),
 ("cma-1960-288","Cleveland Museum of Art — Tripod Cauldron (Ding), Shang, 1200–1100 BCE, acc. 1960.288",
  "https://openaccess-api.clevelandart.org/api/artworks/1960.288","2026-11-23 API HTTP 200；青铜 14.3×12.5cm；说明含宋代以来青铜著录传统"),
 ("cma-2003-2","Cleveland Museum of Art — Tripod (Ding), Western Zhou, 1000s BCE, acc. 2003.2",
  "https://openaccess-api.clevelandart.org/api/artworks/2003.2","2026-11-23 API HTTP 200；青铜 57.4cm；说明含饕餮纹与政治合法性"),
 ("cma-1989-3","Cleveland Museum of Art — Bell (Lai Zhong), Western Zhou, c. 800–700 BCE, acc. 1989.3",
  "https://openaccess-api.clevelandart.org/api/artworks/1989.3","2026-11-23 API HTTP 200；青铜 70.3×37×26.6cm；说明含118字铭文与乐悬制度"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('shang-jia-vessel','商代青铜爵（jia）','作品','art-ancient','公元前13—前11世纪','中国','雕塑','核心',
  '安阳期大型青铜酒器，克利夫兰艺术博物馆藏（2005.54）。','约公元前1250—公元前1046年',
  '三足外撇可架火加热；用于商王室祖先祭祀，祈求丰收与战功。','shang-zhou-bronzes,chinese-jade-art','cma-2005-54'),
 ('shang-ding-small','商代青铜鼎','作品','art-ancient','公元前13—前12世纪','中国','雕塑','重要',
  '商代小型青铜鼎，克利夫兰艺术博物馆藏（1960.288）。','公元前1200—前1100年',
  '按大小成组使用，以谷物与肉奉献祖先；宋代以来成为著录、铭文与类型学研究核心材料。','shang-zhou-bronzes,regular-script','cma-1960-288'),
 ('zhou-ding-large','西周大型青铜鼎','作品','art-ancient','公元前11—前10世纪','中国','雕塑','核心',
  '西周大型青铜鼎，克利夫兰艺术博物馆藏（2003.2）。','公元前1000年代',
  '饕餮纹列于装饰带，双目凝视以激起敬畏；三足以公羊图像装饰；鼎兼为政治权力与合法性的象征。','shang-zhou-bronzes,shang-ding-small','cma-2003-2'),
 ('lai-zhong-bell','逨钟（青铜编钟）','作品','art-ancient','公元前9—前8世纪','中国','综合','核心',
  '陕西眉县西周青铜钟，克利夫兰艺术博物馆藏（1989.3）。','约公元前800—公元前700年',
  '为八件成组编钟之一；118字铭文记逨的世职与为先父作钟；铭文亦被视为早期书法实例。','yayue,shang-zhou-bronzes','cma-1989-3'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
assert close is not None
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")