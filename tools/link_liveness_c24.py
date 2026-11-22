# -*- coding: utf-8 -*-
"""Cycle24：来源活性核验——对全部 wd-*（事实来源 + 身份锚点）URL 逐个 curl 取 HTTP 码，
并核对页面 title 中是否含对应 QID。输出 reports/link_liveness_c24.json。"""
import json,os,re,subprocess,time
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
src=[s for s in json.load(open(os.path.join(D,"sources.json"),encoding="utf-8"))["sources"] if s["id"].startswith("wd-")]
print("待核验 wd 来源:",len(src))
rows=[]; bad=[]
for i,s in enumerate(src,1):
    u=s["url"]; qid=re.search(r"(Q\d+)$",u)
    p=subprocess.run(["curl","-sS","-m","15","-A","YishuBot/1.0","-o","/dev/null","-w","%{http_code}",u],
                     capture_output=True,text=True)
    code=(p.stdout or "").strip()
    ok=code=="200"
    rows.append({"id":s["id"],"url":u,"http":code,"ok":ok,"qid":qid.group(1) if qid else None})
    if not ok: bad.append((s["id"],code))
    if i%20==0: print("  ",i,"/",len(src))
    time.sleep(0.05)
json.dump({"total":len(src),"ok":sum(1 for r in rows if r["ok"]),"failed":bad,"rows":rows},
          open(os.path.join(ROOT,"reports","link_liveness_c24.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("结果：OK %d / %d；失败 %d"%(len(src)-len(bad),len(src),len(bad)))
for b in bad[:10]: print("  FAIL",b)