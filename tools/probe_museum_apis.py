# -*- coding: utf-8 -*-
"""探测博物馆/权威词表开放 API（可用于权威结构化事实与术语定义）。"""
import subprocess
URLS=[
 ("Met object","https://collectionapi.metmuseum.org/public/collection/v1/objects/436535"),
 ("Met search","https://collectionapi.metmuseum.org/public/collection/v1/search?q=monet&hasImages=false"),
 ("ArtIC","https://api.artic.edu/api/v1/artworks/search?q=monet&limit=1"),
 ("Cleveland","https://openaccess-api.clevelandart.org/api/artworks/?q=monet&limit=1"),
 ("Getty AAT","https://vocab.getty.edu/aat/300056033.json"),
 ("Getty site","https://www.getty.edu/research/tools/vocabularies/aat/"),
 ("SMK","https://api.smk.dk/api/v1/art/search/?keys=monet&offset=0&rows=1"),
 ("CooperHewitt","https://api.collection.cooperhewitt.org/rest/?method=cooperhewitt.search.objects&query=monet&per_page=1"),
 ("Rijks API","https://www.rijksmuseum.nl/api/en/collection?key=0fiuZFh4&q=rembrandt"),
 ("Harvard","https://api.harvardartmuseums.org/object?apikey=test&q=monet"),
 ("Europeana API","https://api.europeana.eu/record/v2/search.json?wskey=api2demo&query=monet"),
 ("Smithsonian","https://api.si.edu/openaccess/api/v1.0/search?q=monet&api_key=test"),
 ("V&A","https://api.vam.ac.uk/v2/objects/search?q=monet"),
 ("Walters","https://api.thewalters.org/v1/objects?apikey=test"),
]
for name,u in URLS:
    p=subprocess.run(["curl","-sSL","-m","18","-A","Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                      "-o","/tmp/pr.out","-w","%{http_code} %{size_download}",u],capture_output=True,text=True)
    out=(p.stdout or "").strip()
    hint=""
    try:
        raw=open("/tmp/pr.out","rb").read(1200)
        txt=raw.decode("utf-8","replace").lower()
        if "client challenge" in txt or "__paris" in txt: hint=" [ANTI-BOT]"
        elif txt.lstrip().startswith("{") or txt.lstrip().startswith("["): hint=" [JSON]"
        elif "<html" in txt: hint=" [html]"
    except Exception as e: hint=" [read-err]"
    print("%-14s %s%s"%(name,out,hint))