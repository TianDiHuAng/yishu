# -*- coding: utf-8 -*-
"""把 workflow 产出的 L2 JSON（data/l2_generated/*.json）转成合规 SVG 并落盘为 data/l2/*.json。
SVG 由固定几何模板渲染，保证：viewBox 合法、元素不出界、仅用 CSS 类、无脚本。"""
import json, os, glob, html
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC=os.path.join(ROOT,"data","l2_generated")
DST=os.path.join(ROOT,"data","l2")
os.makedirs(DST,exist_ok=True)

def esc(s): return html.escape(str(s),quote=True)

def render_svg(diagram, title):
    nodes=diagram.get("nodes",[])[:4]
    arrows=diagram.get("arrows",[])
    caption=diagram.get("caption","")
    W,H=760,300
    n=len(nodes)
    if n<2: nodes=[{"label":title,"sub":"","kind":"accent"},{"label":"相关脉络","sub":"","kind":"muted"}]; n=2; arrows=[{"from":0,"to":1}]
    # 水平等距布局，保证不越界
    nw,nh=150,70
    gap=(W-40-nw*n)/(n-1) if n>1 else 0
    centers=[]
    boxes=[]
    for i,nd in enumerate(nodes):
        x=20+i*(nw+gap); y=110
        cls="svg-box-accent" if nd.get("kind")=="accent" else "svg-box-muted"
        boxes.append("<rect class='%s' x='%.1f' y='%d' width='%d' height='%d' rx='8'/>"%(cls,x,y,nw,nh))
        label=esc(nd.get("label",""))[:12]
        boxes.append("<text class='svg-label%s' x='%.1f' y='%d' text-anchor='middle'>%s</text>"%(
            " svg-label-strong" if nd.get("kind")=="accent" else "",x+nw/2,y+32,label))
        if nd.get("sub"):
            boxes.append("<text class='svg-sub' x='%.1f' y='%d' text-anchor='middle'>%s</text>"%(x+nw/2,y+55,esc(nd['sub'])[:14]))
        centers.append((x+nw/2,y+nh/2))
    arr=[]
    for a in arrows:
        f,t=a.get("from"),a.get("to")
        if not (isinstance(f,int) and isinstance(t,int)) or f==t: continue
        if f<0 or t<0 or f>=n or t>=n: continue
        x1,y1=centers[f]; x2,y2=centers[t]
        # 从框边缘出发
        dx=x2-x1
        sx1=x1+(nw/2 if dx>0 else -nw/2); sx2=x2-(nw/2 if dx>0 else -nw/2)
        arr.append("<line class='svg-arrow' x1='%.1f' y1='%d' x2='%.1f' y2='%d'/>"%(sx1,y1,sx2,y2))
        ax=sx2 if dx>0 else sx2
        p="%s,%d %s,%d %s,%d"%(ax,y2, ax+(-9 if dx>0 else 9),y2-5, ax+(-9 if dx>0 else 9),y2+5)
        arr.append("<polygon class='svg-arrowhead' points='%s'/>"%p)
    t=esc(title)[:24]
    cap="<text class='svg-caption' x='%d' y='%d' text-anchor='middle'>%s</text>"%(W//2,262,esc(caption)[:40])
    return ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 %d %d' role='img' aria-label='%s 示意图'>"
            "<title>%s</title><g class='svg-flow'>%s%s%s</g></svg>")%(W,H,t,t,"".join(boxes),"".join(arr),cap)

def main():
    files=sorted(p for p in glob.glob(os.path.join(SRC,"*.json")) if not os.path.basename(p).startswith("_"))
    titles={}
    for e in json.load(open(os.path.join(ROOT,"data","site_entries.json"),encoding="utf-8"))["entries"]:
        titles[e["id"]]=e["title"]
    n=0; bad=[]
    for p in files:
        try:
            d=json.load(open(p,encoding="utf-8"))
        except Exception as ex:
            bad.append((os.path.basename(p),"JSON:%s"%str(ex)[:50])); continue
        items = d.get("entries", [d]) if isinstance(d,dict) else d
        for it in items:
            eid=it.get("id")
            if not eid or eid not in titles: bad.append((p,"bad id %s"%eid)); continue
            sec=it.get("sections",{})
            need=["时代背景","风格特征","代表人物与作品","技法或形式分析","与前后风格的关系和争论","一图","待核实"]
            if any(not sec.get(k) for k in need): bad.append((eid,"缺节")); continue
            sec["一图"]=sec["一图"] or "下图为抽象脉络示意图。"
            overlay={"id":eid,"level":"L2","sections":sec,
                     "svg":render_svg(it.get("diagram",{}),titles[eid])}
            json.dump(overlay,open(os.path.join(DST,eid+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
            n+=1
    print("l2 overlays written=%d bad=%d"%(n,len(bad)))
    for b in bad[:20]: print("  ",b)

if __name__=="__main__": main()
