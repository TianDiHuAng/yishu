import json, subprocess, sys, re
L3 = {
 "romanticism-art": {
  "controversies": [
   {"issue": "西班牙有没有真正的浪漫主义时期？",
    "views": [
     {"holder": "强调其早发的论者（所引来源页 enc-romanticism 所述）",
      "basis": "认为西班牙浪漫主义是欧洲最早的浪漫主义之一。"},
     {"holder": "否定论者与 Richard Caldwell（所引来源页 enc-romanticism 所述）",
      "basis": "有论者认为西班牙根本没有文学浪漫主义时期；Caldwell 认为今人归入西班牙浪漫主义的作家其实是1920年代文学运动的先驱。"}]},
   {"issue": "浪漫主义与西方理性传统的关系应如何评价？",
    "views": [
     {"holder": "Isaiah Berlin（所引来源页 enc-romanticism 所述）",
      "basis": "认为浪漫主义瓦解了西方理性与道德绝对的古典传统，导致“客观真理观念的消融”，并通向民族主义乃至法西斯与极权主义。"},
     {"holder": "当前学界较普遍的看法（所引来源页 enc-romanticism 所述）",
      "basis": "一般接受其属于反启蒙运动，但称其精确定义在20世纪思想史与文学史中一直争论而无共识；多数浪漫派观点大体进步，也有相当数量持保守立场。"}]}
  ],
  "data": [
   {"label": "赫尔德论地理塑造民族经济与习俗", "value": "1784年", "note": "来源:enc-romanticism"},
   {"label": "法国大革命开始", "value": "1789年", "note": "来源:enc-romanticism"},
   {"label": "加勒特《卡蒙斯》出版，葡萄牙浪漫主义开端", "value": "1825年", "note": "来源:enc-romanticism"}
  ],
  "complex_diagram_note": "以欧洲地图式分区展示各国浪漫主义起始年份，并在西班牙处旁注“最早之一”与“并无此时期”两说，另以并列框对照 Berlin 的评价与通行的反启蒙定位。"
 },
 "cubism": {
  "controversies": [
   {"issue": "立体主义的首创权归毕加索还是布拉克？",
    "views": [
     {"holder": "以毕加索为发明者的看法（所引来源页 enc-cubism 所述，1911年已普遍如此认定；Gertrude Stein 以其1909年霍尔塔风景为最早立体主义画作）",
      "basis": "1911年时毕加索已被公认为立体主义的发明者。"},
     {"holder": "后来强调布拉克优先的论者（所引来源页 enc-cubism 所述）",
      "basis": "依据布拉克1908年埃斯塔克风景对空间、体积与体块的处理；Vauxcelles 正是因其《埃斯塔克的房子》写下“立方体的怪异”。"}]},
   {"issue": "哪些画家算“真正的”立体主义者？",
    "views": [
     {"holder": "以毕加索、布拉克为中心的狭义观（所引来源页 enc-cubism 所述）",
      "basis": "把立体主义的发明与核心归于毕加索与布拉克二人。"},
     {"holder": "Christopher Green（所引来源页 enc-cubism 所述）",
      "basis": "指出这种看法伴随“明显狭窄的定义”，边缘化了1911年独立沙龙41号厅参展的梅青格尔、格莱兹、莱热、德劳内、勒福科尼耶等人。"}]}
  ],
  "data": [
   {"label": "布拉克《埃斯塔克的房子》", "value": "1908年", "note": "来源:enc-cubism"},
   {"label": "Vauxcelles 在《Gil Blas》写“立方体的怪异”", "value": "1909年3月25日", "note": "来源:enc-cubism"},
   {"label": "首次立体主义群展（独立沙龙41号厅，无毕加索、布拉克作品）", "value": "1911年春", "note": "来源:enc-cubism"}
  ],
  "complex_diagram_note": "以1908—1911年时间轴并列画廊立体主义（毕加索、布拉克）与沙龙立体主义（41号厅诸人）两线，旁注首创权与定义范围两项争议。"
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
