# -*- coding: utf-8 -*-
"""构建 sources.json：先落盘候选来源，再联网核对标题/作者/年份后标记 verified。"""
import json, os, re, ssl, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
os.makedirs(DATA, exist_ok=True)

# (id, title, author, year, url, type, check_keyword)
# check_keyword 出现在抓取页 <title> 或正文前部才置 verified=true
RAW = [
 # ---- 权威百科：西方艺术 ----
 ("enc-prehistoric-art","Prehistoric art","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Prehistoric_art","权威百科","Prehistoric art"),
 ("enc-egyptian-art","Ancient Egyptian art","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Ancient_Egyptian_art","权威百科","Ancient Egyptian art"),
 ("enc-greek-art","Ancient Greek art","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Ancient_Greek_art","权威百科","Ancient Greek art"),
 ("enc-roman-art","Ancient Roman art","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Ancient_Roman_art","权威百科","Ancient Roman art"),
 ("enc-byzantine-art","Byzantine art","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Byzantine_art","权威百科","Byzantine art"),
 ("enc-medieval-art","Medieval art","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Medieval_art","权威百科","Medieval art"),
 ("enc-romanesque","Romanesque art","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Romanesque_art","权威百科","Romanesque"),
 ("enc-gothic","Gothic art","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Gothic_art","权威百科","Gothic art"),
 ("enc-renaissance","Renaissance","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Renaissance","权威百科","Renaissance"),
 ("enc-italian-renaissance-painting","Italian Renaissance painting","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Italian_Renaissance_painting","权威百科","Italian Renaissance painting"),
 ("enc-high-renaissance","High Renaissance","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/High_Renaissance","权威百科","High Renaissance"),
 ("enc-venetian-school","Venetian school (art)","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Venetian_school_(art)","权威百科","Venetian school"),
 ("enc-northern-renaissance","Northern Renaissance","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Northern_Renaissance","权威百科","Northern Renaissance"),
 ("enc-mannerism","Mannerism","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Mannerism","权威百科","Mannerism"),
 ("enc-baroque","Baroque","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Baroque","权威百科","Baroque"),
 ("enc-rococo","Rococo","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Rococo","权威百科","Rococo"),
 ("enc-neoclassicism","Neoclassicism","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Neoclassicism","权威百科","Neoclassicism"),
 ("enc-romanticism","Romanticism","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Romanticism","权威百科","Romanticism"),
 ("enc-realism-art","Realism (arts)","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Realism_(arts)","权威百科","Realism"),
 ("enc-impressionism","Impressionism","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Impressionism","权威百科","Impressionism"),
 ("enc-post-impressionism","Post-Impressionism","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Post-Impressionism","权威百科","Post-Impressionism"),
 ("enc-symbolism","Symbolism (arts)","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Symbolism_(arts)","权威百科","Symbolism"),
 ("enc-art-nouveau","Art Nouveau","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Art_Nouveau","权威百科","Art Nouveau"),
 ("enc-fauvism","Fauvism","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Fauvism","权威百科","Fauvism"),
 ("enc-expressionism","Expressionism","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Expressionism","权威百科","Expressionism"),
 ("enc-cubism","Cubism","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Cubism","权威百科","Cubism"),
 ("enc-futurism","Futurism","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Futurism","权威百科","Futurism"),
 ("enc-dada","Dada","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Dada","权威百科","Dada"),
 ("enc-surrealism","Surrealism","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Surrealism","权威百科","Surrealism"),
 ("enc-bauhaus","Bauhaus","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Bauhaus","权威百科","Bauhaus"),
 ("enc-abstract-expressionism","Abstract expressionism","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Abstract_expressionism","权威百科","Abstract expressionism"),
 ("enc-pop-art","Pop art","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Pop_art","权威百科","Pop art"),
 ("enc-minimalism","Minimalism","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Minimalism","权威百科","Minimalism"),
 ("enc-conceptual-art","Conceptual art","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Conceptual_art","权威百科","Conceptual art"),
 ("enc-contemporary-art","Contemporary art","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Contemporary_art","权威百科","Contemporary art"),
 # ---- 权威百科：艺术家 ----
 ("enc-leonardo","Leonardo da Vinci","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Leonardo_da_Vinci","权威百科","Leonardo da Vinci"),
 ("enc-michelangelo","Michelangelo","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Michelangelo","权威百科","Michelangelo"),
 ("enc-raphael","Raphael","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Raphael","权威百科","Raphael"),
 ("enc-donatello","Donatello","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Donatello","权威百科","Donatello"),
 ("enc-botticelli","Sandro Botticelli","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Sandro_Botticelli","权威百科","Botticelli"),
 ("enc-rembrandt","Rembrandt","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Rembrandt","权威百科","Rembrandt"),
 ("enc-rubens","Peter Paul Rubens","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Peter_Paul_Rubens","权威百科","Rubens"),
 ("enc-velazquez","Diego Velazquez","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Diego_Velazquez","权威百科","Velazquez"),
 ("enc-vermeer","Johannes Vermeer","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Johannes_Vermeer","权威百科","Vermeer"),
 ("enc-caravaggio","Caravaggio","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Caravaggio","权威百科","Caravaggio"),
 ("enc-monet","Claude Monet","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Claude_Monet","权威百科","Monet"),
 ("enc-van-gogh","Vincent van Gogh","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Vincent_van_Gogh","权威百科","van Gogh"),
 ("enc-cezanne","Paul Cezanne","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Paul_Cezanne","权威百科","Cezanne"),
 ("enc-gauguin","Paul Gauguin","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Paul_Gauguin","权威百科","Gauguin"),
 ("enc-picasso","Pablo Picasso","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Pablo_Picasso","权威百科","Picasso"),
 ("enc-matisse","Henri Matisse","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Henri_Matisse","权威百科","Matisse"),
 ("enc-kandinsky","Wassily Kandinsky","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Wassily_Kandinsky","权威百科","Kandinsky"),
 ("enc-dali","Salvador Dali","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Salvador_Dali","权威百科","Dali"),
 ("enc-warhol","Andy Warhol","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Andy_Warhol","权威百科","Warhol"),
 # ---- 权威百科：西方音乐 ----
 ("enc-medieval-music","Medieval music","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Medieval_music","权威百科","Medieval music"),
 ("enc-renaissance-music","Renaissance music","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Renaissance_music","权威百科","Renaissance music"),
 ("enc-baroque-music","Baroque music","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Baroque_music","权威百科","Baroque music"),
 ("enc-classical-period-music","Classical period (music)","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Classical_period_(music)","权威百科","Classical period"),
 ("enc-romantic-music","Romantic music","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Romantic_music","权威百科","Romantic music"),
 ("enc-20th-century-classical","20th-century classical music","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/20th-century_classical_music","权威百科","20th-century classical music"),
 ("enc-opera","Opera","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Opera","权威百科","Opera"),
 ("enc-symphony","Symphony","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Symphony","权威百科","Symphony"),
 ("enc-sonata","Sonata","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Sonata","权威百科","Sonata"),
 ("enc-fugue","Fugue","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Fugue","权威百科","Fugue"),
 ("enc-gregorian-chant","Gregorian chant","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Gregorian_chant","权威百科","Gregorian chant"),
 ("enc-polyphony","Polyphony","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Polyphony","权威百科","Polyphony"),
 ("enc-tonality","Tonality","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Tonality","权威百科","Tonality"),
 ("enc-serialism","Serialism","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Serialism","权威百科","Serialism"),
 ("enc-bach","Johann Sebastian Bach","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Johann_Sebastian_Bach","权威百科","Johann Sebastian Bach"),
 ("enc-mozart","Wolfgang Amadeus Mozart","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Wolfgang_Amadeus_Mozart","权威百科","Mozart"),
 ("enc-beethoven","Ludwig van Beethoven","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Ludwig_van_Beethoven","权威百科","Beethoven"),
 ("enc-haydn","Joseph Haydn","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Joseph_Haydn","权威百科","Haydn"),
 ("enc-chopin","Frederic Chopin","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Fr%C3%A9d%C3%A9ric_Chopin","权威百科","Chopin"),
 ("enc-wagner","Richard Wagner","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Richard_Wagner","权威百科","Wagner"),
 ("enc-stravinsky","Igor Stravinsky","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Igor_Stravinsky","权威百科","Stravinsky"),
 ("enc-schoenberg","Arnold Schoenberg","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Arnold_Schoenberg","权威百科","Schoenberg"),
 # ---- 权威百科：中国艺术与音乐 ----
 ("enc-chinese-painting","Chinese painting","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Chinese_painting","权威百科","Chinese painting"),
 ("enc-chinese-calligraphy","Chinese calligraphy","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Chinese_calligraphy","权威百科","Chinese calligraphy"),
 ("enc-tang-dynasty-art","Art of the Tang dynasty","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Art_of_the_Tang_dynasty","权威百科","Tang dynasty"),
 ("enc-song-dynasty-art","Art of the Song dynasty","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Art_of_the_Song_dynasty","权威百科","Song dynasty"),
 ("enc-yuan-dynasty-art","Art of the Yuan dynasty","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Art_of_the_Yuan_dynasty","权威百科","Yuan dynasty"),
 ("enc-chinese-music","Chinese music","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Chinese_music","权威百科","Chinese music"),
 ("enc-guzheng","Guzheng","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Guzheng","权威百科","Guzheng"),
 ("enc-jingju","Beijing opera","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Beijing_opera","权威百科","Beijing opera"),
 # ---- 官方机构 / 学术项目 ----
 ("inst-met-heilbrunn","Heilbrunn Timeline of Art History","Metropolitan Museum of Art","2026","https://www.metmuseum.org/toah/","官方机构","Heilbrunn"),
 ("inst-khan-art","Khan Academy Art History","Khan Academy","2026","https://www.khanacademy.org/humanities/art-history","官方机构","Art History"),
 ("inst-tate-art-terms","Tate Art & Artists glossary","Tate","2026","https://www.tate.org.uk/art/art-terms","官方机构","Art terms"),
 ("inst-nga-glossary","National Gallery of Art glossary","National Gallery of Art","2026","https://www.nga.gov/artworks","官方机构","National Gallery"),
 ("web-artstory-movements","Classical and Modern Art Movements","The Art Story Foundation","2026","https://www.theartstory.org/movements/","权威百科","Movements"),
 ("web-artstory-impressionism","Impressionism — Art Movement","The Art Story Foundation","2026","https://www.theartstory.org/movement/impressionism/","权威百科","Impressionism"),
 ("web-artstory-cubism","Cubism — Art Movement","The Art Story Foundation","2026","https://www.theartstory.org/movement/cubism/","权威百科","Cubism"),
]

def verify(item):
    sid, title, author, year, url, typ, kw = item
    ctx = ssl.create_default_context()
    try:
        req = urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0 (compatible; YishuBot/1.0)"})
        with urllib.request.urlopen(req, timeout=25, context=ctx) as r:
            html = r.read(400000).decode("utf-8","ignore")
            status = r.status
        head = html[:60000]
        ok = (status < 400) and (kw.lower() in head.lower())
        note = ("HTTP %d；标题关键词[%s]命中" % (status, kw)) if ok else \
               ("HTTP %d；未命中关键词[%s]" % (status, kw))
        return sid, ok, note, status
    except urllib.error.HTTPError as e:
        return sid, False, "HTTP %d %s" % (e.code, e.reason), e.code
    except Exception as e:
        return sid, False, "%s: %s" % (type(e).__name__, str(e)[:80]), None

def main():
    sources = []
    for sid,title,author,year,url,typ,kw in RAW:
        sources.append({"id":sid,"title":title,"author":author,"year":year,
                        "url":url,"type":typ,"verified":False,
                        "verified_note":"待核验"})
    results = {}
    with ThreadPoolExecutor(max_workers=10) as ex:
        futs = {ex.submit(verify,it): it[0] for it in RAW}
        for f in as_completed(futs):
            try:
                sid, ok, note, status = f.result()
                results[sid] = (ok, note, status)
            except Exception as e:
                results[futs[f]] = (False, "核验异常: %s" % str(e)[:60], None)
    n_ok = 0
    for s in sources:
        if s["id"] in results:
            ok, note, status = results[s["id"]]
            s["verified"] = bool(ok)
            s["verified_note"] = note
            if ok: n_ok += 1
    with open(os.path.join(DATA,"sources.json"),"w",encoding="utf-8") as f:
        json.dump({"sources":sources}, f, ensure_ascii=False, indent=2)
    print("sources total=%d verified=%d" % (len(sources), n_ok))
    bad = [s["id"] for s in sources if not s["verified"]]
    print("unverified:", ", ".join(bad) if bad else "(none)")

if __name__ == "__main__":
    main()
