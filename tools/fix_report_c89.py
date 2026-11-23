# -*- coding: utf-8 -*-
"""Cycle89：补齐 REPORT 生成器中缺失的 cycle87 块，并加入 cycle89（文档对齐）块。"""
import io,os,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle87"' not in t:
    block=('if cyc=="cycle87":\n'
           '    L.append("- 希腊罗马实物 4 件（288 → 292）：库罗斯青年残躯、赫拉克勒斯青铜小像、罗马运动员像、'
           '由尼禄像改刻的韦斯巴芗头像。①库罗斯类型可能受埃及影响、随后按希腊路线发展；'
           '②赫拉克勒斯像旧称运动员，该馆称「很可能」是击打姿态的英雄；'
           '③罗马运动员像由希腊原型转为大理石并加支撑构件（树干/撑杆）；'
           '④韦斯巴芗头像在古代由尼禄像改刻，是**记忆抹除**的物质痕迹，且入藏时相接的躯体**并非原配**（1973年分离）。'
           'R2 同时抓到「约前2144—2124年」的公元后误读，改为双写公元前。站点 325 → 329 页。")\n')
    anchor='if cyc=="cycle86":'
    assert anchor in t
    t=t.replace(anchor, block+anchor); print("cycle87 block inserted")
if 'cyc=="cycle89"' not in t:
    block=('if cyc=="cycle89":\n'
           '    L.append("- 交付前一致性收束：以仓库实际数据为准，把 README / PROGRESS / PROJECT_STATUS 的条目、'
           '来源、单元、页面、硬规则与体检步数一次性对齐为 **300 条 / 431 来源 / 28 单元 / 337 页 / R1–R22 / 12 步**。'
           '并补齐生成器中遗漏的 cycle87 报告块。强调：**300 是数量里程碑，不等于覆盖均衡**；未写 ALL_DONE，'
           '饱和判定仍以 `SATURATION.json` 为准（当前未饱和）。")\n')
    anchor='if cyc=="cycle88":'
    assert anchor in t
    t=t.replace(anchor, block+anchor); print("cycle89 block inserted")
io.open(P,"w",encoding="utf-8").write(t)
r=subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:60],(r.stderr or "").strip()[-100:])