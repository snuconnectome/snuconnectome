# GitHub 저장소 생성 및 Push 가이드

## 현재 상태
- ✅ Git repository 초기화 완료
- ✅ 파일 commit 완료
- ✅ Remote 설정 완료 (git@github.com:snuconnectome/snuconnectome.git)
- ⚠️  GitHub에 repository가 아직 생성되지 않음

## 방법 1: GitHub 웹사이트에서 생성 (권장)

### 1단계: Repository 생성
1. https://github.com/new 접속
2. 다음 정보 입력:
   - **Owner**: snuconnectome
   - **Repository name**: snuconnectome
   - **Description**: Active Inference and AI 학술 심리학과 학사 협의회 제출 자료
   - **Visibility**: Public 또는 Private 선택
   - ⚠️ **중요**: "Add a README file", "Add .gitignore", "Choose a license"는 모두 **체크하지 않음**
3. "Create repository" 클릭

### 2단계: Push
Repository 생성 후 다음 명령 실행:

```bash
cd /home/juke/git/Japan
git push -u origin main
```

---

## 방법 2: GitHub CLI 사용

### 1단계: GitHub CLI 설치 (없는 경우)
```bash
# Ubuntu/Debian
sudo apt-get install gh

# 또는 공식 설치 스크립트
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt-get update
sudo apt-get install gh
```

### 2단계: GitHub CLI 로그인
```bash
gh auth login
```

### 3단계: Repository 생성 및 Push
```bash
cd /home/juke/git/Japan
./setup_github_repo.sh
```

또는 직접 명령:
```bash
gh repo create snuconnectome/snuconnectome \
    --public \
    --description "Active Inference and AI 학술 심리학과 학사 협의회 제출 자료" \
    --source=. \
    --remote=origin \
    --push
```

---

## 방법 3: 제공된 스크립트 사용

```bash
cd /home/juke/git/Japan
./setup_github_repo.sh
```

---

## Push 후 확인

Push가 성공하면 다음 URL에서 확인할 수 있습니다:
- https://github.com/snuconnectome/snuconnectome

---

## 문제 해결

### 문제: "Repository not found"
- GitHub에서 repository를 먼저 생성해야 합니다
- 위의 "방법 1"을 따라 repository를 생성하세요

### 문제: "Permission denied"
- SSH 키가 GitHub에 등록되어 있는지 확인
- 또는 Personal Access Token 사용:
  ```bash
  git remote set-url origin https://[TOKEN]@github.com/snuconnectome/snuconnectome.git
  ```

### 문제: "Authentication failed"
- GitHub CLI로 재인증:
  ```bash
  gh auth login
  ```

---

## 현재 Remote 설정

```bash
git remote -v
```

출력:
```
origin  git@github.com:snuconnectome/snuconnectome.git (fetch)
origin  git@github.com:snuconnectome/snuconnectome.git (push)
```

