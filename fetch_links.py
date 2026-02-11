import requests

def update_m3u():
    # ในอนาคตคุณสามารถเขียนฟังก์ชันดึงลิงก์ (Scraping) มาใส่ตรงนี้ได้
    # ตอนนี้เราจะใช้โครงสร้างมาตรฐานที่คุณมีก่อน
    
    content = """#EXTM3U url-tvg="https://iptv-org.github.io/guide/th.xml" refresh="3600"
#EXTINF:-1 tvg-id="ch3.th" tvg-logo="https://api.bananabatman.org/images/png/hd-ch3.png" group-title="ทีวีออนไลน์",Ch3
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)
#EXTVLCOPT:http-referrer=https://ch3plus.com/
https://ch3-33-web.cdn.byteark.com/live/playlist_720p/index.m3u8
#EXTINF:-1 tvg-id="ThaiPBS" tvg-logo="https://api.bananacake.org/images/png/hd-tpbs.png" group-title="ทีวีออนไลน์",Thai PBS
https://thaipbs-live.cdn.byteark.com/live/playlist.m3u8|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)
"""
    
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write(content)
    print("Playlist updated successfully!")

if __name__ == "__main__":
    update_m3u()
