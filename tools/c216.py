import json, subprocess, sys, re
L3 = {
 "caravaggio": {
  "controversies": [
   {"issue": "卡拉瓦乔1610年死于何因？",
    "views": [
     {"holder": "病亡说（所引来源页 enc-caravaggio 所述：传统史家主梅毒，另有学者主疟疾或布鲁氏菌病；2010年遗骸检测初步提出铅中毒）",
      "basis": "其死时发烧；2010年考古团队用DNA与碳测年认定遗骸，初步检测显示可能铅中毒（当时颜料含大量铅盐）。"},
     {"holder": "遇害说（所引来源页 enc-caravaggio 所述：当时传言及部分学者）",
      "basis": "当时传言称托马索尼家族或马耳他骑士团为复仇杀害了他；部分学者认为是他逃离马耳他后一直追杀他的“仇人”（可能是维尼亚库尔或骑士团派系）所为。"}]},
   {"issue": "卡拉瓦乔作品中的同性情欲意涵能否用来理解其人？",
    "views": [
     {"holder": "Howard Hibbard 等（1970年代起，所引来源页 enc-caravaggio 所述）",
      "basis": "其一生未画一幅女性裸体，德尔蒙特时期的小幅画满是“丰唇、慵懒的少年”，暗示对男性形体的情欲兴趣；《胜利的爱神》模特切科曾与他同住。"},
     {"holder": "持保留者（所引来源页 enc-caravaggio 所述，含 Andrew Graham-Dixon 的概括）",
      "basis": "Graham-Dixon 指出此前一些传记把他假定的同性恋当作解释一切的“唯一钥匙”；另有1605年证词提到“米开朗琪罗的女人”莉娜，及他与菲利德·梅兰德罗尼的传闻。"}]}
  ],
  "data": [
   {"label": "卒年与地点", "value": "1610年，埃尔科莱港（Porto Ercole）", "note": "来源:enc-caravaggio"},
   {"label": "遗骸迁至圣伊拉斯谟墓地", "value": "1956年", "note": "来源:enc-caravaggio"},
   {"label": "遗骸鉴定调查", "value": "2010年，历时一年", "note": "来源:enc-caravaggio"}
  ],
  "complex_diagram_note": "以分支图并列死因诸说（梅毒、疟疾/布鲁氏菌病、铅中毒、遇害）及各自依据，旁注2010年遗骸鉴定的时间节点。"
 },
 "gregorian-chant": {
  "controversies": [
   {"issue": "格里高利圣咏的节奏应如何复原？",
    "views": [
     {"holder": "量化节拍派：Peter Wagner、Jammers、Lipphardt（所引来源页 enc-gregorian-chant 所述）",
      "basis": "主张给圣咏加上节拍格律，但彼此对怎样加并不一致。"},
     {"holder": "自由节奏派：Pothier、Mocquereau（索莱姆，所引来源页 enc-gregorian-chant 所述）",
      "basis": "主张音值大致相等的自由节奏，仅因歌词强调或音乐原因延长部分音；该页另称索莱姆编者在节奏上的处理引发严肃学术争论。"}]}
  ],
  "data": [
   {"label": "五线谱线的引入（传归圭多·达雷佐）", "value": "11世纪初", "note": "来源:enc-gregorian-chant"},
   {"label": "方形记谱普及、各音大致等值", "value": "13世纪", "note": "来源:enc-gregorian-chant"},
   {"label": "《美第奇版》（Editio medicaea）", "value": "1614年", "note": "来源:enc-gregorian-chant"}
  ],
  "complex_diagram_note": "以时间轴展示纽姆谱、11世纪谱线、13世纪方形记谱、1614年美第奇版到19世纪末复原研究，并在末端分叉标出量化节拍派与自由节奏派。"
 },
 "mozart": {
  "controversies": [
   {"issue": "莫扎特书信中的粗俗内容能否说明其精神异常？",
    "views": [
     {"holder": "部分学者（所引来源页 enc-mozart 所述）",
      "basis": "根据莫扎特书信推测其有某种精神障碍。"},
     {"holder": "另一些学者（所引来源页 enc-mozart 所述）",
      "basis": "指出当时当地（包括其家人）屎尿类幽默更为普遍，不宜据此作病理推断。"}]},
   {"issue": "莫扎特临终之病是长期衰退还是突然发作？",
    "views": [
     {"holder": "长期衰退说（所引来源页 enc-mozart 所述）",
      "basis": "认为病情早已开始，经历了漫长而消沉的衰退期。"},
     {"holder": "突发说（所引来源页 enc-mozart 所述）",
      "basis": "认为1791年11月20日起病是突然的；所引来源页称此为“严重争议”，未列出各方具体论者。"}]}
  ],
  "data": [
   {"label": "卧床起病", "value": "1791年11月20日", "note": "来源:enc-mozart"},
   {"label": "去世", "value": "1791年12月5日凌晨0:55，35岁", "note": "来源:enc-mozart"},
   {"label": "下葬", "value": "1791年12月7日，圣马克斯墓地", "note": "来源:enc-mozart"}
  ],
  "complex_diagram_note": "以1791年11—12月日程图标出起病、去世、下葬三点，并以并列框对照长期衰退说与突发说。"
 }
}
for k, v in L3.items():
    p = 'data/l2/%s.json' % k
    d = json.load(open(p, encoding='utf-8')); d['level'] = 'L3'; d['l3'] = v
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
subprocess.run([sys.executable, 'tools/merge_l2.py'], capture_output=True)
out = subprocess.run([sys.executable, 'tools/check.py'], capture_output=True, text=True, encoding='utf-8').stdout
bad = set(re.findall(r'\[R7\] ([\w-]+): 非核心', out))
for k in bad:
    p = 'data/l2/%s.json' % k
    d = json.load(open(p, encoding='utf-8')); d['level'] = 'L2'; d.pop('l3', None)
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('reverted(non-core):', sorted(bad)); print('kept:', sorted(set(L3) - bad))
