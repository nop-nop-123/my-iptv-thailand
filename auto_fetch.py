import requests
import re

OUTPUT="playlist.m3u"

# 🇹🇭 Thai-only sources
SOURCES=[
"https://iptv-org.github.io/iptv/countries/th.m3u",
"https://raw.githubusercontent.com/iptv-org/iptv/master/streams/th.m3u"
]

TARGET=[
"ch3",
"thairath",
"mono29",
"ch5",
"gmm25",
"ch8",
"workpoint",
"thaipbs",
"mcot"
]

def alive(url):
    try:
        r=requests.get(url,timeout=6)
        return r.status_code==200 and "#EXTM3U" not in r.text[:50]
    except:
        return False

found={}

for src in SOURCES:
    print("Scanning",src)
    try:
        txt=requests.get(src,timeout=10).text.splitlines()

        for i,l in enumerate(txt):
            if l.startswith("#EXTINF"):
                name=l.lower()

                for t in TARGET:
                    if t in name and t not in found:
                        url=txt[i+1]

                        if url.startswith("http") and alive(url):
                            found[t]=(l,url)
                            print("✔",t)
    except:
        pass

# rebuild playlist
out=['#EXTM3U url-tvg="https://iptv-org.github.io/guide/th.xml"']

for v in found.values():
    out.append(v[0])
    out.append(v[1])

open(OUTPUT,"w").write("\n".join(out))
print("Done:",len(found),"channels")

