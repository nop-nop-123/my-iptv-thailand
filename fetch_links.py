import requests
import re

def get_ch3_link():
    try:
        # จำลองตัวตนว่าเป็น Browser เพื่อให้เว็บยอมให้เข้าถึง
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Referer': 'https://ch3plus.com/'
        }
        # 1. เข้าไปที่หน้าเว็บหลักของช่อง 3
        response = requests.get("https://ch3plus.com/live", headers=headers, timeout=15)
        
        # 2. ใช้ Regex ค้นหาลิงก์ m3u8 ที่มี Token (x_ark_...) ติดมาด้วย
        # Pattern นี้จะมองหา URL ที่ขึ้นต้นด้วย https และลงท้ายด้วย .m3u8 พร้อมพารามิเตอร์
        found = re.search(r'https://[\w-]+\.cdn\.byteark\.com/live/[^"\']+\.m3u8[^\s"\']*', response.text)
        
        if found:
            return found.group(0)
    except Exception as e:
        print(f"Error fetching Ch3: {e}")
    return None

def main():
    ch3_url = get_ch3_link()
    
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write('#EXTM3U url-tvg="https://iptv-org.github.io/guide/th.xml" refresh="3600"\n')
        
        if ch3_url:
            f.write('#EXTINF:-1 tvg-id="ch3.th" tvg-logo="https://api.bananabatman.org/images/png/hd-ch3.png" group-title="ทีวีออนไลน์",Ch3\n')
            f.write('#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)\n')
            f.write('#EXTVLCOPT:http-referrer=https://ch3plus.com/\n')
            f.write(f"{ch3_url}|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)&Referer=https://ch3plus.com/\n")
        else:
            # ถ้าดึงไม่ได้ ให้ใส่ลิงก์สำรองหรือลิงก์เดิมไว้ก่อน
            f.write('#EXTINF:-1 tvg-id="ch3.th", Ch3 (Update Failed)\n')
            f.write('https://ch3-33-web.cdn.byteark.com/live/playlist_720p/index.m3u8\n')

        # เพิ่มช่องอื่นๆ ที่ลิงก์ไม่ตายตัวลงไปได้เลย
        f.write('#EXTINF:-1 tvg-id="ThaiPBS" tvg-logo="https://api.bananacake.org/images/png/hd-tpbs.png", Thai PBS\n')
        f.write('https://thaipbs-live.cdn.byteark.com/live/playlist.m3u8|User-Agent=Mozilla/5.0\n')

if __name__ == "__main__":
    main()
