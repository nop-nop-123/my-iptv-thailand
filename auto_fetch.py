import requests
import re

OUTPUT = "playlist.m3u"

# 🔎 playlist sources
SOURCES = [
    "https://iptv-org.github.io/iptv/countries/th.m3u",
    "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/th.m3u"
]

CHANNELS = [
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
        r = requests.get(url, timeout=5)
        return r.status_code == 200
    except:
        return False

found = {}

for src in SOURCES:
    try:
        txt = requests.get(src, timeout=10).text
        lines = txt.splitlines()

        for i,l in enumerate(lines):
            if l.startswith("#EXTINF"):
                name = l.lower()
                for ch in CHANNELS:
                    if ch in name and ch not in found:
                        url = lines[i+1]
                        if url.startswith("http") and alive(url):
                            found[ch] = (l, url)
    except:
        pass

# write new playlist
out = ["#EXTM3U"]

for ch in found.values():
    out.append(ch[0])
    out.append(ch[1])

open(OUTPUT,"w").write("\n".join(out))
print("Updated", len(found), "channels")
