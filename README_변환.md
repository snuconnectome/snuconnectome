# Word 변환 가이드

## 문제
LibreOffice로 변환하면 마크다운 문법(**bold**, # 헤더 등)이 그대로 남아있습니다.

## 해결 방법

### 1단계: pandoc 설치

터미널에서 다음 명령을 실행하세요:

```bash
sudo apt-get update
sudo apt-get install pandoc
```

### 2단계: 변환 실행

제공된 스크립트를 실행하세요:

```bash
./convert_md_to_docx.sh
```

또는 직접 pandoc 명령 사용:

```bash
pandoc 워크샵_제출_자료.md -o 워크샵_제출_자료.docx --from markdown+smart --to docx --standalone
```

## 변환 후 확인

Word 파일을 열어서 다음을 확인하세요:

- ✅ **볼드 텍스트**가 제대로 표시되는가?
- ✅ **헤더**가 제목 스타일로 적용되었는가?
- ✅ **표**가 제대로 표시되는가?
- ✅ **목록**이 제대로 표시되는가?
- ✅ **일본어 문자**가 제대로 표시되는가?

## 대안 방법

pandoc 설치가 어려운 경우:

1. **Word에서 직접 열기**
   - Word > 파일 > 열기 > 워크샵_제출_자료.md 선택
   - Word가 자동으로 변환합니다

2. **온라인 변환 도구**
   - https://pandoc.org/try/
   - https://cloudconvert.com/md-to-docx

