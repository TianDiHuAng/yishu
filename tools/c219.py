import json, subprocess, sys, re
L3 = {
 "abstract-expressionism": {
  "controversies": [
   {"issue": "抽象表现主义在冷战中是否被美国中央情报局（CIA）推广利用？",
    "views": [
     {"holder": "修正派：1970年代中期以来的论者，Frances Stonor Saunders《文化冷战》（所引来源页 enc-abstract-expressionism 所述）",
      "basis": "认为1950年代初CIA视此风格为美国思想自由与自由市场的象征，并经文化自由大会（1950—1967）资助、组织推广美国抽象表现主义画家；引CIA国际组织处首任主管 Tom Braden 的访谈为佐证。"},
     {"holder": "Michael Kimmelman（《纽约时报》首席艺评人，《重访修正派》，所引来源页 enc-abstract-expressionism 所述）",
      "basis": "认为关于1940—1950年代美国艺坛的许多信息以及修正派的解读是错误的或脱离语境的。"}]}
  ],
  "data": [
   {"label": "美国社会现实主义为主流", "value": "1930年代", "note": "来源:enc-abstract-expressionism"},
   {"label": "文化自由大会推广活动期", "value": "1950—1967年", "note": "来源:enc-abstract-expressionism"},
   {"label": "CIA说开始被提出", "value": "1970年代中期", "note": "来源:enc-abstract-expressionism"}
  ],
  "complex_diagram_note": "以1930—1970年代时间轴标出社会现实主义主流、抽象表现主义兴起、文化自由大会活动期与修正派论点出现，并以并列框对照 Saunders 与 Kimmelman 两方。"
 },
 "van-gogh": {
  "controversies": [
   {"issue": "梵高所患何病？",
    "views": [
     {"holder": "Perry（1947年首倡）及精神科医生 Hemphill、Blumer（所引来源页 enc-van-gogh 所述）",
      "basis": "认为是双相障碍；所引来源页称共识是其病为发作性，间有正常期。"},
     {"holder": "生物化学家 Wilfred Arnold（所引来源页 enc-van-gogh 所述）",
      "basis": "认为症状更符合急性间歇性卟啉症，并指出流行的“双相障碍与创造力相关”之说可能站不住；另有论者提出颞叶癫痫伴抑郁。"}]}
  ],
  "data": [
   {"label": "双相障碍说首次提出", "value": "1947年（Perry）", "note": "来源:enc-van-gogh"},
   {"label": "所引来源页列出的回溯诊断", "value": "3种（双相障碍、急性间歇性卟啉症、颞叶癫痫伴抑郁）", "note": "来源:enc-van-gogh"},
   {"label": "叔父 Cornelis Marinus 委托画海牙", "value": "1882年初", "note": "来源:enc-van-gogh"}
  ],
  "complex_diagram_note": "以分支图并列三种回溯诊断及其提出者，旁注营养不良、过劳、失眠与酒精等加重因素。"
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
