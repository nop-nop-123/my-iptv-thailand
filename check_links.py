import requests

def check_link(url):
    # แยกเอาแค่ URL จริงๆ ก่อนถึงตัว | (Pipe) เพื่อป้องกัน Error
    clean_url = url.split('|')[0].strip()
    
    # ดึง User-Agent จากลิงก์มาใช้ (ถ้ามี) เพื่อให้การเช็กแม่นยำขึ้น
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    if '|User-Agent=' in url:
        headers['User-Agent'] = url.split('|User-Agent=')[1].split('|')[0]

    try:
        # เช็กสถานะลิงก์ (timeout 15 วินาที เพื่อรองรับ Server ที่ตอบสนองช้า)
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
        print("ไม่พบไฟล์ playlist.m3u")
        return

    new_content = ["#EXTM3U\n"]
    i = 0
    print(f"กำลังเริ่มตรวจสอบลิงก์ทั้งหมด...")
    
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("#EXTINF"):
            info = line
            if i + 1 < len(lines):
                url = lines[i+1].strip()
                # ตรวจสอบสถานะลิงก์
                if check_link(url):
                    print(f"✅ ผ่าน: {url[:50]}...")
                    new_content.append(info + "\n")
                    new_content.append(url + "\n")
                else:
                    print(f"❌ เสีย (ลบออก): {url[:50]}...")
            i += 2
        else:
            i += 1

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(new_content)
    print("อัปเดตไฟล์สำเร็จ!")

if __name__ == "__main__":
    update_m3u()update_m3u()update_m3u()update_m3u()update_m3u()update_m3u()
