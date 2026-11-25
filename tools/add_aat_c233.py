# -*- coding: utf-8 -*-
"""Cycle233：给 7 个新增风格/术语条目补盖蒂 AAT 来源（精确标签命中，见 tmp/aat_c233.json）。
只在“待核实”追加 AAT 对照说明，不改正文；断代或范围有差异的写明差异。幂等。"""
import json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
TAG="（AAT 对照，2026-11-25）"
A={
 "pictorialism":("300111559","Pictorialist","AAT 只说明用于指19世纪的摄影运动，印证名称与所属媒介；本条目所写延续到20世纪初，AAT 未涉及。"),
 "documentary-photography":("300134547","documentary photography","AAT 定义为以事实准确与摄影者客观为重、常记录新闻事件、可意在记录并影响社会状况的摄影方法，与本条目定义相合，印证定义。"),
 "postmodern-architecture":("300022208","Postmodern","AAT 称其为1960年代以后挑战现代主义主导地位的艺术与建筑风格与时期，1970年代在建筑中广泛使用；与本条目“1960年代兴起”相合。AAT 另称该词1934年已由德奥尼斯使用，本条目未写。"),
 "brutalism":("300112048","Brutalist","AAT 称其依赖裸露粗混凝土为结构形式，尤指1960—1970年代，并与勒·柯布西耶晚期作品相关，词源为法语 béton brut。断代差异：本条目据摘要写1950年代起于英国，AAT 侧重1960—1970年代，两说并存，不改正文。"),
 "viol":("300042233","viols","AAT 描述为腰部内收、平背、指板有品、置于膝上或两腿间演奏的弓弦乐器，与本条目形制描述相合，只印证形制。"),
 "xiao":("300224132","xiao","AAT 描述为汉族竹制竖吹笛，一端开吹口，自古即有，指孔数目与排列不一，与本条目“单管竖吹”相合，只印证形制。"),
 "photography":("300054225","photography (process)","AAT 此词条指摄影这一工艺本身，不是摄影史，只作名称层面的有限印证。"),
}
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
n=0
for eid,(num,lab,note) in A.items():
    sid="aat-"+num
    if sid not in have:
        sd["sources"].append({"id":sid,"title":"Getty AAT — %s (%s)"%(lab,num),"author":"Getty Research Institute（Art & Architecture Thesaurus）","year":"2026",
            "url":"http://vocab.getty.edu/page/aat/"+num,"type":"权威主题词表","verified":True,
            "verified_note":"2026-11-25 经 AAT SPARQL 按首选标签“%s”精确查询命中，范围注释已读全"%lab}); have.add(sid)
    p=os.path.join(D,"l2",eid+".json"); j=json.load(open(p,encoding="utf-8"))
    j.setdefault("sources",[]); j["sources"]=list(dict.fromkeys(j["sources"]+[sid]))
    if TAG not in j["sections"]["待核实"]: j["sections"]["待核实"]+=TAG+"盖蒂 AAT（%s）：%s"%(num,note)
    head="已补 AAT 独立来源（只印证定义或形制）；"
    if not j.get("pending_notes","").startswith(head): j["pending_notes"]=head+j.get("pending_notes","")
    json.dump(j,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=2); n+=1
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("updated",n,"sources",len(sd["sources"]))
