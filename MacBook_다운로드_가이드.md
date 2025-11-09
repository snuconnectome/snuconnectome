# MacBook Pro에서 PDF 다운로드 가이드

## 방법 1: GitHub에서 직접 다운로드 (가장 간단)

1. 웹 브라우저에서 다음 URL 접속:
   https://github.com/snuconnectome/snuconnectome

2. `워크샵_제출_자료.pdf` 파일 찾기

3. 파일 클릭하여 상세 페이지로 이동

4. 우측 상단의 "Download" 버튼 클릭

5. 다운로드된 파일을 Desktop으로 이동

---

## 방법 2: Git Clone 사용

MacBook Pro의 터미널에서:

```bash
cd ~/Desktop
git clone https://github.com/snuconnectome/snuconnectome.git
cd snuconnectome
# PDF 파일이 여기에 있습니다
```

---

## 방법 3: SCP를 사용한 직접 전송 (SSH 접근 가능한 경우)

MacBook Pro의 터미널에서:

```bash
# Linux 서버의 IP 주소와 사용자명을 알려주시면 명령어를 제공하겠습니다
scp user@server-ip:/home/juke/git/Japan/워크샵_제출_자료.pdf ~/Desktop/
```

---

## 방법 4: GitHub Raw URL로 직접 다운로드

터미널에서:

```bash
cd ~/Desktop
curl -L -o "워크샵_제출_자료.pdf" \
  "https://github.com/snuconnectome/snuconnectome/raw/main/워크샵_제출_자료.pdf"
```

또는 브라우저에서 다음 URL로 직접 접속:
https://github.com/snuconnectome/snuconnectome/raw/main/워크샵_제출_자료.pdf

---

## 추천 방법

**가장 간단한 방법**: GitHub 웹사이트에서 직접 다운로드
- https://github.com/snuconnectome/snuconnectome
- `워크샵_제출_자료.pdf` 파일 클릭 → Download

