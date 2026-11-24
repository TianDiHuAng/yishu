# -*- coding: utf-8 -*-
"""Cycle154：中国书法 4 条（祝允明草书 / 文徵明谢赐绣丝诗 / 越山道宗《吟风一样松》/ 梁启超对联）。来源 CMA。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-2025-192","Cleveland Museum of Art — Retreat on an Autumn Day, in Cursive Script, Zhu Yunming, 1523, acc. 2025.192",
  "https://openaccess-api.clevelandart.org/api/artworks/2025.192","2026-11-24 API HTTP 200；手卷 纸本墨 高34.3cm 书法段514.2cm；款识癸未（1523）七月晦日；含两首诗释文与脱字标注"),
 ("cma-1998-169","Cleveland Museum of Art — Poem on Imperial Gift of an Embroidered Silk, Wen Zhengming, c. 1525, acc. 1998.169",
  "https://openaccess-api.clevelandart.org/api/artworks/1998.169","2026-11-24 API HTTP 200；立轴 纸本墨 书法343.5×93.3cm；说明含嘉靖帝赐绣丝、大幅书法稀少、英译诗文"),
 ("cma-2003-354","Cleveland Museum of Art — Calligraphy in Semi-Cursive Style (xing-caoshu), Yueshan Daozong, c. 1660–1709, acc. 2003.354",
  "https://openaccess-api.clevelandart.org/api/artworks/2003.354","2026-11-24 API HTTP 200；立轴 纸本墨 画心128.9×29cm；款识吟風一樣松/悅山/道宗之印；说明含黄檗宗僧、寒山诗、暂译"),
 ("cma-2023-162","Cleveland Museum of Art — Calligraphy Couplet, Liang Qichao, after 1911, acc. 2023.162",
  "https://openaccess-api.clevelandart.org/api/artworks/2023.162","2026-11-24 API HTTP 200；对联一对 纸本墨 每幅128×30cm；说明含碑学风格、改革者、各引一位历史文化人物诗句"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('zhu-yunming-autumn-retreat','祝允明《闲居秋日》草书手卷（1523）','作品','art-china-calligraphy','明代','中国','书法','重要',
  '苏州祝允明草书手卷，书两首自作诗，克利夫兰艺术博物馆藏（2025.192）。','1523年',
  '该馆称这是祝允明的杰作：以草书写两首自作诗，笔法不拘、迅疾而凭直觉，力道之强使字溃解为点或线；自右向左、自上而下书写，墨色由淡干到浓饱交替，单字可占一整行或延入下一行，随笔势如在纸上舞动；款识为癸未（1523）七月晦日。',
  'cursive-script,china-calligraphy-history','cma-2025-192'),
 ('wen-zhengming-silk-poem','文徵明《谢赐绣丝诗》大幅行楷轴（约1525）','作品','art-china-calligraphy','明代','中国','书法','重要',
  '苏州文徵明行楷大轴，谢嘉靖帝赐绣丝，克利夫兰艺术博物馆藏（1998.169）。','约1525年',
  '诗作表达文徵明对嘉靖帝（在位1522—67）赐绣丝以嘉奖其勤勉服务的感谢；该馆称深黑墨写成的大字优雅、布局得当而有力，体现出一位杰出学者艺术家的手笔；文徵明这种大尺幅的书法作品很少见。',
  'running-script,regular-script','cma-1998-169'),
 ('yueshan-pine-wind-calligraphy','越山道宗《吟风一样松》行草轴（约1660—1709）','作品','art-china-calligraphy','清代','中国','书法','重要',
  '黄檗宗僧人越山道宗的行草立轴，五字取自《寒山诗》，克利夫兰艺术博物馆藏（2003.354）。','约1660—1709年',
  '该馆称这是黄檗宗僧人越山所书的雄健书法，五字暂译「松树在风中歌唱」，句出《寒山诗》；寒山既是诗僧的号，也是地名；一首诗里寒山写到在去寒山的路上迷失，或许暗指对觉悟的寻求；款识为「吟風一樣松」「悅山」「道宗之印」。',
  'yueshan-daizong-calligraphy,cursive-script','cma-2003-354'),
 ('liang-qichao-couplet','梁启超书法对联（1911年后）','作品','art-china-calligraphy','近现代','中国','书法','重要',
  '梁启超以碑学风格书写的对联，克利夫兰艺术博物馆藏（2023.162）。','1911年后',
  '该馆称：这位著名政治家与近代改革者以棱角分明、坚实而少有变化的楷书写成，灵感来自古代石碑上的刻字；这类书体在当时的改革者中流行，因为他们要复兴古代文化并在中国深厚的古代根基上建设新中国；两幅各引中国历史上一位文化人物的诗句。',
  'regular-script,china-calligraphy-history','cma-2023-162'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")
