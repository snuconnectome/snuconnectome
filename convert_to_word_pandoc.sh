#!/bin/bash
# Markdown to Word 변환 스크립트 (pandoc 사용)

MD_FILE="워크샵_제출_자료.md"
DOCX_FILE="워크샵_제출_자료.docx"

# pandoc 설치 확인
if ! command -v pandoc &> /dev/null; then
    echo "pandoc이 설치되어 있지 않습니다."
    echo "설치 중..."
    
    # Ubuntu/Debian
    if command -v apt-get &> /dev/null; then
        sudo apt-get update
        sudo apt-get install -y pandoc
    # macOS
    elif command -v brew &> /dev/null; then
        brew install pandoc
    else
        echo "패키지 매니저를 찾을 수 없습니다. 수동으로 pandoc을 설치해주세요."
        echo "Ubuntu/Debian: sudo apt-get install pandoc"
        echo "macOS: brew install pandoc"
        exit 1
    fi
fi

# 파일 존재 확인
if [ ! -f "$MD_FILE" ]; then
    echo "오류: $MD_FILE 파일을 찾을 수 없습니다."
    exit 1
fi

echo "변환 중: $MD_FILE -> $DOCX_FILE"

# pandoc으로 변환
pandoc "$MD_FILE" \
    -o "$DOCX_FILE" \
    --from markdown \
    --to docx \
    --reference-doc=/usr/share/pandoc/data/reference.docx 2>/dev/null || \
pandoc "$MD_FILE" \
    -o "$DOCX_FILE" \
    --from markdown \
    --to docx

if [ $? -eq 0 ]; then
    echo "✓ 변환 완료: $DOCX_FILE"
    echo "파일 크기: $(du -h "$DOCX_FILE" | cut -f1)"
else
    echo "✗ 변환 실패"
    exit 1
fi

