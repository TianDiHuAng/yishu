# -*- coding: utf-8 -*-
"""探测一批可能的内容来源（艺术史/音乐史），逐个取 HTTP 状态与大小。
目的：找出能读到**正文**的站点，以便在不降低标准的前提下扩充。"""
import subprocess
URLS=[
 ("Gutenberg","https://www.gutenberg.org/ebooks/subject/2786"),
 ("Gutenberg raw","https://www.gutenberg.org/cache/epub/30755/pg30755.txt"),
 ("Standard Ebooks","https://standardebooks.org/ebooks"),
 ("Getty","https://www.getty.edu/publications/virtuallibrary/"),
 ("Smarthistory","https://smarthistory.org/"),
 ("WikiArt","https://www.wikiart.org/en/paintings-by-style"),
 ("MoMA","https://www.moma.org/collection/"),
 ("NGA","https://www.nga.gov/education/teachers/lessons-activities.html"),
 ("Rijksmuseum","https://www.rijksmuseum.nl/en/rijksstudio"),
 ("Europeana","https://www.europeana.eu/en/search?query=impressionism"),
 ("UNESCO WHC","https://whc.unesco.org/en/list/"),
 ("ICOMOS","https://www.icomos.org/en"),
 ("Gallica","https://gallica.bnf.fr/"),
 ("Persee","https://www.persee.fr/"),
 ("OpenEdition","https://books.openedition.org/"),
 ("Britannica alt","https://www.britannica.com/art/Gothic-architecture"),
 ("Artsy","https://www.artsy.net/"),
 ("Khan dev","https://cdn.kastatic.org/"),
]
for name,u in URLS:
    p=subprocess.run(["curl","-sS","-m","15","-A","Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                      "-o","/tmp/probe.out","-w","%{http_code} %{size_download}",u],
                     capture_output=True,text=True)
    out=(p.stdout or "").strip()
    hint=""
    try:
        head=open("/tmp/probe.out",encoding="utf-8",errors="replace").read(400).lower()
        if "client challenge" in head or "__paris" in head or "captcha" in head: hint=" [ANTI-BOT SHELL]"
        elif "<html" in head: hint=" [html]"
        elif len(head.strip())>0: hint=" [text]"
    except Exception: pass
    print("%-16s %s%s"%(name,out,hint))