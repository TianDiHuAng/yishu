import json, subprocess, sys, re
L3 = {
 "verdi": {
  "controversies": [
   {"issue": "威尔第的歌剧有多大的政治性？",
    "views": [
     {"holder": "Marco Pizzo、George Martin（所引来源页 enc-verdi 所述）",
      "basis": "Pizzo 认为1815年后音乐成为政治工具，威尔第歌剧受爱国情怀与意大利独立斗争激发；Martin 称其为复兴运动“最伟大的艺术家”。《纳布科》中的《希伯来奴隶合唱》曾被爱国者用作颂歌，1859年起“Viva VERDI”成为拥戴维托里奥·埃马努埃莱的口号。"},
     {"holder": "Mary Ann Smart、Roger Parker（所引来源页 enc-verdi 所述）",
      "basis": "Smart 指出当时的乐评很少提及政治主题；Parker 认为其歌剧的政治维度是19世纪后期民族主义史家夸大的。所引来源页另称1850年代起其歌剧中爱国主题很少。"}]}
  ],
  "data": [
   {"label": "“Viva VERDI”口号出现（那不勒斯）", "value": "1859年", "note": "来源:enc-verdi"},
   {"label": "意大利统一", "value": "1861年", "note": "来源:enc-verdi"},
   {"label": "Pizzo 所称音乐成为政治工具的起点", "value": "1815年后", "note": "来源:enc-verdi"}
  ],
  "complex_diagram_note": "以1815—1861年时间轴标出复兴运动节点与《纳布科》、“Viva VERDI”口号，并以并列框对照 Pizzo/Martin 与 Smart/Parker 两方。"
 },
 "jan-van-eyck": {
  "controversies": [
   {"issue": "扬·凡·艾克的真迹有多少件？",
    "views": [
     {"holder": "收藏这些作品的博物馆（所引来源页 enc-jan-van-eyck 引 Holland Cotter 1998年所述）",
      "basis": "1980年代中期约40件作品被视为原作。"},
     {"holder": "主要研究者（所引来源页 enc-jan-van-eyck 引 Holland Cotter 1998年所述）",
      "basis": "其中约10件被有力地质疑为工坊之作；Cotter 估计可归属者只有约二十多幅，且把握程度不一，并指出艺术史家与收藏馆在定作者时关系复杂、存在张力。"}]}
  ],
  "data": [
   {"label": "有把握归属的存世画作年代", "value": "1432—1439年", "note": "来源:enc-jan-van-eyck"},
   {"label": "签名并题“ALS ICH KAN”的作品", "value": "10件（含根特祭坛画）", "note": "来源:enc-jan-van-eyck"},
   {"label": "1980年代中期视为原作的作品", "value": "约40件，其中约10件今被质疑", "note": "来源:enc-jan-van-eyck"},
   {"label": "常被认作《都灵—米兰时祷书》“G手”", "value": "1901年起", "note": "来源:enc-jan-van-eyck"}
  ],
  "complex_diagram_note": "以柱状对照1980年代中期约40件、受质疑约10件与 Cotter 估计约二十多件，旁注“G手”归属与1432—1439年署年作品。"
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
