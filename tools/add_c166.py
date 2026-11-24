# -*- coding: utf-8 -*-
"""Cycle166：comparative 2 条（中世纪、古典主义的美术-音乐对照）。仅用库内已有概述与来源，不引入新事实。"""
import io,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T=[
 ('medieval-crossmedia','中世纪：石构教堂与圣咏的并行','风格','comparative','中世纪','欧洲','综合','重要',
  '比较中世纪视觉艺术（罗马式、哥特式）与中世纪音乐（圣咏、复调）在宗教场所中的各自表现。','约5—15世纪',
  '建筑与雕塑以半圆拱、尖拱与彩色玻璃为标志，音乐以单声部圣咏为主、晚期出现复调；两者都主要服务于教会。',
  'romanesque,gothic,medieval-music,gregorian-chant','enc-romanesque,enc-gothic,enc-medieval-music,enc-gregorian-chant'),
 ('classical-crossmedia','古典主义：新古典主义美术与古典时期音乐','风格','comparative','18—19世纪初','欧洲','综合','重要',
  '比较新古典主义美术与古典时期音乐在克制、清晰与秩序上的共同取向。','约18世纪中后期—19世纪初',
  '美术以对称构图与清晰轮廓回归古典形式，音乐以均衡、清晰与奏鸣曲式确立交响曲等范式；两者的断代与内涵并不完全重合。',
  'neoclassicism,classical-period-music','enc-neoclassicism,enc-classical-period-music'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
txt="\n".join(lines)
T=[t for t in T if "'%s'"%t[0] not in txt]
if T:
    close=max(i for i,l in enumerate(lines) if l.strip()=="]")
    lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
    io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended",len(T))
