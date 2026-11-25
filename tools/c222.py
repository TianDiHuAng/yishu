import json, subprocess, sys, re
L3 = {
 "giotto": {
  "controversies": [
   {"issue": "阿西西圣方济各上堂《圣方济各生平》壁画组是否出自乔托？",
    "views": [
     {"holder": "归属乔托的一方（所引来源页 enc-giotto 所述）",
      "basis": "乔托约1297年的板上画《圣方济各领受圣痕》用了圣人撑住将倾教堂的母题，该母题此前见于阿西西壁画；在缺乏反证时，上堂中凡非明显出自契马布埃之手的壁画都被归给名气更大的乔托。"},
     {"holder": "Millard Meiss 与 Leonetto Tintori（1960年代，所引来源页 enc-giotto 所述）",
      "basis": "检查全部阿西西壁画，发现部分颜料含铅白，契马布埃约1283年严重损坏的《十字架》也用此材料，而已知乔托作品中都没有；方济各会相关委托文书已被拿破仑军队毁掉，无法以文献定案。"}]}
  ],
  "data": [
   {"label": "契马布埃《十字架》（含铅白）", "value": "约1283年", "note": "来源:enc-giotto"},
   {"label": "新圣母大殿悬挂《十字架》（高约5米）", "value": "约1290年", "note": "来源:enc-giotto"},
   {"label": "《圣方济各领受圣痕》板上画", "value": "约1297年", "note": "来源:enc-giotto"},
   {"label": "Meiss 与 Tintori 检查阿西西壁画", "value": "1960年代", "note": "来源:enc-giotto"}
  ],
  "complex_diagram_note": "以证据对照图并列两方：左侧为母题重现与传统归属，右侧为铅白颜料检测与文献毁失，下方时间轴标出约1283、约1290、约1297年与1960年代检测。"
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
print('\n'.join(l for l in out.splitlines() if l.startswith('  [')))
