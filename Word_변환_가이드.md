# Markdown to Word 변환 가이드

## 문제점
LibreOffice로 직접 변환하면 마크다운 문법(**bold**, # 헤더 등)이 그대로 남아있습니다.

## 해결 방법

### 방법 1: pandoc 사용 (권장)

pandoc은 마크다운을 Word 형식으로 잘 변환하는 도구입니다.

#### 설치
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install pandoc

# macOS
brew install pandoc
```

#### 변환 명령
```bash
# 기본 변환
pandoc 워크샵_제출_자료.md -o 워크샵_제출_자료.docx

# 또는 제공된 스크립트 사용
./convert_to_word_pandoc.sh
```

#### 고급 옵션
```bash
# 참조 문서 스타일 사용 (있는 경우)
pandoc 워크샵_제출_자료.md -o 워크샵_제출_자료.docx \
    --reference-doc=reference.docx

# 표 스타일 지정
pandoc 워크샵_제출_자료.md -o 워크샵_제출_자료.docx \
    --standalone \
    --toc
```

---

### 방법 2: Python 스크립트 사용

제공된 Python 스크립트를 사용할 수 있습니다.

```bash
python3 convert_to_word.py
```

---

### 방법 3: 온라인 변환 도구

1. **Pandoc Try** (https://pandoc.org/try/)
   - 마크다운 파일을 업로드하고 Word 형식으로 다운로드

2. **CloudConvert** (https://cloudconvert.com/md-to-docx)
   - 마크다운을 Word로 변환

3. **Zamzar** (https://www.zamzar.com/convert/md-to-docx/)
   - 파일 변환 서비스

---

### 방법 4: 수동 변환 (Word에서 직접)

1. Word를 엽니다
2. "파일" > "열기" > 마크다운 파일 선택
3. Word가 자동으로 변환합니다
4. 필요시 서식 조정

---

## 변환 후 확인 사항

변환 후 다음을 확인하세요:

- [ ] **볼드 텍스트**가 제대로 표시되는가?
- [ ] **헤더**가 제목 스타일로 적용되었는가?
- [ ] **표**가 제대로 표시되는가?
- [ ] **목록**이 제대로 표시되는가?
- [ ] **링크**가 제대로 작동하는가?
- [ ] **일본어 문자**가 제대로 표시되는가?

---

## 문제 해결

### 문제: pandoc이 설치되지 않음
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install pandoc

# 또는 snap 사용
sudo snap install pandoc
```

### 문제: 변환 후 서식이 이상함
- Word에서 "홈" > "스타일"을 사용하여 수동으로 조정
- 또는 참조 문서(reference.docx)를 만들어 사용

### 문제: 표가 깨짐
- Word에서 표를 선택하고 "표 디자인"에서 스타일 적용
- 또는 수동으로 표 서식 조정

---

## 참고

- pandoc 공식 문서: https://pandoc.org/
- pandoc 사용 예제: https://pandoc.org/demos.html

