import json
L3 = {
 "rembrandt": {
  "controversies": [
   {"issue": "伦勃朗作品总数应缩减到什么程度？",
    "views": [
     {"holder": "伦勃朗研究计划（Rembrandt Research Project，1960年代起，所引来源页 enc-rembrandt 所述）",
      "basis": "结合技术检测重新鉴定，将20世纪初所认定的600余幅油画缩减到近300幅，并剔除大量此前归属的作品。"},
     {"holder": "持异议的一方（所引来源页 enc-rembrandt 称这种缩减“常有争议”）",
      "basis": "部分被剔除的作品此后又被重新归回；素描方面有两位专家认为可确定为亲笔者不超过约75件，此说同样受到质疑。"}]},
   {"issue": "弗里克收藏馆《波兰骑士》是否为伦勃朗亲笔？",
    "views": [
     {"holder": "Josua Bruyn（伦勃朗研究计划，1980年代，所引来源页 enc-rembrandt 所述）",
      "basis": "谨慎地提出该画可能出自其学生威廉·德罗斯特（Willem Drost）之手；该页称此为少数意见，现已普遍不被接受。"},
     {"holder": "Simon Schama（1999年《伦勃朗的眼睛》）与 Ernst van de Wetering（1997年墨尔本研讨会）（所引来源页 enc-rembrandt 所述）",
      "basis": "主张归属伦勃朗本人；弗里克馆展签始终写“伦勃朗”。仍存疑的少数学者认为画面执行不均，倾向各部分分属不同作者。"}]}
  ],
  "data": [
   {"label": "20世纪初鉴赏家认定的油画数", "value": "600余幅", "note": "来源:enc-rembrandt"},
   {"label": "伦勃朗研究计划缩减后的油画数", "value": "近300幅", "note": "来源:enc-rembrandt"},
   {"label": "版画总数", "value": "略少于300件（较稳定）", "note": "来源:enc-rembrandt"},
   {"label": "自画像油画（今认定）", "value": "40余幅（旧时约90幅）", "note": "来源:enc-rembrandt"}
  ],
  "complex_diagram_note": "以柱状对照展示20世纪初与伦勃朗研究计划之后的油画、版画认定数量变化，并在旁注标出《波兰骑士》归属两说。"
 },
 "vermeer": {
  "controversies": [
   {"issue": "维米尔是否借助暗箱（camera obscura）等光学装置作画？",
    "views": [
     {"holder": "David Hockney 与 Charles M. Falco（2001年“霍克尼—法尔科论题”）、Philip Steadman（2001年《维米尔的暗箱》）、Tim Jenison（2008年起）（所引来源页 enc-vermeer 所述）",
      "basis": "画中珍珠般高光被认为是原始镜头的光晕；Steadman 发现六幅画尺寸恰与同一房间后墙暗箱成像相符；Jenison 以凹面镜加比对镜复制《音乐课》。"},
     {"holder": "不接受机械辅助说的一方（所引来源页 enc-vermeer 将此列为长期争论）",
      "basis": "直接证据有限：无确证出自维米尔的素描，准备性草图或描摹痕迹的证据也很少。"}]}
  ],
  "data": [
   {"label": "Thoré-Bürger 19世纪归属作品数", "value": "66件（其目录后称70余件）", "note": "来源:enc-vermeer"},
   {"label": "今公认作品数", "value": "34幅", "note": "来源:enc-vermeer"},
   {"label": "已检测出的颜料种数", "value": "约20种（常用7种主色）", "note": "来源:enc-vermeer"}
  ],
  "complex_diagram_note": "以时间轴展示归属数量从66件到34幅的收缩，并以并列框图对照暗箱说各论者的证据与反方指出的证据缺口。"
 },
 "beethoven": {
  "controversies": [
   {"issue": "“英雄风格”能否概括贝多芬中期？",
    "views": [
     {"holder": "沿用“英雄”时期说法的一方（所引来源页 enc-beethoven 所述）",
      "basis": "第三（英雄）、第五交响曲等作品易于以“英雄”描述，该词常被用作中期的别名。"},
     {"holder": "质疑该术语的贝多芬研究者（所引来源页 enc-beethoven 称其日益有争议）",
      "basis": "第六（田园）交响曲、第24号钢琴奏鸣曲等中期作品并不“英雄”，以一词概括整个时期不恰当。"}]},
   {"issue": "1812年“永恒的爱人”信的收信人是谁？",
    "views": [
     {"holder": "Maynard Solomon（所引来源页 enc-beethoven 所述）",
      "basis": "论证收信人为安东尼·布伦塔诺（Antonie Brentano）。"},
     {"holder": "其他候选说（所引来源页 enc-beethoven 所列）",
      "basis": "朱丽叶塔·圭恰迪、特蕾莎·马尔法蒂、埃尔德迪伯爵夫人、约瑟芬·布伦斯维克等均曾被提出。"}]}
  ],
  "data": [
   {"label": "“永恒的爱人”信写作年份与地点", "value": "1812年，特普利采", "note": "来源:enc-beethoven"},
   {"label": "信的篇幅", "value": "10页，未寄出", "note": "来源:enc-beethoven"},
   {"label": "中期所含交响曲", "value": "第3—8号", "note": "来源:enc-beethoven"}
  ],
  "complex_diagram_note": "以早、中、晚三期分栏展示代表作，并在中期栏旁注“英雄风格”术语之争与“永恒的爱人”候选人名单。"
 }
}
for k, v in L3.items():
    p = 'data/l2/%s.json' % k
    d = json.load(open(p, encoding='utf-8'))
    d['level'] = 'L3'; d['l3'] = v
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('ok', k)
