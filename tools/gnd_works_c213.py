# -*- coding: utf-8 -*-
"""Cycle213：用 GND 音乐作品规范记录核对作曲家条目里已点名的代表作，并给出创作年代。
匹配：作品记录的 firstComposer 必须是该作曲家的 GND 编号，且标目与给定原题精确相等（不做模糊匹配）。
只在条目“待核实”里追加对照说明，并把作品记录登记为来源；不改正文。用法：python tools/gnd_works_c213.py [probe|apply]"""
import json,os,subprocess,sys,time,urllib.parse
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
UA="YishuBot/1.0 (educational art-history knowledge base)"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
# 条目id -> [(GND 标目原题, 条目中的中文名)]；只列条目正文里已经点名的作品
W={
 "bartok":[("A csodálatos mandarin","《神奇的满大人》"),("A kékszakállú herceg vára","《蓝胡子城堡》"),("Concerto for orchestra","《乐队协奏曲》"),("Music for strings, percussion and celesta","《为弦乐、打击乐与钢片琴而作的音乐》")],
 "prokofiev":[("Petja i volk","《彼得与狼》"),("Romeo i Džul'etta","《罗密欧与朱丽叶》"),("Poručik Kiže","《基热中尉》"),("Ljubov' k trem apel'sinam","《三橘爱》")],
 "mendelssohn":[("Elias","《以利亚》"),("Paulus","《圣保罗》"),("Die Hebriden","《赫布里底群岛》序曲"),("Ein Sommernachtstraum","《仲夏夜之梦》")],
 "berlioz":[("Symphonie fantastique","《幻想交响曲》"),("Harold en Italie","《哈罗尔德在意大利》"),("Les Troyens","《特洛伊人》"),("La damnation de Faust","《浮士德的天谴》"),("Benvenuto Cellini","《本韦努托·切利尼》"),("Béatrice et Bénédict","《比阿特丽斯与贝内迪克》"),("L'enfance du Christ","《基督的童年》")],
 "smetana":[("Prodaná nevěsta","《被出卖的新嫁娘》"),("Má vlast","《我的祖国》"),("Vltava","《伏尔塔瓦河》")],
 "sibelius":[("Finlandia","《芬兰颂》"),("Kullervo","《库勒沃》"),("Valse triste","《悲伤圆舞曲》"),("Karelia-Suite","《卡累利阿组曲》")],
 "ravel":[("Boléro","《波莱罗》")],
 "shostakovich":[("Ledi Makbet Mcenskogo uezda","《姆钦斯克县的麦克白夫人》")],
 "verdi":[("Nabucco","《纳布科》")],
 "rachmaninoff":[("Aleko","《阿列科》")],
 "stravinsky":[("Vesna svjaščennaja","《春之祭》")],
 "schoenberg":[("A survivor from Warsaw","《华沙幸存者》")],
}
def probe():
    H=json.load(open(os.path.join(ROOT,"tmp","gnd_c210.json"),encoding="utf-8"))
    out={}
    for eid,works in W.items():
        if eid not in H: print("no composer gnd",eid); continue
        cg=H[eid]["gnd"]
        for title,zh in works:
            q='firstComposer.id:"https://d-nb.info/gnd/%s" AND preferredName:"%s"'%(cg,title)
            d=get("https://lobid.org/gnd/search?q=%s&filter=type:MusicalWork&format=json&size=10"%urllib.parse.quote(q))
            hit=None
            for m in (d or {}).get("member",[]):
                if m.get("preferredName","").strip().lower()==title.lower(): hit=m;break
            if hit:
                rec={"gnd":hit["gndIdentifier"],"name":hit["preferredName"],"date":(hit.get("dateOfProduction") or [None])[0],"zh":zh,"composer":cg}
                out.setdefault(eid,[]).append(rec); print("HIT ",eid,zh,rec["gnd"],rec["name"],rec["date"])
            else:
                print("miss",eid,zh,title,[m.get("preferredName") for m in (d or {}).get("member",[])][:3])
            time.sleep(0.3)
    json.dump(out,open(os.path.join(ROOT,"tmp","gnd_works_c213_hits.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print("hits",sum(len(v) for v in out.values()))
def apply():
    out=json.load(open(os.path.join(ROOT,"tmp","gnd_works_c213_hits.json"),encoding="utf-8"))
    sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
    n=0
    for eid,recs in out.items():
        p=os.path.join(D,"l2",eid+".json"); j=json.load(open(p,encoding="utf-8"))
        parts=[]
        for r in recs:
            sid="gnd-"+r["gnd"].lower()
            if sid not in have:
                sd["sources"].append({"id":sid,"title":"GND — %s（作品）, %s"%(r["name"],r["gnd"]),"author":"Deutsche Nationalbibliothek（Gemeinsame Normdatei，经 lobid.org）","year":"2026",
                    "url":"https://d-nb.info/gnd/"+r["gnd"],"type":"国家图书馆作品规范记录（标目、作曲者、创作年代）","verified":True,
                    "verified_note":"2026-11-25 经 lobid.org 取回；firstComposer 为 GND %s，标目“%s”精确匹配，创作年代 %s"%(r["composer"],r["name"],r["date"] or "未载")})
                have.add(sid)
            j["sources"]=list(dict.fromkeys(j.get("sources",[])+[sid]))
            parts.append("%s（GND 标目“%s”，%s）"%(r["zh"],r["name"],("创作年代 "+r["date"]) if r["date"] else "未载年代"))
        note="（GND 作品对照，2026-11-25）德国国家图书馆规范档有本条目所列作品的作品记录，作曲者与本人记录一致："+"；".join(parts)+"。这些记录只印证作品归属与年代，不印证条目其余内容。"
        if "（GND 作品对照，2026-11-25）" not in j["sections"]["待核实"]: j["sections"]["待核实"]+=note
        json.dump(j,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=2); n+=1
    json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
    print("entries updated",n,"sources",len(sd["sources"]))
if __name__=="__main__":
    {"probe":probe,"apply":apply}[sys.argv[1]]()
