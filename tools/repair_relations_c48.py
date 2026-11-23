# -*- coding: utf-8 -*-
"""修复 Cycle48 的关系补丁误伤：把被污染的 id 复原，并把导览 id 追加到真正的 related 行（sources 行的上一行）。"""
import io,os,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(ROOT,"tools","catalog.py")
lines=io.open(p,encoding="utf-8").read().split("\n")
TARGET={"maya-el-peru-stela":"americas-art","aztec-feathered-serpent":"americas-art",
        "maori-hei-tiki":"oceania-art","asmat-war-shield":"oceania-art"}
report=[]
for tid,ov in TARGET.items():
    # 1) 复原被污染的 id 行
    bad="('%s,%s',"%(tid,ov)
    for i,l in enumerate(lines):
        if l.strip()==bad:
            lines[i]=l.replace(bad,"('%s',"%tid); report.append(("id-restored",tid,i+1)); break
    # 2) 定位元组起点，再向上寻找 sources 行（含 cma-/vam-），其上一行即 related
    start=None
    for i,l in enumerate(lines):
        if l.strip().startswith("('%s',"%tid): start=i; break
    assert start is not None, tid
    end=start
    for j in range(start,min(start+18,len(lines))):
        if lines[j].strip().startswith("('cma-") or lines[j].strip().startswith("('vam-") or '"cma-' in lines[j] or '"vam-' in lines[j]:
            end=j; break
    rel_idx=end-1
    m=re.search(r"'([a-z0-9\-]+(?:,[a-z0-9\-]+)*)'",lines[rel_idx])
    assert m, ("related line not found", tid, lines[rel_idx])
    val=m.group(1)
    if ov not in val.split(","):
        newval=val+","+ov
        lines[rel_idx]=lines[rel_idx][:m.start(1)]+newval+lines[rel_idx][m.end(1):]
        report.append(("relation",tid,rel_idx+1,newval))
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print(report)