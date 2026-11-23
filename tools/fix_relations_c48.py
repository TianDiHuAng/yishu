# -*- coding: utf-8 -*-
"""按元组定位，为 4 件器物的 related 追加导览条目 id（保证双向关联）。"""
import io,os,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(ROOT,"tools","catalog.py")
lines=io.open(p,encoding="utf-8").read().split("\n")
TARGET={"maya-el-peru-stela":"americas-art","aztec-feathered-serpent":"americas-art",
        "maori-hei-tiki":"oceania-art","asmat-war-shield":"oceania-art"}
done=[]
for tid,ov in TARGET.items():
    start=None
    for i,l in enumerate(lines):
        if l.strip().startswith("('%s',"%tid):
            start=i; break
    assert start is not None, tid
    # 在其后 16 行内找到 related 字符串行（形如 'a,b',）
    for j in range(start,min(start+16,len(lines))):
        m=re.search(r"'([a-z0-9\-]+(?:,[a-z0-9\-]+)*)',\s*$",lines[j])
        if m and ov not in m.group(1) and ("," in m.group(1) or m.group(1).endswith("-work") or True):
            val=m.group(1)
            if val.split(",")[0] in ("maya-el-peru-stela","aztec-feathered-serpent","maori-hei-tiki","asmat-war-shield") or True:
                # 仅在包含目标器物 id 或明显是 related 字段时替换
                if tid in val or val in (TARGET.keys()):
                    lines[j]=lines[j][:m.start(1)]+val+","+ov+lines[j][m.end(1):]
                    done.append((tid,j+1))
                    break
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("patched:",done)