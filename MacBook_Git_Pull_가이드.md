# MacBook Pro에서 Git Pull 가이드

## 방법 1: 기존 저장소에서 Pull

MacBook Pro의 터미널에서 저장소 디렉토리로 이동한 후:

```bash
cd ~/path/to/snuconnectome  # 저장소 디렉토리로 이동
git pull origin main
```

## 방법 2: 처음 Clone하는 경우

MacBook Pro의 터미널에서:

```bash
cd ~/Desktop
git clone https://github.com/snuconnectome/snuconnectome.git
cd snuconnectome
```

## 방법 3: 스크립트 사용

제공된 스크립트를 MacBook Pro로 복사한 후:

```bash
chmod +x macbook_pull_command.sh
./macbook_pull_command.sh
```

## 최신 커밋 확인

현재 GitHub에 있는 최신 커밋들:
- `b2b5757`: Update all files: PDF with tables, conversion scripts, and documentation
- `9e06e21`: Update PDF with professor table format
- `f749f15`: Convert professor list to table format in PDF
- `6b73e81`: Add professor list as table format in PDF
- `d495acf`: Fix PDF table format: Convert markdown table to CSV format

## 포함된 최신 파일들

- `워크샵_제출_자료.pdf` - 표 형식이 포함된 최신 PDF
- `워크샵_제출_자료.md` - 원본 마크다운 파일
- `워크샵_제출_자료.docx` - Word 파일
- `convert_with_table.py` - 표 변환 스크립트
- `fix_professor_table.py` - 교수 목록 표 변환 스크립트
- 기타 변환 스크립트 및 가이드 문서들

## 문제 해결

### 문제: "Repository not found"
- GitHub 저장소가 생성되었는지 확인: https://github.com/snuconnectome/snuconnectome
- SSH 키가 등록되어 있는지 확인

### 문제: "Permission denied"
- SSH 키 확인: `ssh -T git@github.com`
- 또는 HTTPS 사용: `git remote set-url origin https://github.com/snuconnectome/snuconnectome.git`

### 문제: 충돌 발생
```bash
git stash
git pull origin main
git stash pop
```

