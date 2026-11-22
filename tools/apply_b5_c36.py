# -*- coding: utf-8 -*-
"""Cycle36：把 B5 的 Wikidata 尝试结果写入两条目的"待核实"（不改正文、不改 when）。
1) romanesque：Wikidata Q46805 记 1000–1200，与本条目『约1000—1150』终点相差 50 年 → 登记差异，等第三来源。
2) cursive-script：Wikidata Q717343 张旭 生年 670 → 仅登记备查；其作品名称仍待核。
其余 3 项（realism 年代、donatello 术语、草书年代）Wikidata 无可用信息，维持待核。"""
import json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LD=os.path.join(ROOT,"data","l2")
N1=("【已复核·Wikidata】断代差异：Wikidata 实体 Romanesque art（Q46805）记起始 1000 年、终止 1200 年；"
    "本条目正文采『约1000—1150』，终点相差 50 年，且 1150 这一终点源自早期种子、未获独立来源支撑。"
    "处置：**不据单一结构化来源改动正文**，差异登记于此，待第三来源（专著/博物馆资料）判定后再定。")
N2=("【已复核·Wikidata】张旭生年：Wikidata 实体 Zhang Xu（Q717343，描述为 Chinese calligrapher）记生年 670 年。"
    "本条目不据此改写任何年份（单一结构化来源），仅登记备查；其具体作品名称仍未获可核验来源，维持待核。")
for eid,note,mark in [("romanesque",N1,"断代差异"),("cursive-script",N2,"张旭生年")]:
    p=os.path.join(LD,eid+".json"); o=json.load(open(p,encoding="utf-8"))
    pend=o["sections"]["待核实"]
    if mark not in pend:
        o["sections"]["待核实"]=pend+" "+note
        json.dump(o,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
        print("updated",eid)
print("done")