# -*- coding: utf-8 -*-
"""修 build_report_autonomous.py 中 cycle54 段落里的 ASCII 引号（改用「」）。"""
import io,os,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","build_report_autonomous.py")
lines=io.open(P,encoding="utf-8").read().split("\n")
NEW=('    L.append("- **不变式全面盘点（Cycle50 以来首次）**，三项处置：①**11 条「死重来源」**（在库但零引用，'
     '如《夜巡》《珍珠耳环的少女》《呐喊》的来源）移入 data/sources_reserve.json 并在状态页公开——'
     '**来源总数 337 → 326**，数字变小但变真；②**L3 门禁复核 6 → 4**：rembrandt 与 monet 无两方具名立场，'
     '按 R16 **降为 L2**（monet 原文即写「概述未提及争议」），gothic 把「学界存在讨论」改写为**具名两方**'
     '（1140 年起点 vs 12世纪后期—16世纪框架）后**保留 L3**；③新增 **invariants_c54.py（9 项检查）为体检第 10 步**，'
     '仅硬性问题失败，L3 判读降为人工复核（本轮关键词法误报了 impressionism 与 baroque-music，二者实际各有两方）。'
     '现存 L3：希腊艺术、哥特式、印象派、巴洛克音乐；盘点硬性**问题 0**。")')
n=0
for i,l in enumerate(lines):
    if "不变式全面盘点（Cycle50 以来首次）" in l and l.strip().startswith("L.append("):
        lines[i]=NEW; n+=1
io.open(P,"w",encoding="utf-8").write("\n".join(lines))
print("replaced",n)
r=subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("rc=",r.returncode,"|",(r.stdout or "").strip()[:60],(r.stderr or "").strip()[-200:])