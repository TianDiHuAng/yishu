import json, subprocess, sys, re
L3 = {
 "chopin": {
  "controversies": [
   {"issue": "肖邦死于何病？",
    "views": [
     {"holder": "结核说：死亡证明与主治医生 Cruveilhier（当时法国结核病首要权威），及2014年心脏目视检查（2017年刊于《美国医学杂志》）（所引来源页 enc-chopin 所述）",
      "basis": "死亡证明写明死因为结核；2014年未开罐的心脏目视检查认为，可能的死因是慢性结核并发的罕见心包炎。"},
     {"holder": "其他病因说（所引来源页 enc-chopin 所述）",
      "basis": "曾有人提出囊性纤维化、肝硬化、α1-抗胰蛋白酶缺乏症等。"}]}
  ],
  "data": [
   {"label": "存世作品", "value": "230余部", "note": "来源:enc-chopin"},
   {"label": "心脏目视检查", "value": "2014年进行，2017年发表", "note": "来源:enc-chopin"},
   {"label": "乔治·桑致肖邦信件", "value": "约200封，1851年后退还桑并被其销毁", "note": "来源:enc-chopin"}
  ],
  "complex_diagram_note": "以分支图并列结核说与其他病因说，旁注死亡证明与2014年心脏检查两个证据节点。"
 },
 "wagner": {
  "controversies": [
   {"issue": "瓦格纳的思想在多大程度上影响了纳粹？",
    "views": [
     {"holder": "强调关联的一方（所引来源页 enc-wagner 所述）",
      "basis": "希特勒崇拜瓦格纳，视其歌剧为自己德意志民族愿景的体现，1922年演讲称其作品歌颂“英雄的条顿本性”，1923年起常赴拜罗伊特；瓦格纳音乐用于许多纳粹活动。"},
     {"holder": "限制关联的一方（所引来源页 enc-wagner 所述）",
      "basis": "其女婿张伯伦从未见过瓦格纳，不能可信地视为其观点的传递者；纳粹只取其思想中有用于宣传的部分而压制其余；纳粹高层整体并不分享希特勒的热情，罗森堡等人还拒斥《帕西法尔》。"}]}
  ],
  "data": [
   {"label": "希特勒演讲称颂瓦格纳", "value": "1922年", "note": "来源:enc-wagner"},
   {"label": "希特勒开始常赴拜罗伊特", "value": "1923年起", "note": "来源:enc-wagner"},
   {"label": "张伯伦与瓦格纳之女伊娃结婚", "value": "1908年", "note": "来源:enc-wagner"}
  ],
  "complex_diagram_note": "以关系图连接瓦格纳、拜罗伊特、张伯伦、希特勒与纳粹宣传，在各连线上标注两方对影响强弱的不同判断。"
 },
 "stravinsky": {
  "controversies": [
   {"issue": "斯特拉文斯基的新古典时期从哪部作品开始？",
    "views": [
     {"holder": "Noble（所引来源页 enc-stravinsky 所述）",
      "basis": "认为始于1920年的《管乐交响曲》。"},
     {"holder": "巴托克（所引来源页 enc-stravinsky 所述）",
      "basis": "认为“真正开始于”《管乐八重奏》，其后是《钢琴协奏曲》。"}]}
  ],
  "data": [
   {"label": "《管乐交响曲》", "value": "1920年", "note": "来源:enc-stravinsky"},
   {"label": "新古典时期的取法对象", "value": "18世纪（晚期巴洛克）音乐", "note": "来源:enc-stravinsky"}
  ],
  "complex_diagram_note": "以时间轴标出《管乐交响曲》《管乐八重奏》《钢琴协奏曲》，以两种起点标记对照 Noble 与巴托克的分期。"
 },
 "medieval-music": {
  "controversies": [
   {"issue": "中世纪音乐中不完全拍（imperfect tempus）段落如何演奏？",
    "views": [
     {"holder": "等长说（所引来源页 enc-medieval-music 所述部分音乐学家）",
      "basis": "认为这些段落中的短音符（breve）与完全拍段落等长。"},
     {"holder": "变长说（所引来源页 enc-medieval-music 所述部分音乐学家）",
      "basis": "认为其长度有变化，并就变化比例进一步争论。"}]}
  ],
  "data": [
   {"label": "《但以理剧》", "value": "约1140年", "note": "来源:enc-medieval-music"},
   {"label": "Marchetto da Padova 活跃期", "value": "1305—1319年", "note": "来源:enc-medieval-music"}
  ],
  "complex_diagram_note": "以记谱演进时间轴（纽姆谱、方形谱、新艺术时期的拍制）为主线，旁注不完全拍演奏的等长说与变长说。"
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
