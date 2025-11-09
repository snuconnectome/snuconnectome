#!/usr/bin/env python3
"""
표가 제대로 포함된 PDF 생성
LibreOffice Writer 문서를 직접 생성
"""

import subprocess
import os

# LibreOffice Writer 매크로를 사용하여 표 삽입
# 또는 ODT 파일을 직접 생성

print("표가 포함된 PDF를 생성합니다...")

# 1. 먼저 정리된 텍스트 파일 생성
os.system("python3 final_clean_for_pdf.py")

# 2. LibreOffice Writer로 ODT 생성
print("ODT 파일 생성 중...")
subprocess.run([
    "libreoffice", "--headless", "--convert-to", "odt",
    "워크샵_제출_자료_final.txt", "--outdir", "."
], check=True)

print("ODT 파일 생성 완료. 이제 표를 수동으로 삽입해야 합니다.")
print("또는 LibreOffice Writer에서 CSV 파일을 열어 표로 변환한 후 문서에 삽입하세요.")

