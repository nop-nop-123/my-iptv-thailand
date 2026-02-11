import requests
import re

def get_live_link(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Referer': 'https://ch3plus.com/'
        }
        # ดึงหน้าเว็บต้นทาง
        response = requests.get(url, headers=headers, timeout=15)
        # ใช้ Regex ค้นหาลิงก์ .m3u8 ที่มี Token ติดมาด้วย
        match = re.search(r'https://[\w-]+\.cdn\.byteark\.com/live/[^"\']+\.m3u8[^\s"\']*', response.text)
        return match.group(0) if match else None
    except:
        return None

def update_playlist():
    ch3_link = get_live_link("https://ch3plus.com/live")
    
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write('#EXTM3U url-tvg="https://iptv-org.github.io/guide/th.xml" refresh="3600"\n')
        
        if ch3_link:
            f.write('#EXTINF:-1 tvg-id="ch3.th" tvg-logo="https://api.bananabatman.org/images/png/hd-ch3.png" group-title="ทีวีออนไลน์",Ch3\n')
            f.write('#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)\n')
            f.write('#EXTVLCOPT:http-referrer=https://ch3plus.com/\n')
            f.write(f"{ch3_link}|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)&Referer=https://ch3plus.com/\n")
            
        # ใส่ช่องอื่นๆ ที่ลิงก์ไม่ค่อยเปลี่ยนตามปกติ
        f.write('#EXTINF:-1 tvg-id="ThaiPBS" tvg-logo="https://api.bananacake.org/images/png/hd-tpbs.png", Thai PBS\n')
        f.write('https://thaipbs-live.cdn.byteark.com/live/playlist.m3u8|User-Agent=Mozilla/5.0\n')

if __name__ == "__main__":
    update_playlist()
