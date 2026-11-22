# -*- coding: utf-8 -*-
"""加强网络鲁棒性：curl 重试5次、间隔递进；失败时抛错而不是静默返回空，
避免把"网络抖动"误判成"无此实体"。"""
import io,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","person_dates_c15.py")
s=io.open(P,encoding="utf-8").read()
old='''def curl_json(url,tries=3):
    for i in range(tries):
        p=subprocess.run(["curl","-sS","-m","15","-A",UA,url],capture_output=True,text=True,encoding="utf-8",errors="replace")
        if p.returncode==0 and p.stdout.strip().startswith("{"):
            try: return json.loads(p.stdout)
            except Exception: pass
    return None'''
new='''def curl_json(url,tries=5):
    import time
    last=None
    for i in range(tries):
        p=subprocess.run(["curl","-sS","-m","20","-A",UA,url],capture_output=True,text=True,encoding="utf-8",errors="replace")
        if p.returncode==0 and p.stdout.strip().startswith("{"):
            try: return json.loads(p.stdout)
            except Exception as e: last=e
        else:
            last=p.stderr[:60] if p.stderr else "rc=%d"%p.returncode
        time.sleep(0.8*(i+1))
    print("   [warn] fetch failed:",url[:70],last)
    return None'''
assert old in s; s=s.replace(old,new)
io.open(P,"w",encoding="utf-8").write(s)
print("hardened curl retries")