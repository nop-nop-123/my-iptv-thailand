import requests

def check_link(url):
    try:
        # ใช้คำสั่ง HEAD เพื่อความรวดเร็ว (ไม่โหลดไฟล์วิดีโอมาทั้งไฟล์)
        response = requests.head(url, timeout=5, allow_redirects=True)
        return response.status_code == 200
    except:
        return False

def update_m3u():
    input_file = "playlist.m3u"
    updated_lines = []
    
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # ถ้าเจอแถวที่เป็นรายละเอียดช่อง (#EXTINF) ให้เช็กบรรทัดถัดไปที่เป็น URL
        if line.startswith("#EXTINF"):
            info_line = line
            url_line = lines[i+1].strip()
            
            print(f"Checking: {url_line}")
            if check_link(url_line):
                updated_lines.append(info_line + "\n")
                updated_lines.append(url_line + "\n")
            else:
                print(f"--- Dead link removed: {url_line} ---")
            
            i += 2
        elif line.startswith("#EXTM3U"):
            updated_lines.append(line + "\n")
            i += 1
        else:
            i += 1

    with open(input_file, "w", encoding="utf-8") as f:
        f.writelines(updated_lines)

if __name__ == "__main__":
    update_m3u()
