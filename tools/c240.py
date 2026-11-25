# -*- coding: utf-8 -*-
"""Cycle240：把 14 个摘要过短、不宜单独成条的乐理基础词合成一个导读条目“音乐基础要素”。
每个词只转述各自的 Wikipedia 摘要（取回 2026-11-25，缓存 data/_cache/wp），各配 Wikipedia + Wikidata 两源。
用法：python tools/c240.py add ; python tools/build_scope.py ; python tools/c240.py write"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data"); sys.path.insert(0,os.path.join(ROOT,"tools"))
WP="https://en.wikipedia.org/wiki/"
NOTE="2026-11-25 经 Wikipedia REST summary 接口取回，HTTP 200；摘要缓存于 data/_cache/wp；用于导读条目 music-basics 的一个小节"
WDN="2026-11-25 由同一摘要接口返回的 wikibase_item 取得 QID"
W=[("melody","Melody","Q170412"),("timbre","Timbre","Q176501"),("scale-music","Scale_(music)","Q179651"),
   ("interval-music","Interval_(music)","Q189962"),("triad","Triad_(music)","Q944899"),("key-music","Key_(music)","Q534932"),
   ("meter-music","Metre_(music)","Q630649"),("binary-form","Binary_form","Q1193859"),("rondo","Rondo","Q13323"),
   ("minuet","Minuet","Q205734"),("variation-form","Variation_(music)","Q214981"),("ostinato","Ostinato","Q216745"),
   ("woodwind","Woodwind_instrument","Q181247"),("string-instrument","String_instrument","Q1798603")]
SRC=[]
for k,pg,q in W: SRC+=["enc-"+k,"wd-"+k]
EID="music-basics"
T=(EID,"音乐基础要素：旋律、音色、音高组织、拍子与常见曲式","术语","overview-guide","历代","欧洲","音乐体裁","重要",
 "导读条目：把旋律、音色、音阶、音程、三和弦、调、拍子、二部曲式、回旋曲式、小步舞曲、变奏、固定音型、木管与弦乐器 14 个基础词放在一处说明。","历代（概念工具，本项目划分）",
 "本条目把 14 个基础词合在一起，每个词只写各自来源给出的定义。旋律是听者感知为一个整体的线性音列；音色是区分声源的声音品质；音阶是从一个音到其八度之间的连续音列；音程是两音的音高差；三和弦是可按三度叠置的三个音；调是乐曲中最常用的音高与调性稳定中心；拍子是规则重复的强弱拍型。曲式方面，二部曲式由两个相关段落组成（常作 A-A-B-B），回旋曲式以主部主题与对比主题交替（如 ABACA），变奏是以改变后的形式重复材料，固定音型是同一声部中持续重复的动机。小步舞曲是源于法国的双人社交舞，通常为三拍子。乐器分类中，木管属管乐器大类，弦乐器靠振动的弦发声。",
 "texture-music,ternary-form,strophic-form,homophony,polyphony,tonality,sonata-form,brass-instrument,keyboard-instrument",
 ",".join(SRC))
SEC={
 "时代背景":"这些是乐理与分析用语，本身没有单一年代；“历代”为本项目划分。小步舞曲一词源自意大利语 minuetto 与法语 menuet，是 14 个词中唯一带历史来源的。",
 "风格特征":"旋律：一串在听者感知中构成整体的音，字面上是音高与节奏的结合，是背景伴奏前的前景（来源：Melody 摘要）。音色：又称音质，使人能按来源区分声音，如合唱人声与乐器，也能区分同类乐器（来源：Timbre 摘要）。",
 "代表人物与作品":"各来源摘要都没有点名作曲家或作品，本条目不补写。",
 "技法或形式分析":"音高组织——音阶：从一音到其八度的任何连续音列，通常按音高排列；音程：两音之间的音高差，相继发声为旋律音程，同时发声为和声音程；三和弦：可按三度纵向叠置的三个音，是西方音乐最常见的和弦；调：西方调性音乐中乐曲最常用的音高与调性稳定中心。时间组织——拍子：规则重复的强拍、拍点等模式；与节奏不同，拍点不一定发声，但由演奏者暗示、为听者所预期。曲式——二部曲式：两个相关段落、通常各自反复，常作 A-A-B-B；回旋曲式：主部主题与一个或多个对比主题交替，如 ABACA、ABACABA；变奏：材料以改变后的形式重复，可改旋律、节奏、和声、对位、音色或配器；固定音型：同一声部中持续重复的动机或乐句，常在同一音高。",
 "与前后风格的关系和争论":"舞曲——小步舞曲：源于法国的双人社交舞，通常为 3/4 拍。乐器——木管乐器：管乐器大类中的一族；弦乐器（又称弦鸣乐器）：演奏者以扫、拨、击等方式使弦振动发声。各词之间的联系（如三部曲式、主调与复调、奏鸣曲式）为库内互链，本项目所加。",
 "一图":"示意图以“音乐基础要素”为中心，分出音高组织、时间组织、曲式三组。",
 "待核实":"（1）本条目由 14 个词的 Wikipedia 摘要拼合而成，每个词配同源 Wikidata，来源独立性有限，整条标记待核实。（2）这些摘要多只有一两句定义，本条目不补写例子、历史或作曲家。（3）合并为一条是本项目的编排决定：这些词单独成条内容过薄（见 D239）。"}
NODES=[("音高组织","音阶·音程·三和弦·调"),("音乐基础要素","14 个基础词"),("时间组织","拍子"),("曲式","二部·回旋·变奏·固定音型")]
def add():
    sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
    for k,pg,q in W:
        pn=pg.replace("_"," ")
        for s in ({"id":"enc-"+k,"title":pn,"author":"Wikipedia contributors","year":"2026","url":WP+pg,"type":"权威百科","verified":True,"verified_note":NOTE},
                  {"id":"wd-"+k,"title":"Wikidata: %s (%s)"%(pn,q),"author":"Wikimedia Foundation（Wikidata 社区维护）","year":"2026","url":"https://www.wikidata.org/wiki/"+q,"type":"权威结构化数据","verified":True,"verified_note":WDN}):
            if s["id"] not in have: sd["sources"].append(s); have.add(s["id"])
    json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
    p=os.path.join(ROOT,"tools","catalog.py"); txt=io.open(p,encoding="utf-8").read(); lines=txt.split("\n")
    if "('%s',"%EID not in txt:
        close=max(i for i,l in enumerate(lines) if l.strip()=="]")
        lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in T)]
        io.open(p,"w",encoding="utf-8").write("\n".join(lines))
    print("sources",len(sd["sources"]))
def write():
    from render_l2_svg import render_svg
    diag={"nodes":[{"label":a,"sub":b,"kind":"accent" if i==1 else "muted"} for i,(a,b) in enumerate(NODES)],"arrows":[{"from":1,"to":i} for i in (0,2,3)],"caption":"据 14 则 Wikipedia 摘要"}
    json.dump({"id":EID,"level":"L2","sections":SEC,"svg":render_svg(diag,EID),"sources":SRC,"needs_verification":True,
               "pending_notes":"来源独立性有限（14 则 Wikipedia 摘要+同源 Wikidata）；合并成条为本项目编排"},
              open(os.path.join(D,"l2",EID+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=2)
    print("wrote",EID)
{"add":add,"write":write}[sys.argv[1]]()
