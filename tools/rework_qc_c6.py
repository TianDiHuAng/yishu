# -*- coding: utf-8 -*-
"""Cycle6 质量闸返工：R17 判定为"编辑待办冒充学术争议"的22个条目降级回 L2（移除 l3 块）；
保留6个真实争议条目（greek-art/gothic/rembrandt/impressionism/monet/baroque-music）。
同时为 starry-night 的待核实补一条关于 enc-moma 佐证力偏弱的诚实说明。"""
import json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LD=os.path.join(ROOT,"data","l2")
DROP=['renaissance','leonardo','michelangelo','baroque','caravaggio','neoclassicism','romanticism-art',
      'post-impressionism','van-gogh','cezanne','expressionism','cubism','surrealism','abstract-expressionism',
      'picasso','contemporary-art','song-painting','china-calligraphy-history','opera','beethoven','stravinsky','schoenberg']
n=0
for eid in DROP:
    p=os.path.join(LD,eid+".json")
    if not os.path.exists(p): print("missing",eid); continue
    o=json.load(open(p,encoding="utf-8"))
    o["level"]="L2"
    o.pop("l3",None)
    json.dump(o,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    n+=1
print("downgraded to L2:",n)
# starry-night 诚实说明
p=os.path.join(LD,"starry-night.json")
o=json.load(open(p,encoding="utf-8"))
note="（5）关于馆藏佐证：所引 enc-moma 为维基「现代艺术博物馆」机构词条，只能佐证该馆存在与所在地，不能直接佐证本作品的馆藏登记；收藏地表述目前依据作品条目自身与其来源，馆藏编号与入藏年份待馆方页面核实。"
if "馆藏佐证" not in o["sections"]["待核实"]:
    o["sections"]["待核实"]+=" "+note
    json.dump(o,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("starry-night disclosure updated")