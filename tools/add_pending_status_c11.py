# -*- coding: utf-8 -*-
"""Cycle11（本地）：为同时含"原待核项 + 【已复核】结论"的15个条目加状态说明，
消除"既说待核又给出结论"的阅读矛盾（保留原文留痕，不删改既有内容）。"""
import json,glob,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LD=os.path.join(ROOT,"data","l2")
HEAD="状态说明：本页先列出写作时的原待核项（保留原文以留存修订痕迹），其后【已复核】各条为后续复核找到的第二来源与结论；两者并存不表示矛盾，以【已复核】为准。 "
n=0
for p in sorted(glob.glob(os.path.join(LD,"*.json"))):
    o=json.load(open(p,encoding="utf-8"))
    pend=o.get("sections",{}).get("待核实","")
    if "【已复核】" in pend and not pend.startswith("状态说明"):
        o["sections"]["待核实"]=HEAD+pend
        json.dump(o,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
        n+=1
print("status header added:",n)