import requests

def check_link(url):
    # แยกเอาแค่ URL จริงๆ ก่อนถึงตัว | (Pipe)
    clean_url = url.split('|')[0].strip()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    try:
        # ใช้สิทธิ์เข้าถึงแบบดึงข้อมูลบางส่วนเพื่อความเร็ว
        response = requests.get(clean_url, headers=headers, timeout=15, stream=True)
        return response.status_code == 200
    except:
        return False

def update_m3u():
    filename = "playlist.m3u"
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except:
        return

    new_content = ["#EXTM3U\n"]
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("#EXTINF"):
            if i + 1 < len(lines):
                url = lines[i+1].strip()
                print(f"Checking: {url}")
                if check_link(url):
                    new_content.append(line + "\n")
                    new_content.append(url + "\n")
                else:
                    print(f"❌ ลิงก์เสีย: ถูกคัดออก")
            i += 2
        else:
            i += 1

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(new_content)

if __name__ == "__main__":
    update_m3u()update_m3u()update_m3u()update_m3u()
