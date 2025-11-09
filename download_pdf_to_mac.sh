#!/bin/bash
# MacBook Pro로 PDF 다운로드 스크립트
# 사용법: ./download_pdf_to_mac.sh [macbook-ip] [username]

MAC_IP="${1}"
MAC_USER="${2:-$USER}"
PDF_URL="https://github.com/snuconnectome/snuconnectome/raw/main/워크샵_제출_자료.pdf"

if [ -z "$MAC_IP" ]; then
    echo "사용법: $0 <macbook-ip-address> [username]"
    echo ""
    echo "예시:"
    echo "  $0 192.168.1.100 juke"
    echo ""
    echo "또는 MacBook Pro에서 직접 실행할 명령:"
    echo "  cd ~/Desktop"
    echo "  curl -L -o '워크샵_제출_자료.pdf' '$PDF_URL'"
    exit 1
fi

echo "MacBook Pro ($MAC_IP)로 PDF 전송 중..."

# SCP를 사용하여 전송
scp "$PDF_URL" "${MAC_USER}@${MAC_IP}:~/Desktop/워크샵_제출_자료.pdf" 2>&1

if [ $? -eq 0 ]; then
    echo "✓ 전송 완료!"
else
    echo "❌ 전송 실패"
    echo ""
    echo "대안: MacBook Pro에서 직접 다운로드:"
    echo "  cd ~/Desktop"
    echo "  curl -L -o '워크샵_제출_자료.pdf' '$PDF_URL'"
fi

