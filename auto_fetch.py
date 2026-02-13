import requests,time

OUTPUT="playlist.m3u"

SOURCES=[
"https://iptv-org.github.io/iptv/countries/th.m3u",
"https://raw.githubusercontent.com/iptv-org/iptv/master/streams/th.m3u"
]

TARGET=[
"ch3","thairath","mono29","ch5",
"gmm25","ch8","workpoint","thaipbs","mcot"
]

def score(url):
    try:
        t=time.time()
        r=requests.get(url,timeout=6)
        latency=time.time()-t

        if r.status_code==200 and "#EXTM3U" not in r.text[:40]:
            return latency
    except:
        pass
    return 999

found={}

for src in SOURCES:
    print("Scan:",src)
    try:
        lines=requests.get(src,timeout=10).text.splitlines()

        for i,l in enumerate(lines):
            if l.startswith("#EXTINF"):
                low=l.lower()

                for t in TARGET:
                    if t in low:
                        url=lines[i+1]

                        if url.startswith("http"):
                            s=score(url)

                            if s<999:
                                if t not in found or s<found[t][2]:
                                    found[t]=(l,url,s)
    except:
        pass

# build playlist with fallback
out=['#EXTM3U url-tvg="https://iptv-org.github.io/guide/th.xml"']

for t,v in found.items():
    out.app

