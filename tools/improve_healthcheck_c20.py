# -*- coding: utf-8 -*-
"""Cycle20：改进体检工具——①把"来源重合度未执行"的原因写精确（内容来源不可达，Wikidata 无正文）；
②把 link_audit 摘要并入 healthcheck 输出。"""
import io,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","healthcheck_c10.py"); s=io.open(P,encoding="utf-8").read()
old='R["overlap"]="skipped: network degraded"'
new=('R["overlap"]="skipped: 内容来源（Wikipedia/Met/Tate）不可达，无法抓取正文比对；'
     'Wikidata 为结构化数据（无正文），不适用 n-gram 重合度。最近有效结果：Cycle5 抽样5条，重合 0%"')
assert old in s; s=s.replace(old,new)
old2='json.dump(R,open(os.path.join(ROOT,"reports","healthcheck_c10.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)'
new2=('la=os.path.join(ROOT,"reports","link_audit.json")\n'
      'if os.path.exists(la):\n'
      '    L=json.load(open(la,encoding="utf-8"))\n'
      '    R["link_audit"]={"cross_domain":len(L.get("cross_domain",[])),"oneway":L.get("oneway_count"),"total_links":L.get("total_links")}\n'
      +old2)
assert old2 in s; s=s.replace(old2,new2)
io.open(P,"w",encoding="utf-8").write(s)
print("healthcheck improved")