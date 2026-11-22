# -*- coding: utf-8 -*-
"""为 cycle14 追加 REPORT 说明（按 D019：用脚本文件，禁用反引号与未转义 ASCII 引号）。"""
import io,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","build_report_autonomous.py")
s=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle14"' in s:
    print("already present"); raise SystemExit
block = (
'if cyc=="cycle14":\n'
'    L.append("- 本轮特别说明（突破）：Cycle13 的网络结论需修正——Wikipedia/Met/Tate 仍不可达、'
'百度/Khan 仅返回反爬壳页，但 www.wikidata.org（api.php 与 Special:EntityData/*.json）、'
'api.wikimedia.org、commons.wikimedia.org、dbpedia.org 均可达且返回可用 JSON。'
'新增 tools/wikidata_verify.py（三重消歧：标题+描述类型词+作者名），核验 5 个作品档案的作者与收藏地，'
'结果与条目一致（星夜/维纳斯的诞生/西斯廷天顶画/格尔尼卡/春之祭）；'
'春之祭实体的 P170 字段异常（西德尼·諾蘭）已标注不采信。'
'同时修复真实数据丢失 bug：merge_l2 的 sources 由覆盖改为并集（D021）。'
'来源 164→169（verified 164），check/links/audit_all 全通过。")\n'
)
anchor='if cyc=="cycle13":'
assert anchor in s
io.open(P,"w",encoding="utf-8").write(s.replace(anchor, block+anchor))
print("cycle14 report block added")