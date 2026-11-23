# -*- coding: utf-8 -*-
"""一键体检入口 audit_all.py：串行运行全部本地校验与审计，汇总为一张表。
不联网、不改数据；返回码 0=全部通过，1=有失败项。
用法：python tools/audit_all.py
"""
import json,os,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY=[sys.executable,"-X","utf8"]
import glob,py_compile
_bad=[]
for _p in sorted(glob.glob(os.path.join(ROOT,"tools","*.py"))):
    try: py_compile.compile(_p,doraise=True)
    except Exception as _e: _bad.append((os.path.basename(_p),str(_e)[:80]))
STEPS=[
 ("py_compile（全部工具可编译）", "__COMPILE__"),
 ("check.py（R1-R21 硬规则）","tools/check.py"),
 ("check_links.py（站内链接）","tools/check_links.py"),
 ("healthcheck_c10.py（九维体检）","tools/healthcheck_c10.py"),
 ("consistency_audit.py（内容自洽）","tools/consistency_audit.py"),
 ("link_audit.py（关联图）","tools/link_audit.py"),
 ("oneway_audit.py（单向关联）","tools/oneway_audit.py"),
 ("pending_render_audit_c30.py（渲染一致性+HTML结构）","tools/pending_render_audit_c30.py"),
 ("overlay_guard.py（覆盖层不得改基础字段）","tools/overlay_guard.py"),
 ("invariants_c54.py（不变式盘点：死重/孤儿/L3/单元页）","tools/invariants_c54.py"),
 ("usability_c60.py（可用性：标题层级/锚点/表格/link）","tools/usability_c60.py"),
]
summary=[]
fails=0
fails_compile=0
env=dict(os.environ,PYTHONIOENCODING="utf-8")
for name,script in STEPS:
    if script=="__COMPILE__":
        summary.append({"step":name,"status":"ok" if not _bad else "FAIL",
                        "tail":"%d 个 .py 全部通过"%len(glob.glob(os.path.join(ROOT,"tools","*.py"))) if not _bad else str(_bad[:3])})
        if _bad: fails_compile=1
        continue
    p=os.path.join(ROOT,script)
    if not os.path.exists(p):
        summary.append({"step":name,"status":"missing"}); continue
    r=subprocess.run(PY+[p],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace",env=env)
    out=(r.stdout or "").strip().splitlines()
    tail=out[-1][:110] if out else ""
    ok=(r.returncode==0) and ("errors=0" in " ".join(out) or r.returncode==0)
    if "errors=" in " ".join(out) and "errors=0" not in " ".join(out): ok=False
    if not ok: fails+=1
    summary.append({"step":name,"returncode":r.returncode,"status":"ok" if ok else "FAIL","tail":tail})
print("="*78)
print("一键体检 audit_all")
print("="*78)
for s in summary:
    print(" %-34s %-5s %s"%(s["step"],s.get("status"),s.get("tail","")[:70]))
print("-"*78)
_total=fails+fails_compile
print("失败项：%d（其中工具编译失败 %d）"%(_total,fails_compile))
json.dump({"steps":summary,"fails":_total,"fails_compile":fails_compile},open(os.path.join(ROOT,"reports","audit_all.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
sys.exit(1 if (fails or fails_compile) else 0)