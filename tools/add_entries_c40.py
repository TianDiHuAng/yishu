# -*- coding: utf-8 -*-
"""Cycle40 步骤1（修正版）：新增 4 条目到 catalog ROWS + 4 条权威机构来源。
单元 id 校正：degas→art-impression，rodin→art-modern，作品→work-archives。
"""
import io,json,os,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")

SRC=[
 {"id":"cma-1916-1043","title":"Cleveland Museum of Art — Edgar Degas, Dancers (c. 1896), acc. 1916.1043",
  "author":"Cleveland Museum of Art（开放数据 API）","year":"2026",
  "url":"https://clevelandart.org/art/1916.1043","type":"权威机构藏品记录","verified":True,
  "verified_note":"2026-11-23 openaccess-api HTTP 200：title/creation_date/technique/measurements/accession/description/creators 全部取到"},
 {"id":"cma-1918-328","title":"Cleveland Museum of Art — Auguste Rodin, The Age of Bronze (1875–76), acc. 1918.328",
  "author":"Cleveland Museum of Art（开放数据 API）","year":"2026",
  "url":"https://clevelandart.org/art/1918.328","type":"权威机构藏品记录","verified":True,
  "verified_note":"2026-11-23 openaccess-api HTTP 200：尺寸/题记/铸造者铭文(A. RUDIER)/provenance/description 取到"},
 {"id":"vam-o1758562","title":"Victoria and Albert Museum — Auguste Rodin, Mask of Hanako, Type E Study (1912), O1758562",
  "author":"Victoria and Albert Museum（V&A API v2）","year":"2026",
  "url":"https://collections.vam.ac.uk/item/O1758562/","type":"权威机构藏品记录","verified":True,
  "verified_note":"2026-11-23 api.vam.ac.uk/v2/museumobject/O1758562 HTTP 200：title/材料(paste glass)/高度22cm"},
 {"id":"cma-1933-220","title":"Cleveland Museum of Art — Mi Youren, Cloudy Mountains (1130), acc. 1933.220",
  "author":"Cleveland Museum of Art（开放数据 API）","year":"2026",
  "url":"https://clevelandart.org/art/1933.220","type":"权威机构藏品记录","verified":True,
  "verified_note":"2026-11-23 openaccess-api HTTP 200：尺寸/题记及英译/provenance/description/creators(1072–1151) 取到"},
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8"))
have={s["id"] for s in sd["sources"]}
for s in SRC:
    if s["id"] not in have: sd["sources"].append(s)
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources now:",len(sd["sources"]))

TUPLES=[
 ('degas','埃德加·德加','人物','art-impression','19世纪','法国','绘画','重要',
  '法国画家，以芭蕾舞者与后台场景题材著称，常被列入印象派群体但对这一标签持保留。','1834—1917年',
  '以粉彩层叠技法描绘舞者与日常瞬间，偏好非舞台正面的私密视角；芭蕾题材作品逾千件。','impressionism,monet','cma-1916-1043'),
 ('rodin','奥古斯特·罗丹','人物','art-modern','19—20世纪','法国','雕塑','重要',
  '法国雕塑家，以强调人体表面起伏与心理张力著称，常被视为现代雕塑的重要起点。','1840—1917年',
  '代表作《青铜时代》《思想者》；常去除叙事道具以突出身体本身，生前声名与争议并存。','realism-art,rodin-age-of-bronze','cma-1918-328,vam-o1758562'),
 ('rodin-age-of-bronze','罗丹《青铜时代》','作品','work-archives','19世纪','法国','雕塑','重要',
  '奥古斯特·罗丹的青铜雕像，克利夫兰艺术博物馆藏（1918.328），为其现存最早等身雕塑。','1875—76年（本铸件1916年铸造）',
  '塑造一名初醒的男性裸体；原持矛而作者去之，使观者专注身体的感觉与心理强度；因高度写实曾被误指为真人翻模。','rodin,realism-art','cma-1918-328'),
 ('mi-youren-cloudy-mountains','米友仁《云山图》','作品','work-archives','12世纪','中国','绘画','重要',
  '米友仁作手卷，克利夫兰艺术博物馆藏（1933.220），为其南渡后有纪年与自题之作。','1130年',
  '以湿墨点累积营造云山迷蒙氛围，承其父米芾一脉的墨戏传统；卷后有作者自题纪年与记事。','song-painting,china-painting-history','cma-1933-220'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
# ROWS 的结束行：最后一个单独的 ']'
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
assert close is not None, "ROWS closing bracket not found"
block=[]
for t in TUPLES:
    body=",\n ".join(repr(x) for x in t)
    block.append("(%s)," % body)
lines[close:close]=block
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog tuples appended at line",close+1)
r=subprocess.run([sys.executable,"-X","utf8","-c",
  "import sys;sys.path.insert(0,'tools');from catalog import entries;es=entries();print('entries',len(es));print([e['id'] for e in es[-4:]])"],
  cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print(r.stdout.strip()); print(r.stderr.strip()[-200:])