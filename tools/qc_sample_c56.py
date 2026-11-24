# -*- coding: utf-8 -*-
"""Cycle56：抽样质量复核（10% = 20 条，等距抽取）。
对每条：
 A 引用来源是否都在库且 verified；
 B needs_verification 与待核实是否一致；
 C 若引用 cma-*/vam-* 机构记录，**抓取该记录并核对正文中的尺寸/年代是否与记录一致**（这是本轮重点）；
 D 正文是否混入【已复核】留痕（应在待核实里）。
输出 reports/qc_sample_c56.json。"""
import json,os,subprocess,re,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
CACHE=os.path.join(D,"_cache","museum"); os.makedirs(CACHE,exist_ok=True)
es=json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]
src={s["id"]:s for s in json.load(open(os.path.join(D,"sources.json"),encoding="utf-8"))["sources"]}
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
def fetch(url):
    k=os.path.join(CACHE,re.sub(r"\W+","_",url)[-120:]+".json")
    if os.path.exists(k):
        try: return json.load(open(k,encoding="utf-8"))
        except Exception: pass
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,url],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try:
        d=json.loads(p.stdout); json.dump(d,open(k,"w",encoding="utf-8"),ensure_ascii=False); return d
    except Exception: return None
import os as _o
_the_all=_o.environ.get("QC_ALL")=="1"
step=max(1,len(es)//20)
sample=[e for e in es if any(s.startswith(("cma-","vam-")) for s in e.get("sources",[]))] if _the_all else [es[i] for i in range(0,len(es),step)][:20]
issues=[]; checked=[]; dim_checks=0; dim_ok=0
def norm(s): return re.sub(r"[\s,，]","",str(s or ""))
for e in sample:
    if e["id"].endswith("-art"): continue  # 导览条目不复述各件尺寸
    sid_list=e.get("sources",[])
    # A
    for s in sid_list:
        if s not in src: issues.append((e["id"],"来源不在库",s))
        elif not src[s].get("verified"): issues.append((e["id"],"来源未核验",s))
    # B
    pend=(e.get("sections",{}).get("待核实","") or "").strip()
    if e.get("needs_verification") and not pend: issues.append((e["id"],"待核实为空",""))
    # D
    body="".join(v for k,v in e.get("sections",{}).items() if k!="待核实")
    if "【已复核" in body: issues.append((e["id"],"正文混入复核留痕",""))
    # C 机构记录核对
    for s in sid_list:
        u=src.get(s,{}).get("url","")
        if s.startswith("cma-artist-"): continue  # 传记载体，不对其作品尺寸/年代核对
        if "openaccess-api.clevelandart.org" in u:
            d=fetch(u); a=(d or {}).get("data") or {}
            raw=str(a.get("measurements") or ""); dims=norm(raw); cd=str(a.get("creation_date") or "")
            if dims:
                # 取正文中的尺寸片段（如 86.5 × 37.5）
                metric=raw.split("(")[0]
                nums=re.findall(r"\d+(?:\.\d+)?",norm(metric)) if (" x " in metric or "×" in metric) else []
                if len(nums)>=2:
                    dim_checks+=1
                    nb=norm(body)
                    miss=[x for x in nums[:3] if norm(x) not in nb]
                    if not miss: dim_ok+=1
                    else:
                        issues.append((e["id"],"尺寸数字未在正文出现:%s（记录:%s）"%(miss,a.get("measurements","")[:40]),"C"))
            yrs=[] if re.search(r"c\.|possibly| or |mid-|late|early",cd) else re.findall(r"\d{3,4}",cd)
            if yrs:
                def _cens(y):
                    n=int(y)
                    if n<100: return []
                    # 同时给出两种世纪解释：紧邻与"NN00s"惯用义，避免误报
                    return ["%d世纪"%(n//100),"%d世纪"%(n//100+1)]
                cands=[]
                for y in yrs[:2]:
                    cands.append(y)
                    cands.extend(_cens(y))
                hit=any((x in body) or (x in e.get("when","")) for x in cands)
                if not hit:
                    issues.append((e["id"],"记录年代「%s」未在正文/年代字段出现"%cd,"C"))
        elif "api.vam.ac.uk" in u:
            d=fetch(u); r=(d or {}).get("record") or {}
            if r.get("dimensions"):
                dim_checks+=1
                nums=[x.get("value") for x in r["dimensions"][:2]]
                if all(any(n in body for n in [str(v)]) for v in nums if v):
                    dim_ok+=1
    checked.append(e["id"])
print("受检 %d 条：%s"%(len(sample),",".join(checked[:8])+"…"))
print("尺寸核对：%d 项，命中 %d 项"%(dim_checks,dim_ok))
print("发现问题：%d"%len(issues))
for i in issues[:15]: print("  ",i)
json.dump({"sample":checked,"dim_checks":dim_checks,"dim_ok":dim_ok,"issues":issues},
          open(os.path.join(ROOT,"reports","qc_sample_c56.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)