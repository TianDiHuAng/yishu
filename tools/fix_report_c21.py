# -*- coding: utf-8 -*-
"""修复 build_report_autonomous.py 中被 ASCII 引号破坏的 cycle21 说明行：整行替换为不含 ASCII 引号的文本。"""
import io,os,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","build_report_autonomous.py")
lines=io.open(P,encoding="utf-8").read().split("\n")
NEW=('    L.append("- 本轮特别说明：用 Wikidata 补齐 **5 个作品条目的尺寸/材质/藏品编号**'
     '（蒙娜丽莎 79.4×53.4cm、INV 779/MR 316；星夜 73.7×92.1cm、472.1941；'
     '维纳斯的诞生 172.5×278.5cm、00158551；西斯廷天顶 4093×1341cm；格尔尼卡 349×776cm、DE00050），'
     '这正是 TASK 提示「最容易写错」的信息。但**只登记在待核实节、不写入正文**——'
     '该组数据仅有一个结构化来源，未达双源互证标准。'
     '另登记日本建筑(Q1422874)/印度建筑(Q61050)实体，但**本轮不建条目**：'
     '现有日/印艺术页此刻无法复核是否含建筑章节，据此写木构或石窟特征即属无源断言。")')
n=0
for i,ln in enumerate(lines):
    if ln.strip().startswith("L.append(") and "最容易写错" in ln:
        lines[i]=NEW; n+=1
io.open(P,"w",encoding="utf-8").write("\n".join(lines))
print("replaced lines:",n)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],
                 cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("build_report rc=",r.returncode, (r.stdout or "").strip()[:120], (r.stderr or "").strip()[-200:])