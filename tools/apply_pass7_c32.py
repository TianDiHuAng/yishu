# -*- coding: utf-8 -*-
"""Cycle32：中国专题别名检索结果——采纳 4 条，拒绝 11 条（逐条写明口径理由）。"""
import json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")
ADOPT={"ming-painting":"Q6864640","xieyi":"Q10894988",
       "china-music-history":"Q277393","pipa":"Q6685124"}
REJECT={
 "tang-painting":"Q7682682『Tang dynasty art』是唐代整体艺术，比条目（唐代绘画）宽",
 "song-painting":"仅有《宋代绘画及其对日本艺术的影响》等论文，无『宋代绘画』实体",
 "yuan-painting":"仅有『元代绘画史工具书简介』等论文，无实体",
 "qing-painting":"仅有『清代绘画集锦册』（一件藏品）与论文，无体裁级实体",
 "china-painting-history":"仅有『中国绘画史方法论』等论文，无学科/通史实体",
 "yangshao-painted-pottery":"Q854631『Yangshao culture』是考古学文化，比条目（仰韶彩陶）宽",
 "chinese-jade-art":"Q175089『jade』为材质、Q60733799『Jade objects』为泛玉器，均非『中国玉器』",
 "shang-zhou-bronzes":"Q4390114『bronze object』为材质门类；Q917520 是铭文，口径不同",
 "dunhuang-art":"Q43286『Mogao Caves』是石窟遗址，条目为『敦煌艺术』（壁画/彩塑总体），口径不同",
 "six-dynasties-art":"Q836465 是『魏晋南北朝』历史时期，不是艺术实体",
 "wuwangdu-chu-music-archaeology":"Q126007958 是『武王墩墓』遗址，条目为考古研究进展，口径不同",
}
cand=json.load(open(os.path.join(ROOT,"reports","entity_pass7_c32.json"),encoding="utf-8"))
look={}
for eid,cs in cand.items():
    for c in cs:
        look.setdefault((eid,c["qid"]),c)
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
es={e["id"]:e for e in json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]}
rows=[]
for eid,qid in ADOPT.items():
    c=look.get((eid,qid),{})
    label=c.get("label") or eid; desc=(c.get("desc") or "")[:60]
    sid="wd-anchor-%s"%eid
    if sid not in have:
        sd["sources"].append({"id":sid,"title":"Wikidata 实体（身份锚点）：%s（%s）"%(label,qid),
            "author":"Wikimedia Foundation（Wikidata 社区维护）","year":"2026",
            "url":"https://www.wikidata.org/wiki/%s"%qid,"type":"权威结构化数据（身份锚点）","verified":True,
            "verified_note":"Cycle32 中文别名检索 + 逐条核对口径后采纳；仅作身份锚点，不作事实依据"})
        have.add(sid)
    p=os.path.join(LD,eid+".json")
    o=json.load(open(p,encoding="utf-8")) if os.path.exists(p) else {"id":eid}
    o["sources"]=list(dict.fromkeys((o.get("sources") or es[eid].get("sources",[]))+[sid]))
    json.dump(o,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    rows.append("| %s | %s | %s | %s |"%(eid,label,qid,desc))
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
md=["# Cycle32 中国专题别名锚定（人工确认）","","采纳 **%d** 条："%len(ADOPT),"",
    "| 条目 id | 实体标签 | QID | 描述 |","|---|---|---|---|"]+rows+["","## 已拒绝（%d 条，逐条口径说明）"%len(REJECT),""]
for k,v in REJECT.items(): md.append("- **%s**：%s"%(k,v))
open(os.path.join(ROOT,"reports","entity_pass7_vetted.md"),"w",encoding="utf-8").write("\n".join(md))
print("adopted",len(ADOPT),"rejected",len(REJECT),"sources",len(sd["sources"]))