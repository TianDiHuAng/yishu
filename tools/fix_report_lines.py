# -*- coding: utf-8 -*-
"""修复 build_report_autonomous.py 中被 bash 反引号吞掉内容的 cycle12/cycle13 说明行。"""
import io,os,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","build_report_autonomous.py")
lines=io.open(P,encoding="utf-8").read().split("\n")
FIX={
 "cycle12":"L.append(\"- 本轮特别说明：网络第六轮降级，按预案换角度。新增 tools/oneway_audit.py 审校 47 条单向关联（same_unit 36 / same_domain 11 / **跨域 0**），全部补成双向 → 关联总数 373→420、单向 0、零度节点 0、度均 3.0/最大 12；条目页新增「同单元前后条目」导航（按起始年代排序 + 单元总览入口），已在 art-modern 单元核对排序正确。\")",
 "cycle13":"L.append(\"- 本轮特别说明：网络能力精确定位——可达站点为 github（200）、百度百科（200）、Khan Academy（200）、Britannica（403），不可达为 wikipedia/met/tate；但可达站点全部返回反爬壳页（百度返回 __PARIS_CHALLENGE__ 挑战页 4.7KB 无正文；Khan 返回 Client Challenge 3KB；Britannica 为 Cloudflare Just a moment），因此仍无可用权威正文，内容建设继续受阻。同时新增 tools/audit_all.py 一键体检（check/链接/九维体检/内容自洽/关联图/单向关联 共6项，本轮 6/6 通过）。\")",
}
out=[]
cur=None
for ln in lines:
    m=re.match(r'if cyc=="(cycle\d+)":',ln.strip())
    if m: cur=m.group(1)
    if ln.strip().startswith("L.append(") and cur in FIX and "特别说明" in ln:
        out.append(FIX[cur]); cur=None; continue
    out.append(ln)
    if ln.strip().startswith("L.append(") and cur in FIX: cur=None
io.open(P,"w",encoding="utf-8").write("\n".join(out))
print("patched lines:",len(FIX))