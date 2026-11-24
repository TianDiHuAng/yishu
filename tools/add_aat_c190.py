# -*- coding: utf-8 -*-
"""Cycle190：给24个风格/术语条目追加盖蒂 AAT 来源。写入前按标签重查，编号必须一致才写；不改 when、不改正文。"""
import json,os,sys,time
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from probe_aat_c190 import q
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)));D=os.path.join(ROOT,"data")
AAT="https://vocab.getty.edu/aat/";TAG="（AAT 对照，2026-11-24）"
M={
 'gothic':('300020775','Gothic (Medieval)','AAT：12世纪中叶始于法国北部，此后百年传遍西欧，在各地不同时间演变为文艺复兴。与本条目（约1140—1500年，西欧）相容。'),
 'neoclassicism':('300021477','Neoclassical','AAT：18世纪中叶至19世纪中叶欧美的建筑与美术、装饰艺术风格，受地中海与近东考古发现启发，模仿希腊罗马形式，被视为对洛可可的反动。与本条目（约1750—1850年）一致。'),
 'fauvism':('300021300','Fauve','AAT：与一群法国青年画家相关，年代约1898—1906年，以大胆鲜亮色彩为特征。与本条目的差异：本条目 when 为约1905—1908年，AAT 起止都更早。口径不同，本条目不裁决，保持原 when。'),
 'conceptual-art':('300264827','Conceptual','AAT：泛指1960—1970年代的艺术，强调传达观念与艺术家意图而非制作物品，并批判艺术作为商品。本条目 when 写“1960年代—至今”，AAT 这个风格词条只覆盖到1970年代（更早或更宽的观念性艺术另有词条），终点不同，保持原 when。'),
 'abstract-expressionism':('300022099','Abstract Expressionist','AAT：美国绘画运动，主要以纽约为中心，兴盛于1940—1950年代。与本条目一致。'),
 'romanesque':('300020768','Romanesque','AAT：11—12世纪西欧最显著的风格与时期，以圆拱、砌石拱顶、巨大体量为特征。与本条目一致。'),
 'early-christian-art':('300020665','Early Christian','AAT：艺术上一般指3世纪至9世纪中叶意大利与西地中海的艺术。与本条目的差异：本条目 when 为约2—6世纪，AAT 起点晚约一个世纪、终点晚约三个世纪。口径不同，保持原 when。'),
 'art-deco':('300021426','Art Deco','AAT：以建筑与装饰艺术为主，1920—1930年代在欧美广泛传播，1925年巴黎装饰艺术博览会后流行。本条目 when 起点写1910年代，比 AAT 早；保持原 when。'),
 'ukiyo-e':('300106769','Ukiyo-e','AAT：绘画等媒介中的独特类型，以木版画最突出，兴起于江户时代（1600—1868），面向中产阶层市场。与本条目（约17—19世纪，日本）一致。'),
 'northern-renaissance':('300252246','Northern Renaissance','AAT：指文艺复兴在15世纪晚期由意大利传入北欧后的艺术与建筑风格。与本条目的差异：本条目 when 起点为约1400年，AAT 起点为15世纪晚期。AAT 偏重“意大利风格北传”，而本条目包含早期尼德兰绘画，口径不同，保持原 when。'),
 'high-renaissance':('300021142','High Renaissance','AAT：主要在15世纪最后十年发展于佛罗伦萨与罗马，一般认为随1520年代风格主义出现而结束。与本条目（约1490—1527年）一致。'),
 'early-renaissance':('300021141','Early Renaissance','AAT：14世纪中晚期在意大利中部发展，15世纪早中期传遍半岛与北欧。本条目 when 起点为约1400年，AAT 起点更早（14世纪中晚期），口径略有出入，保持原 when。'),
 'gothic-revival-architecture':('300021452','Gothic Revival','AAT：以追求历史准确地再现哥特元素为特征的建筑与装饰艺术风格，在英美最重要的时期为18世纪中叶至19世纪中叶。本条目 when 为17世纪下半叶—19世纪末，范围更宽；保持原 when。'),
 'modern-architecture':('300021474','Modernist','AAT：20世纪一系列前卫艺术与建筑运动，是对社会现代性的反应，1970年代起被后现代主义取代。该词条跨门类且很宽泛，只能印证本条目“20世纪”的大致范围，不能印证具体建筑史叙述。'),
 'mughal-architecture':('300018939','Mughal','AAT：莫卧儿皇帝统治下印度北部与中部的文化、时期与风格，16世纪中叶至17世纪晚期，特征为伊斯兰建筑复兴与波斯、印度本土影响交融。本条目 when 延至18世纪，比 AAT 晚；保持原 when。该词条是文化/时期总称，不专指建筑。'),
 'khmer-art':('300386546','Khmer','AAT：古代高棉人的文化与风格。摘录主要是民族与迁徙史，未给出艺术断代，只能印证“高棉”这一文化归属，不能印证本条目 when（约9—15世纪）。'),
 'xieyi':('300310141','xieyi','AAT：中国画中以写意、放笔为之的方法，通常用墨。与本条目一致。'),
 'gongbi':('300310140','gongbi','AAT：中国画技法，用笔工细、注重细节与法度，通常用于设色画。与本条目一致。'),
 'violin':('300042215','violins','AAT：提琴族的高音成员，形制为空腔共鸣箱、内收腰、拱形面背板、两个 f 孔与四根弦。只印证形制，不含年代与沿革。'),
 'piano':('300042909','pianos','AAT：带键盘的类齐特拉弦鸣乐器，以琴键控制的回弹击槌敲弦发声。只印证发声原理，不含年代与沿革。'),
 'seal-script':('300343588','seal script','AAT：一般指汉代隶书之前的中国古文字书体，包括大篆与小篆，秦统一后由李斯主持统一。与本条目相容。注意：AAT 摘录把秦统一写为公元前211年，通行年份是前221年，属 AAT 自身笔误，本条目不采用。'),
 'clerical-script':('300343578','clerical script','AAT：汉代发展并广泛用于公文与教育的书体，由篆书演变而来，萌芽于周末与秦的毛笔书写。与本条目（汉代）一致。注意：AAT 摘录中“秦（221-226 BCE）”“东汉（late 3rd century BCE）”等年代明显有误，本条目不采用这些年代。'),
 'running-script':('300343585','running script','AAT：半草书体，与楷书同期（公元1—3世纪）从汉代隶书发展而来，字内笔画常连写。与本条目（约2世纪—至今）相容。'),
 'music-notation':('300417622','musical notation','AAT：以文字或标准符号视觉化表示音乐的各种系统的总称。只印证定义，不含年代与沿革。'),
}
bad=[]
for eid,(num,label,_) in M.items():
    try: ids=[r[0] for r in q(label)]
    except Exception as e: ids=['ERR '+str(e)[:50]]
    ok=num in ids; print(eid,num,'OK' if ok else 'MISMATCH %s'%ids)
    if not ok: bad.append(eid)
    time.sleep(0.4)
if bad: raise SystemExit('核对不通过，未写入: %s'%bad)
sp=os.path.join(D,"sources.json");sd=json.load(open(sp,encoding="utf-8"));have={s["id"] for s in sd["sources"]}
for eid,(num,label,_) in M.items():
    sid="aat-"+num
    if sid not in have:
        sd["sources"].append({"id":sid,"title":"Getty AAT — %s, %s"%(label,num),"author":"J. Paul Getty Trust（Art & Architecture Thesaurus，开放词表）","year":"2026","url":AAT+num,"type":"权威机构词表（术语定义）","verified":True,
          "verified_note":"2026-11-24 经 vocab.getty.edu SPARQL 接口取回该术语的英文定义（scopeNote），编号与标签匹配；原文存档于 tmp/aat_c190.json"});have.add(sid)
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2);print("sources:",len(sd["sources"]))
for eid,(num,label,note) in M.items():
    p=os.path.join(D,"l2",eid+".json");j=json.load(open(p,encoding="utf-8"));sid="aat-"+num
    j.setdefault("sources",[])
    if sid not in j["sources"]: j["sources"].append(sid)
    t=j["sections"].get("待核实","")
    if TAG not in t: j["sections"]["待核实"]=t+TAG+note
    json.dump(j,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("l2 updated",len(M))
