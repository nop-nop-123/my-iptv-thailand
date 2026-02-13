name: Auto Update IPTV

on:
  schedule:
    - cron: '0 */6 * * *' # ตั้งค่าให้รันทุกๆ 6 ชั่วโมง
  workflow_dispatch:      # อนุญาตให้กดรันเองได้ด้วยตนเอง

jobs:
  update-playlist:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3 # ดึงโค้ดจาก Repo ลงมา

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: pip install requests # ติดตั้งไลบรารีที่จำเป็น

      - name: Run Update Script
        run: python update_playlist.py # รันสคริปต์ของคุณ

      - name: Commit and Push changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add playlist.m3u
          git commit -m "Auto-update dead links" || exit 0 # คอมมิตไฟล์ที่อัปเดต
          git push
