# -*- coding: utf-8 -*-
"""规范化 wd-* 来源：修正 'QQ123' → 'Q123'（title 与 url 同步），并核对 URL 可达（抽样）。"""
import json,os,re,subprocess
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sp=os.path.join(ROOT,"data","sources.json")
sd=json.load(open(sp,encoding="utf-8"))
fixed=[]
for s in sd["sources"]:
    if not s["id"].startswith("wd-"): continue
    t=s["title"]; u=s["url"]
    nt=re.sub(r"\bQQ(\d+)", r"Q\1", t)
    nu=re.sub(r"/QQ(\d+)$", r"/Q\1", u)
    if nt!=t or nu!=u:
        s["title"]=nt; s["url"]=nu; fixed.append((s["id"],nt,nu))
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("规范化:",len(fixed))
for f in fixed[:5]: print("  ",f)
# 抽样核对一个 URL
if fixed:
    u=fixed[0][2]
    p=subprocess.run(["curl","-sS","-m","15","-A","YishuBot/1.0","-o","/dev/null","-w","%{http_code}",u],capture_output=True,text=True)
    print("抽查",u,"HTTP",p.stdout.strip())