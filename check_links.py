import requests

playlist = "playlist.m3u"
lines = open(playlist).read().splitlines()

new_lines = []

for line in lines:
    if line.startswith("http"):
        try:
            r = requests.head(line, timeout=5)
            if r.status_code >= 400:
                print("Dead:", line)
                # ใส่ fallback link หรือข้าม
                continue
        except:
            print("Error:", line)
            continue
    new_lines.append(line)

open(playlist, "w").write("\n".join(new_lines))
