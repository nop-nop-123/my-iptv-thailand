import requests

OUTPUT="playlist.m3u"
ORIGINAL="playlist.m3u"

sources=[
"https://iptv-org.github.io/iptv/countries/th.m3u"
]

def alive(url):
    try:
        return requests.get(url,timeout=5).status_code==200
    except:
        return False

# อ่านไฟล์เดิม
with open(ORIGINAL) as f:
    old=f.readlines()

new=[]
i=0
while i<len(old):
    line=old[i]
    if line.startswith("#EXTINF"):
        url=old[i+1].strip() if i+1<len(old) else ""
        if url.startswith("http") and alive(url):
            new.append(line.strip())
            new.append(url)
        else:
            # 🔵 เก็บช่องไว้ (ไม่ลบ)
            new.append(line.strip())
            new.append(url)
        i+=2
    else:
        i+=1

open(OUTPUT,"w").write("\n".join(new))
print("SAFE update done")
"channels")
