import requests

def check_link(url):
    try:
        # ตัดส่วนที่เป็น User-Agent ออกเพื่อเอาแค่ URL บริสุทธิ์ไปเช็ก
        clean_url = url.split('|')[0].strip()
        headers = {'User-Agent': 'Mozilla/5.0'}
        # เช็กสถานะด้วย GET (เพิ่ม timeout เป็น 15 วินาที)
        r = requests.get(clean_url, headers=headers, timeout=15, stream=True)
        return r.status_code == 200
    except:
        return False

def main():
    file_path = "playlist.m3u"
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except:
        return

    new_lines = ["#EXTM3U\n"]
    for i in range(len(lines)):
        line = lines[i].strip()
        if line.startswith("#EXTINF"):
            if i + 1 < len(lines):
                url = lines[i+1].strip()
                if check_link(url):
                    new_lines.append(line + "\n")
                    new_lines.append(url + "\n")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    main()update_m3u()update_m3u()update_m3u()update_m3u()update_m3u()update_m3u()
