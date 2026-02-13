import requests

playlist="playlist.m3u"

def alive(url):
    try:
        return requests.get(url,timeout=5).status_code==200
    except:
        return False

with open(playlist) as f:
    lines=f.readlines()

out=[]
i=0

while i<len(lines):
    line=lines[i]

    if line.startswith("#EXTINF"):
        url=lines[i+2].strip() if lines[i+1].startswith("#KODIPROP") else lines[i+1].strip()

        if url.startswith("http"):
            if not alive(url):
                print("DEAD:",url)

        out.append(line.rstrip())
        if lines[i+1].startswith("#KODIPROP"):
            out.append(lines[i+1].rstrip())
            out.append(url)
            i+=3
        else:
            out.append(url)
            i+=2
    else:
        out.append(line.rstrip())
        i+=1

open(playlist,"w").write("\n".join(out))
print("Finished — nothing deleted")
