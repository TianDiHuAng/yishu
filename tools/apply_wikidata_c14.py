# -*- coding: utf-8 -*-
"""Cycle14：把 Wikidata 核验结果写入 sources.json 与 5 个作品档案条目的"待核实"（留痕式补记）。
不修改正文断言；只把"作者/收藏地"由 Wikidata 结构化数据确认的部分记为【已复核】。
对 Q206015 的 P170 异常（标签为西德尼·諾蘭而非斯特拉文斯基）如实记录为数据问题，不采信该字段。"""
import json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")
rep={x["entry_id"]:x["accepted"] for x in json.load(open(os.path.join(ROOT,"reports","wikidata_verify.json"),encoding="utf-8"))}
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8"))
have={s["id"] for s in sd["sources"]}

def add_source(sid,title,qid):
    if sid in have: return sid
    sd["sources"].append({"id":sid,"title":title,"author":"Wikimedia Foundation（Wikidata 社区维护）",
        "year":"2026","url":"https://www.wikidata.org/wiki/%s"%qid,"type":"权威结构化数据",
        "verified":True,"verified_note":"Cycle14 API 读取 EntityData 成功（HTTP200 JSON），并按标题/类型/作者三重消歧"})
    have.add(sid); return sid

NOTES={
 "starry-night":("星夜","wd-starry-night"),
 "birth-of-venus-work":("维纳斯的诞生","wd-birth-of-venus"),
 "sistine-ceiling-work":("西斯廷礼拜堂天顶画","wd-sistine-ceiling"),
 "guernica-work":("格尔尼卡","wd-guernica"),
 "rite-of-spring-work":("春之祭","wd-rite-of-spring"),
}
for eid,(cn,sid) in NOTES.items():
    acc=rep.get(eid)
    if not acc: print("skip no-accept",eid); continue
    add_source(sid,"Wikidata: %s (%s)"%(acc["labels"].get("en",cn),acc["qid"]),acc["qid"])
    p=os.path.join(LD,eid+".json"); o=json.load(open(p,encoding="utf-8"))
    if sid not in o.get("sources",[]): o.setdefault("sources",[]).append(sid)
    coll="、".join(acc["collection"]) if acc["collection"] else "（Wikidata 未列收藏机构）"
    cr="、".join(acc["creator"]) if acc["creator"] else "（未列）"
    line="【已复核·Wikidata】作者与收藏：第二来源 %s（https://www.wikidata.org/wiki/%s），据其结构化数据：作者=%s；收藏=%s。"%(
        sid,acc["qid"],cr,coll)
    if eid=="rite-of-spring-work":
        line+=" 注：该条目 P170（作者）字段标签为「西德尼·諾蘭」，与实际作品（描述明确为 Igor Stravinsky 的芭蕾音乐）不符，属 Wikidata 数据异常，本条**不采信该字段**，作者仍以原来源为准。"
    pend=o["sections"]["待核实"]
    if "【已复核·Wikidata】" not in pend:
        o["sections"]["待核实"]=pend+" "+line
        json.dump(o,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources now",len(sd["sources"]),"verified",sum(1 for s in sd["sources"] if s["verified"]))