#!/bin/bash
# Markdown to Word 변환 스크립트
# 사용법: ./convert_md_to_docx.sh [입력파일.md] [출력파일.docx]

set -e

MD_FILE="${1:-워크샵_제출_자료.md}"
DOCX_FILE="${2:-워크샵_제출_자료.docx}"

echo "=========================================="
echo "Markdown to Word 변환 스크립트"
echo "=========================================="
echo "입력 파일: $MD_FILE"
echo "출력 파일: $DOCX_FILE"
echo ""

# 파일 존재 확인
if [ ! -f "$MD_FILE" ]; then
    echo "❌ 오류: $MD_FILE 파일을 찾을 수 없습니다."
    exit 1
fi

# pandoc 설치 확인 및 설치
if ! command -v pandoc &> /dev/null; then
    echo "⚠️  pandoc이 설치되어 있지 않습니다."
    echo ""
    echo "pandoc 설치 방법:"
    echo "  Ubuntu/Debian: sudo apt-get install pandoc"
    echo "  macOS:         brew install pandoc"
    echo ""
    echo "설치 후 다시 실행해주세요."
    exit 1
fi

echo "✓ pandoc 확인됨"
echo ""

# 기존 파일 백업
if [ -f "$DOCX_FILE" ]; then
    BACKUP_FILE="${DOCX_FILE}.backup.$(date +%Y%m%d_%H%M%S)"
    echo "기존 파일 백업: $BACKUP_FILE"
    cp "$DOCX_FILE" "$BACKUP_FILE"
fi

echo "변환 중..."
echo ""

# pandoc으로 변환 (최고 품질 옵션)
pandoc "$MD_FILE" \
    -o "$DOCX_FILE" \
    --from markdown+smart \
    --to docx \
    --standalone \
    --wrap=none \
    --toc-depth=3 \
    --highlight-style=default \
    --metadata title="Active Inference and AI 학술 심리학과 학사 협의회 개최 신청서"

if [ $? -eq 0 ]; then
    echo ""
    echo "=========================================="
    echo "✓ 변환 완료!"
    echo "=========================================="
    echo "출력 파일: $DOCX_FILE"
    echo "파일 크기: $(du -h "$DOCX_FILE" | cut -f1)"
    echo ""
    echo "변환 후 확인 사항:"
    echo "  - 볼드 텍스트가 제대로 표시되는지 확인"
    echo "  - 헤더가 제목 스타일로 적용되었는지 확인"
    echo "  - 표가 제대로 표시되는지 확인"
    echo "  - 목록이 제대로 표시되는지 확인"
    echo ""
else
    echo ""
    echo "❌ 변환 실패"
    exit 1
fi

