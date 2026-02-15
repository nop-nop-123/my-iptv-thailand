import requests

def check_link(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    try:
        # ใช้ทั้ง GET และ HEAD เพื่อความแม่นยำ (บาง Server ไม่รองรับ HEAD)
        response = requests.get(url, headers=headers, timeout=10, stream=True)
        return response.status_code == 200
    except:
        return False

def update_m3u():
    filename = "playlist.m3u"
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Error: ไม่พบไฟล์ playlist.m3u")
        return

    new_content = ["#EXTM3U\n"]
    for i in range(len(lines)):
        line = lines[i].strip()
        if line.startswith("#EXTINF"):
            if i + 1 < len(lines):
                url = lines[i+1].strip()
                print(f"กำลังเช็ค: {url}")
                if check_link(url):
                    new_content.append(line + "\n")
                    new_content.append(url + "\n")
                else:
                    print(f"--- ลิงก์เสีย ลบออก: {url} ---")
    
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(new_content)

if __name__ == "__main__":
    update_m3u()update_m3u()update_m3u()
