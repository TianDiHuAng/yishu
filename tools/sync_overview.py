# -*- coding: utf-8 -*-
"""复检返工补充：同步覆盖 L1 seed 的 overview/when，使首页卡片与正文一致。"""
import json, os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data","l2")
def upd(eid, **kw):
    p=os.path.join(D,eid+".json")
    o=json.load(open(p,encoding="utf-8")); o.update(kw)
    json.dump(o,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
upd("gothic", overview="以尖拱与彩色玻璃窗著称的中世纪晚期风格，12世纪后期兴起于法国并传遍欧洲；肋拱、飞扶壁等具体结构术语因来源不足列入待核实。")
upd("greek-art", when="约公元前900—前146年",
    overview="雕塑从古风时期的程式化青年像发展到古典时期的理想人体，建筑形成多立克、爱奥尼、科林斯三柱式；断代终点采来源明确记载的前146年。")
print("overview synced")
