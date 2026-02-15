import requests

def check_link(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    try:
        # ใช้ timeout 10 วินาที และอนุญาตให้เปลี่ยนเส้นทาง (Redirect)
        response = requests.head(url, headers=headers, timeout=10, allow_redirects=True)
        # ถ้า Status Code อยู่ระหว่าง 200-399 ถือว่ายังใช้งานได้
        return response.status_code < 400
    except Exception as e:
        print(f"Error checking {url}: {e}")
        return False

def update_m3u():
    filename = "playlist.m3u"
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Error: playlist.m3u not found!")
        return

    new_content = []
    if lines and lines[0].strip().startswith("#EXTM3U"):
        new_content.append(lines[0])

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("#EXTINF"):
            info = line
            # ตรวจสอบบรรทัดถัดไปว่าเป็น URL หรือไม่
            if i + 1 < len(lines):
                url = lines[i+1].strip()
                print(f"Checking: {url}")
                if check_link(url):
                    new_content.append(info + "\n")
                    new_content.append(url + "\n")
                else:
                    print(f">>> Found dead link: {url}")
                i += 2
            else:
                i += 1
        else:
            i += 1

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(new_content)
    print("Update completed!")

if __name__ == "__main__":
    update_m3u()update_m3u()
