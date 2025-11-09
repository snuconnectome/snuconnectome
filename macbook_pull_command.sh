#!/bin/bash
# MacBook Pro에서 실행할 Git Pull 스크립트

echo "=========================================="
echo "MacBook Pro Git Pull 스크립트"
echo "=========================================="
echo ""

# 저장소 디렉토리 확인
if [ ! -d ".git" ]; then
    echo "현재 디렉토리가 Git 저장소가 아닙니다."
    echo ""
    echo "저장소를 clone하려면:"
    echo "  cd ~/Desktop"
    echo "  git clone https://github.com/snuconnectome/snuconnectome.git"
    echo "  cd snuconnectome"
    echo "  git pull origin main"
    exit 1
fi

echo "현재 브랜치 확인..."
CURRENT_BRANCH=$(git branch --show-current)
echo "현재 브랜치: $CURRENT_BRANCH"
echo ""

echo "Remote 저장소 확인..."
git remote -v
echo ""

echo "최신 변경사항 가져오기..."
git fetch origin
echo ""

echo "현재 상태 확인..."
git status
echo ""

echo "최신 변경사항 병합..."
git pull origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "=========================================="
    echo "✓ Pull 완료!"
    echo "=========================================="
    echo ""
    echo "최신 커밋:"
    git log --oneline -3
else
    echo ""
    echo "❌ Pull 실패"
    echo "충돌이 있거나 다른 문제가 발생했습니다."
fi

