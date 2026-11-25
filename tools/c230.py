# -*- coding: utf-8 -*-
"""Cycle230：用克利夫兰艺术博物馆开放数据补黄公望、仇英两位人物与 3 件藏品（取回 2026-11-25，缓存 tmp/cma_c230_detail.json）。
用法：python tools/c230.py add ; python tools/build_scope.py ; python tools/c230.py write"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data"); sys.path.insert(0,os.path.join(ROOT,"tools"))
X="来源没有给出，本条目不补写。"
CMAN="2026-11-25 克利夫兰艺术博物馆开放数据 API HTTP 200；"
SRC=[
 ("enc-huang-gongwang","Huang Gongwang","Wikipedia contributors","https://en.wikipedia.org/wiki/Huang_Gongwang","权威百科","2026-11-25 经 Wikipedia REST summary 接口取回，HTTP 200；摘要缓存于 data/_cache/wp"),
 ("wd-huang-gongwang","Wikidata: Huang Gongwang (Q702525)","Wikimedia Foundation（Wikidata 社区维护）","https://www.wikidata.org/wiki/Q702525","权威结构化数据","2026-11-25 由摘要接口返回的 wikibase_item 取得 QID"),
 ("enc-qiu-ying","Qiu Ying","Wikipedia contributors","https://en.wikipedia.org/wiki/Qiu_Ying","权威百科","2026-11-25 经 Wikipedia REST summary 接口取回，HTTP 200；摘要缓存于 data/_cache/wp"),
 ("wd-qiu-ying","Wikidata: Qiu Ying (Q769372)","Wikimedia Foundation（Wikidata 社区维护）","https://www.wikidata.org/wiki/Q769372","权威结构化数据","2026-11-25 由摘要接口返回的 wikibase_item 取得 QID"),
 ("cma-1992-1","Cleveland Museum of Art — Huang Gongwang, Summer Mountains (after Dong Yuan), acc. 1992.1","Cleveland Museum of Art（开放数据 API）","https://openaccess-api.clevelandart.org/api/artworks/1992.1","权威机构藏品记录",CMAN+"立轴 绢本水墨淡设色 画心131.7×55.6cm；说明含《写山水诀》用墨之法与董源"),
 ("cma-1963-102","Cleveland Museum of Art — Qiu Ying, Zhao Mengfu Writing the Heart Sutra in Exchange for Tea, acc. 1963.102","Cleveland Museum of Art（开放数据 API）","https://openaccess-api.clevelandart.org/api/artworks/1963.102","权威机构藏品记录",CMAN+"手卷 纸本水墨淡设色 1542—43 画心20.6×78.3cm；说明含赵孟頫写经换茶"),
 ("cma-1997-94","Cleveland Museum of Art — Wang Meng, Writing Books under the Pine Trees, acc. 1997.94","Cleveland Museum of Art（开放数据 API）","https://openaccess-api.clevelandart.org/api/artworks/1997.94","权威机构藏品记录",CMAN+"册页 纸本水墨设色 画心39.8×56.9cm；说明含赵孟頫外孙、黄鹤山樵、明初入狱"),
]
CP="art-china-painting"
# id,title,kind,era,tier,def,when,overview,related,sources,medium ; sections
E=[
("huang-gongwang","黄公望（Huang Gongwang）","人物","元代","核心",
 "宋末生于江苏常熟的画家、诗人与文人（1269—1354），“元四家”中最年长者。","1269—1354",
 "黄公望，本名陆坚，宋末生于江苏常熟，画家、诗人与作家，是“元四家”中最年长者。克利夫兰艺术博物馆藏其《夏山图（仿董源）》，馆方说明引其论画文字《写山水诀》：作画最难在用墨，先用淡墨逐步加深，再用干而浓的墨与较深的墨染，以分田路、远近；并称他可能借董源的眼光观察自然、学得此法，其风格与董源相通。",
 "yuan-painting,wang-meng,ni-zan,cma-huang-summer-mountains,shan-shui","enc-huang-gongwang,wd-huang-gongwang,cma-1992-1",
 dict(era="宋末生于常熟，属元代（1206—1368）。生卒1269—1354来自摘要描述栏。",feat="克利夫兰馆方说明称其笔线柔圆，常以深线叠于浅线之上。",
      who="元四家中最年长者；代表藏品见《夏山图（仿董源）》条目。《富春山居图》等名作两份来源均未提及，本条目不补写。",
      tech="据馆方说明转引《写山水诀》：先淡墨后浓墨，干笔浓墨与深墨染相配，以分田路与远近。",
      rel="馆方说明称其风格与五代董源相通，“可能”由董源学得用墨之法——这是推测语气。元四家其余三人摘要未点名。",
      nodes=[("董源","风格相通"),("黄公望","元四家最年长"),("写山水诀","论用墨"),("夏山图","克利夫兰藏")])),
("qiu-ying","仇英（Qiu Ying）","人物","明代","核心",
 "明代画家（1494—1552），擅工笔。","1494—1552",
 "仇英是明代画家，擅工笔技法。克利夫兰艺术博物馆称他是苏州的职业画家，藏有其1542—43年为赞助人所作手卷《赵孟頫写经换茶图》。库内另有其《独乐园图》条目。",
 "gongbi,ming-painting,qiu-ying-garden,cma-qiu-ying-tea,wu-school","enc-qiu-ying,wd-qiu-ying,cma-1963-102",
 dict(era="明代，生卒1494—1552来自摘要描述栏；克利夫兰馆方称其为苏州职业画家。",feat="摘要称其擅工笔。",
      who="《赵孟頫写经换茶图》（克利夫兰藏，1542—43）、《独乐园图》（库内另条）。",
      tech="摘要只说擅工笔；具体笔法"+X,
      rel="馆方称其为“职业画家”，为赞助人作画；与吴门画派的关系两份来源均未谈，库内互链为本项目所加。克利夫兰另藏一卷《宫女图》标为清代（1644—1911），归属存疑，本条目不收。",
      nodes=[("苏州","职业画家"),("仇英","明代工笔"),("写经换茶图","1542—43"),("独乐园图","库内另条")])),
("cma-huang-summer-mountains","黄公望《夏山图》（仿董源）","作品","元代","重要",
 "黄公望立轴，绢本水墨淡设色，克利夫兰艺术博物馆藏（1992.1）。","1290—1354（馆方年代）",
 "此立轴为黄公望仿董源笔意的巨幅山水，画心131.7×55.6厘米。馆方说明称其以柔圆笔线绘成，深线常叠于浅线之上，这与《写山水诀》中先淡后浓、以分远近的用墨之法相合。",
 "huang-gongwang,dong-yuan-x,yuan-painting","cma-1992-1",
 dict(era="馆方年代1290—1354，即黄公望在世期间，未定具体年份。",feat="巨幅山水，柔圆笔线，深线叠于浅线。",
      who="黄公望；题称仿五代董源（活动于约937—975）。",tech="绢本水墨淡设色；先淡墨后浓墨的层叠用墨。画心131.7×55.6厘米，全幅257.4×71.2厘米。",
      rel="馆方以《写山水诀》解释此画用墨，并推测黄公望由董源学得此法。",
      nodes=[("董源","所仿"),("夏山图","立轴·绢本"),("写山水诀","用墨之法"),("131.7×55.6cm","画心")])),
("cma-qiu-ying-tea","仇英《赵孟頫写经换茶图》","作品","明代","重要",
 "仇英手卷，纸本水墨淡设色，克利夫兰艺术博物馆藏（1963.102）。","1542—1543年",
 "馆方说明称，相传元代书法家赵孟頫（1254—1322）曾为一位李姓僧人抄写《心经》以换茶；明代苏州职业画家仇英为其赞助人画了这一场景。画中赵孟頫执笔，面前铺纸，案上有砚、墨锭和小水滴；水滴入砚，研墨锭即成墨汁。",
 "qiu-ying,zhao-mengfu,ming-painting","cma-1963-102",
 dict(era="1542—1543年，明代。",feat="以文人故事为题，细写文房器具。",
      who="仇英；画中人物赵孟頫。",tech="手卷，纸本水墨淡设色；画心20.6×78.3厘米，全卷21.1×553.6厘米。",
      rel="写经换茶是“相传”之事，馆方未作考证。",
      nodes=[("赵孟頫","画中人物"),("写经换茶图","手卷1542—43"),("文房","砚·墨·水滴"),("赞助人","受画者")])),
("cma-wang-meng-pine","王蒙《松下著书图》","作品","元末明初","重要",
 "王蒙册页，纸本水墨设色，克利夫兰艺术博物馆藏（1997.94）。","约1308—1385（馆方以画家生卒为年代）",
 "馆方说明称王蒙出身吴兴（今湖州）名门，是赵孟頫的外孙；除在元、明两朝断续任职外，一生多半隐退，此画即表达这一点。1360年代红巾军反元、蒙古人失去对江南的控制时，他退入杭州以北山中，自号黄鹤山樵；明初受清洗牵连死于狱中。",
 "wang-meng,zhao-mengfu,yuan-painting","cma-1997-94",
 dict(era="馆方年代为画家生卒（约1308—1385），未定作画年份。",feat="以松下著书表达隐退之志。",
      who="王蒙；馆方称其为赵孟頫外孙。",tech="册页，纸本水墨设色；画心39.8×56.9厘米。",
      rel="馆方所述生平与王蒙条目所据中文维基一致（黄鹤山樵、明初入狱），赵孟頫外孙一点为本条新增来源所给。",
      nodes=[("赵孟頫","外祖父"),("松下著书图","册页"),("黄鹤山樵","自号"),("隐退","主题")])),
]
def add():
    sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
    for sid,t,a,u,ty,n in SRC:
        if sid not in have: sd["sources"].append({"id":sid,"title":t,"author":a,"year":"2026","url":u,"type":ty,"verified":True,"verified_note":n})
    json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
    p=os.path.join(ROOT,"tools","catalog.py"); txt=io.open(p,encoding="utf-8").read(); lines=txt.split("\n")
    T=[(e[0],e[1],e[2],CP,e[3],"中国","绘画",e[4],e[5],e[6],e[7],e[8].replace("dong-yuan-x,",""),e[9]) for e in E if "('%s',"%e[0] not in txt]
    close=max(i for i,l in enumerate(lines) if l.strip()=="]")
    lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
    io.open(p,"w",encoding="utf-8").write("\n".join(lines)); print("catalog appended",len(T),"sources",len(sd["sources"]))
def write():
    from render_l2_svg import render_svg
    for e in E:
        s=e[10]; nodes=s["nodes"]; src=e[9].split(",")
        one=len(src)==1
        todo="（1）"+("本条目只有克利夫兰艺术博物馆藏品记录一个来源，整条标记待核实。" if one else "人物事实来自 Wikipedia 摘要与同源 Wikidata，另有克利夫兰馆方说明一个独立来源，整条仍标待核实。")+"（2）来源未给出的作品与年代一律未补写。"
        sec={"时代背景":s["era"],"风格特征":s["feat"],"代表人物与作品":s["who"],"技法或形式分析":s["tech"],"与前后风格的关系和争论":s["rel"],
             "一图":"示意图以%s为中心，标示%s。"%(nodes[1][0],"、".join(n[0] for i,n in enumerate(nodes) if i!=1)),"待核实":todo}
        diag={"nodes":[{"label":a,"sub":b,"kind":"accent" if i==1 else "muted"} for i,(a,b) in enumerate(nodes)],"arrows":[{"from":1,"to":i} for i in (0,2,3)],"caption":"据所引来源"}
        json.dump({"id":e[0],"level":"L2","sections":sec,"svg":render_svg(diag,e[0]),"sources":src,"needs_verification":True,
                   "pending_notes":"单一机构来源" if one else "百科同源＋一馆藏来源"},
                  open(os.path.join(D,"l2",e[0]+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=2)
    print("wrote",len(E))
{"add":add,"write":write}[sys.argv[1]]()
