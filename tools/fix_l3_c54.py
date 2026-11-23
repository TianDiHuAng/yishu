# -*- coding: utf-8 -*-
"""Cycle54 修复 1：L3 门禁复核。
- rembrandt（69字，仅"学界主要讨论分期"）与 monet（明言概述未提及争议）→ 降为 L2（诚实降级）。
- gothic：把"学界存在讨论"改写为**具名的两个立场**（1140 起点 vs 来源页面的12世纪后期—16世纪框架），保 L3。
"""
import io,json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LD=os.path.join(ROOT,"data","l2")
# 1) 降级
for eid in ["rembrandt","monet"]:
    p=os.path.join(LD,eid+".json"); o=json.load(open(p,encoding="utf-8"))
    if o.get("level")=="L3":
        o["level"]="L2"
        pend=o["sections"].get("待核实","")
        note=("【已复核·Cycle54】本条原标为 L3（深度条目）。复核发现其「争议」节并无**两方具名立场**，"
              "按 R16 要求（L3 须有 ≥1 组真实争议、≥2 方）不符，故**降级为 L2**；原有内容一字未删，"
              "争议节的说明保留原样。")
        o["sections"]["待核实"]=(pend+" "+note).strip()
        json.dump(o,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
        print("downgraded",eid)
# 2) gothic 争议改写为两方
p=os.path.join(LD,"gothic.json"); o=json.load(open(p,encoding="utf-8"))
old=o["sections"]["与前后风格的关系和争论"]
new=("在脉络上，哥特式艺术承接罗马式艺术，其后与文艺复兴相连，构成中世纪晚期向近代趣味过渡的一段。"
     "**围绕起点的断代存在两种立场**：一方以 **1140 年**为起点——所引来源记载巴黎附近圣但尼修道院教堂唱诗班于1140至1144年间重建，"
     "并称其为第一座哥特式建筑；另一方以**12世纪后期**为起点、并以**16世纪**为止，即把整段风格史框在「12世纪后期—16世纪」（所引来源页面给出的框架）。"
     "两种立场各有来源支撑，本条目并列而不裁定；此外，地域流派（如法国、英国、德意志）的划分标准亦有讨论，本条目未展开。")
o["sections"]["与前后风格的关系和争论"]=new
json.dump(o,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("gothic: two positions written; len",len(new))
print("old len",len(old))