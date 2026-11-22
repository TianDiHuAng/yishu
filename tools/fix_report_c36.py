# -*- coding: utf-8 -*-
"""修复 build_report_autonomous.py 中被 ASCII 引号破坏的 cycle36 说明行：整行替换（用「」）。"""
import io,os,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","build_report_autonomous.py")
lines=io.open(P,encoding="utf-8").read().split("\n")
NEW=('    L.append("- 本轮把 B5 剩余 5 项用 Wikidata **时间声明**再核一遍，结果为「1 个真实差异 + 1 个备查事实 + 3 个仍无解」：'
     '①**romanesque 发现断代差异**——Wikidata「Romanesque art」(Q46805) 记 P580=1000 / P582=1200，'
     '本条目正文采「约1000—1150」，**终点差 50 年**，而 1150 本身源自早期种子、从未有独立来源；'
     '②张旭实体给出**生年 670**，但条目待核的是「作品名称」，仍无解；'
     '③realism 年代、草书年代、donatello 术语无可用声明。'
     '处置：**一律不据单一结构化来源改正文**，差异与备查事实写进复核记录，并注明「待第三来源判定」。'
     '发现差异比抹平差异更有价值。")')
n=0
for i,ln in enumerate(lines):
    if ln.strip().startswith("L.append(") and "B5 剩余 5 项用 Wikidata" in ln:
        lines[i]=NEW; n+=1
io.open(P,"w",encoding="utf-8").write("\n".join(lines))
print("replaced:",n)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],
                 cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("rc=",r.returncode,"|",(r.stdout or "").strip()[:80],(r.stderr or "").strip()[-160:])