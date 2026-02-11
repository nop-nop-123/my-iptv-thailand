import requests
import re

def get_live_link(url, pattern):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(url, headers=headers, timeout=10)
        match = re.search(pattern, response.text)
        return match.group(0) if match else None
    except:
        return None

# สร้างไฟล์ playlist.m3u ใหม่
with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write('#EXTM3U url-tvg="https://iptv-org.github.io/guide/th.xml" refresh="3600"\n')
    
    # ตัวอย่าง: ช่อง 3 (ต้องใช้ Regex ที่ตรงกับโครงสร้างเว็บปัจจุบัน)
    ch3_live = get_live_link("https://ch3plus.com/live", r'https://.*\.m3u8.*?(?=")')
    if ch3_live:
        f.write('#EXTINF:-1 tvg-id="ch3.th" tvg-logo="https://api.bananabatman.org/images/png/hd-ch3.png", Ch3\n')
        f.write(f"{ch3_live}|User-Agent=Mozilla/5.0...\n")

    # สำหรับช่องที่ลิงก์ไม่ตาย (เช่น Thai PBS) ก็เขียนลงไปตรงๆ ได้เลย
    f.write('#EXTINF:-1 tvg-id="ThaiPBS" tvg-logo="...", Thai PBS\n')
    f.write('https://thaipbs-live.cdn.byteark.com/live/playlist.m3u8|User-Agent=Mozilla/5.0...\n')
