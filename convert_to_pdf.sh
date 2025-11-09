#!/bin/bash
# Markdown/Word to PDF 변환 스크립트

INPUT_FILE="${1:-워크샵_제출_자료.md}"
OUTPUT_FILE="${2:-워크샵_제출_자료.pdf}"

echo "=========================================="
echo "PDF 변환 스크립트"
echo "=========================================="
echo "입력 파일: $INPUT_FILE"
echo "출력 파일: $OUTPUT_FILE"
echo ""

# 파일 존재 확인
if [ ! -f "$INPUT_FILE" ]; then
    echo "❌ 오류: $INPUT_FILE 파일을 찾을 수 없습니다."
    exit 1
fi

# 파일 확장자 확인
EXTENSION="${INPUT_FILE##*.}"

if [ "$EXTENSION" = "docx" ]; then
    echo "Word 파일에서 PDF 변환 중..."
    libreoffice --headless --convert-to pdf "$INPUT_FILE" --outdir . 2>&1
    
    # 변환된 파일 이름 확인
    CONVERTED_FILE="${INPUT_FILE%.docx}.pdf"
    if [ -f "$CONVERTED_FILE" ] && [ "$CONVERTED_FILE" != "$OUTPUT_FILE" ]; then
        mv "$CONVERTED_FILE" "$OUTPUT_FILE"
    fi
    
elif [ "$EXTENSION" = "md" ]; then
    echo "Markdown 파일에서 PDF 변환 중..."
    
    # pandoc 사용 (있는 경우)
    if command -v pandoc &> /dev/null; then
        echo "pandoc 사용 중..."
        pandoc "$INPUT_FILE" -o "$OUTPUT_FILE" \
            --pdf-engine=xelatex \
            --variable mainfont="NanumGothic" \
            --variable geometry:margin=1in \
            --toc \
            --toc-depth=3 2>&1 || \
        pandoc "$INPUT_FILE" -o "$OUTPUT_FILE" \
            --pdf-engine=pdflatex \
            --variable geometry:margin=1in \
            --toc \
            --toc-depth=3 2>&1 || \
        pandoc "$INPUT_FILE" -o "$OUTPUT_FILE" 2>&1
        
        if [ $? -eq 0 ]; then
            echo "✓ pandoc으로 변환 완료"
            exit 0
        fi
    fi
    
    # LibreOffice 사용
    echo "LibreOffice 사용 중..."
    libreoffice --headless --convert-to pdf "$INPUT_FILE" --outdir . 2>&1
    
    # 변환된 파일 이름 확인
    CONVERTED_FILE="${INPUT_FILE%.md}.pdf"
    if [ -f "$CONVERTED_FILE" ] && [ "$CONVERTED_FILE" != "$OUTPUT_FILE" ]; then
        mv "$CONVERTED_FILE" "$OUTPUT_FILE"
    fi
else
    echo "❌ 지원하지 않는 파일 형식: $EXTENSION"
    exit 1
fi

if [ -f "$OUTPUT_FILE" ]; then
    echo ""
    echo "=========================================="
    echo "✓ PDF 변환 완료!"
    echo "=========================================="
    echo "출력 파일: $OUTPUT_FILE"
    echo "파일 크기: $(du -h "$OUTPUT_FILE" | cut -f1)"
    echo ""
else
    echo ""
    echo "❌ PDF 변환 실패"
    exit 1
fi

