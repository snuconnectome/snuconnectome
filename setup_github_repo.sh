#!/bin/bash
# GitHub Repository 생성 및 Push 스크립트

REPO_NAME="snuconnectome"
ORG_NAME="snuconnectome"

echo "=========================================="
echo "GitHub Repository 설정 스크립트"
echo "=========================================="
echo ""

# GitHub CLI 확인
if command -v gh &> /dev/null; then
    echo "✓ GitHub CLI (gh) 확인됨"
    echo ""
    echo "GitHub CLI로 repository 생성 중..."
    
    # Repository 생성
    gh repo create ${ORG_NAME}/${REPO_NAME} \
        --public \
        --description "Active Inference and AI 학술 심리학과 학사 협의회 제출 자료" \
        --source=. \
        --remote=origin \
        --push 2>&1
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "✓ Repository 생성 및 Push 완료!"
        echo "Repository URL: https://github.com/${ORG_NAME}/${REPO_NAME}"
    else
        echo ""
        echo "⚠️  Repository 생성 실패 또는 이미 존재합니다."
        echo ""
        echo "수동으로 진행하세요:"
        echo "1. https://github.com/new 에서 repository 생성"
        echo "2. Repository 이름: ${REPO_NAME}"
        echo "3. 생성 후 다음 명령 실행:"
        echo "   git remote add origin git@github.com:${ORG_NAME}/${REPO_NAME}.git"
        echo "   git push -u origin main"
    fi
else
    echo "⚠️  GitHub CLI (gh)가 설치되어 있지 않습니다."
    echo ""
    echo "설치 방법:"
    echo "  Ubuntu/Debian: sudo apt-get install gh"
    echo "  또는: https://cli.github.com/"
    echo ""
    echo "또는 수동으로 진행:"
    echo "1. https://github.com/new 에서 repository 생성"
    echo "   - Repository 이름: ${REPO_NAME}"
    echo "   - Description: Active Inference and AI 학술 심리학과 학사 협의회 제출 자료"
    echo "   - Public 또는 Private 선택"
    echo "   - README, .gitignore, license는 추가하지 않음"
    echo ""
    echo "2. 생성 후 다음 명령 실행:"
    echo "   git remote add origin git@github.com:${ORG_NAME}/${REPO_NAME}.git"
    echo "   git push -u origin main"
fi

