import requests

def check_link(url):
    # แยกเอาแค่ URL จริงๆ ก่อนถึงตัว | (Pipe) เพื่อไม่ให้สคริปต์พัง
    clean_url = url.split('|')[0].strip()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    try:
        # ใช้คำสั่ง GET แบบ stream เพื่อเช็กสถานะโดยไม่โหลดไฟล์เต็ม
        response = requests.get(clean_url, headers=headers, timeout=10, stream=True)
        return response.status_code == 200
    except:
        return False

def update_m3u():
    filename = "playlist.m3u"
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except:
        print("ไม่พบไฟล์ playlist.m3u")
        return

    new_content = ["#EXTM3U\n"]
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("#EXTINF"):
            info = line
            if i + 1 < len(lines):
                url = lines[i+1].strip()
                print(f"กำลังเช็ค: {url.split('|')[0][:50]}...") # แสดง Log สั้นๆ
                if check_link(url):
                    new_content.append(info + "\n")
                    new_content.append(url + "\n")
                else:
                    print(">>> ลิงก์ตาย: คัดออก")
            i += 2
        else:
            i += 1

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(new_content)
    print("อัปเดตเรียบร้อย!")

if __name__ == "__main__":
    update_m3u()update_m3u()update_m3u()update_m3u()update_m3u()
