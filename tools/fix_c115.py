# -*- coding: utf-8 -*-
"""修复 Cycle115 重名：khurasan-ewer 已存在(cma-1945-27)。把本轮新件改名 khurasan-ewer-va 并恢复原 overlay。"""
import json,os,subprocess,io,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LD=os.path.join(ROOT,"data","l2")
# 1) 先把我的 overlay 另存为 khurasan-ewer-va.json
src=os.path.join(LD,"khurasan-ewer.json")
d=json.load(open(src,encoding="utf-8")); d["id"]="khurasan-ewer-va"
json.dump(d,open(os.path.join(LD,"khurasan-ewer-va.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("saved khurasan-ewer-va.json")
# 2) 恢复原 overlay
subprocess.run(["git","checkout","HEAD","--","data/l2/khurasan-ewer.json"],cwd=ROOT)
print("restored original overlay")
# 3) catalog：把“第二个” khurasan-ewer 元组的 id 与 title 改掉
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
idx=[i for i,l in enumerate(lines) if l.startswith("('khurasan-ewer',")]
print("tuple starts:",idx)
assert len(idx)>=2, idx
i=idx[-1]  # 最后一个是本轮追加的
lines[i]="('khurasan-ewer-va',"
# 改其后一行 title（'呼罗珊嵌金银执壶' -> 加 V&A）
for j in range(i,min(i+4,len(lines))):
    if "呼罗珊嵌金银执壶" in lines[j]:
        lines[j]=lines[j].replace("呼罗珊嵌金银执壶","呼罗珊嵌金银执壶（V&A）")
        break
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog renamed ->khurasan-ewer-va")
import ast; ast.parse(io.open(p,encoding="utf-8").read()); print("catalog syntax ok")