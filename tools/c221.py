import json, subprocess, sys, re
L3 = {
 "josquin": {
  "controversies": [
   {"issue": "若斯坎是否被不切实际地抬高为文艺复兴音乐的中心人物？",
    "views": [
     {"holder": "Edward Lowinsky 等（1964年论文、1971年国际若斯坎节暨研讨会、1976年专著，所引来源页 enc-josquin 所述）",
      "basis": "早期音乐复兴推动对若斯坎的再评价；1971年会议把他牢固确立在文艺复兴音乐的中心，Lowinsky 1976年专著进一步巩固。"},
     {"holder": "Richard Sherr 所述21世纪初的异议（所引来源页 enc-josquin 所述）",
      "basis": "2001年 Grove Music Online 所列归属作品不足200部（此前逾370部），用今已不归他的作品分析其风格的早期研究因此受损，传记也因同名者混淆被大幅改写；Sherr 的结论是其声誉略有下降，但凭最受推崇、归属最确定的作品，他仍是音乐史上的巨擘。"}]}
  ],
  "data": [
   {"label": "归属作品数（Grove 2001年）", "value": "不足200部（此前逾370部）", "note": "来源:enc-josquin"},
   {"label": "Osthoff 首部重要研究", "value": "第1卷1962年、第2卷1965年", "note": "来源:enc-josquin"},
   {"label": "国际若斯坎节暨研讨会", "value": "1971年", "note": "来源:enc-josquin"},
   {"label": "《新若斯坎全集》开始出版", "value": "1987年", "note": "来源:enc-josquin"}
  ],
  "complex_diagram_note": "以时间轴标出1962—1987年的研究与出版节点，并以柱状对照归属作品数从逾370部降至不足200部，旁注抬高与修正两方。"
 },
 "pollock": {
  "controversies": [
   {"issue": "波洛克的滴画是否有艺术价值？",
    "views": [
     {"holder": "批评者：Robert Coates、《雷诺兹新闻》1959年标题（所引来源页 enc-pollock 所述）",
      "basis": "Coates 讥其部分作品为“只是无组织的随机能量爆发，因而毫无意义”；《雷诺兹新闻》称“这不是艺术，是品味低劣的玩笑”。"},
     {"holder": "支持者：Jean Hélion、Clement Greenberg、Harold Rosenberg（所引来源页 enc-pollock 所述）",
      "basis": "Greenberg 从形式主义出发，视其为当时最好的绘画，是经塞尚、立体主义上溯马奈的西方传统的顶点；Rosenberg 1952年在 ARTnews 提出“行动绘画”，认为画布上发生的是事件而非图画。"}]},
   {"issue": "2003年温斯科特储物柜发现的24件波洛克风格作品是否为真迹？",
    "views": [
     {"holder": "俄勒冈大学研究者的分形分析（2005年应波洛克—克拉斯纳基金会要求，所引来源页 enc-pollock 所述）",
      "basis": "分析发现6幅受争议画作的图案与14幅确定真迹之间存在差异。"},
     {"holder": "Ellen G. Landau 与 Claude Cernuschi（2007年《Pollock Matters》，所引来源页 enc-pollock 所述）",
      "basis": "Landau 曾是1990年代基金会鉴定委员会成员，书中列出藏画家族与波洛克生前的诸多联系，以将这些画作放回她认为恰当的历史语境。"}]}
  ],
  "data": [
   {"label": "Rosenberg 提出“行动绘画”", "value": "1952年", "note": "来源:enc-pollock"},
   {"label": "温斯科特储物柜发现作品", "value": "2003年，24件", "note": "来源:enc-pollock"},
   {"label": "分形分析比对", "value": "2005年，6幅受争议作品对14幅确定真迹", "note": "来源:enc-pollock"},
   {"label": "《Pollock Matters》巡展与出版", "value": "2007年", "note": "来源:enc-pollock"}
  ],
  "complex_diagram_note": "以两栏并列评价之争（批评者与 Greenberg、Rosenberg）和真伪之争（分形分析与 Landau），下方时间轴标出1952、2003、2005、2007年节点。"
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
