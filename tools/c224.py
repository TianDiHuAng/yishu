import json, subprocess, sys, re
L3 = {
 "shostakovich": {
  "controversies": [
   {"issue": "肖斯塔科维奇是否以音乐进行隐蔽的异见表达？（正统与修正之争）",
    "views": [
     {"holder": "修正派：Solomon Volkov（1979年《见证》）、其子女 Maxim 与 Galina、Allan B. Ho 与 Dmitry Feofanov（所引来源页 enc-shostakovich 所述）",
      "basis": "《见证》称许多作品藏有反政府的暗码，把他放进自普希金以来俄国艺术家绕过审查的传统；Volkov 认为他在与政府的关系中扮演“圣愚”。Mravinsky 说他常以具体意象说明意图；Ho 与 Feofanov 反驳称至少两页经签名的手稿含有争议内容。"},
     {"holder": "质疑者：Laurel Fay、Richard Taruskin（所引来源页 enc-shostakovich 所述）",
      "basis": "质疑《见证》的真实性，认为它由旧文章、传闻和可能少量本人谈话拼成；Fay 2002年《重审 Volkov 的〈见证〉》指出手稿中唯有经本人签名核实的几页与早年访谈逐字相同，且都无争议内容。所引来源页另称 Maxim 1981年曾说该书不是其父之作。"}]}
  ],
  "data": [
   {"label": "《见证》出版", "value": "1979年", "note": "来源:enc-shostakovich"},
   {"label": "Maxim 称该书非其父之作", "value": "1981年", "note": "来源:enc-shostakovich"},
   {"label": "Maxim 转而较正面评价 Volkov", "value": "1991年苏联解体后", "note": "来源:enc-shostakovich"},
   {"label": "Fay《Volkov's Testimony reconsidered》", "value": "2002年", "note": "来源:enc-shostakovich"}
  ],
  "complex_diagram_note": "以1979—2002年时间轴标出《见证》出版、Maxim 前后态度变化与 Fay 文章，并以并列框对照修正派与质疑者的证据。"
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
