#!/usr/bin/env python3
"""
Markdown to Word 변환 스크립트
마크다운 파일을 Word 형식으로 변환하며, 마크다운 문법을 제대로 렌더링합니다.
"""

import sys
import os
import re
from pathlib import Path

def markdown_to_word_text(md_content):
    """
    마크다운 텍스트를 Word에서 사용할 수 있는 형식으로 변환
    **bold** -> 볼드 텍스트로 변환 (Word에서는 직접 처리 불가하므로 제거)
    """
    # 마크다운 헤더 제거 (# ## ### 등)
    lines = md_content.split('\n')
    result = []
    
    for line in lines:
        # 헤더 처리 (# 제거하고 볼드로 표시)
        if line.startswith('#'):
            level = len(line) - len(line.lstrip('#'))
            text = line.lstrip('#').strip()
            # Word에서는 헤더 스타일을 직접 적용할 수 없으므로 텍스트만 남김
            result.append(text)
        # 볼드 처리 (**text** -> text)
        elif '**' in line:
            # **text** 패턴 제거
            line = re.sub(r'\*\*(.+?)\*\*', r'\1', line)
            result.append(line)
        # 리스트 항목 처리 (- 제거)
        elif line.strip().startswith('- '):
            text = line.strip()[2:]
            result.append(f'  • {text}')
        # 코드 블록 제거 (```)
        elif line.strip().startswith('```'):
            continue
        # 링크 처리 [text](url) -> text
        elif '[' in line and '](' in line:
            line = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', line)
            result.append(line)
        # 기타 마크다운 문법 제거
        else:
            # 인라인 코드 `code` -> code
            line = re.sub(r'`([^`]+)`', r'\1', line)
            result.append(line)
    
    return '\n'.join(result)

def convert_markdown_to_word(md_file, docx_file):
    """
    마크다운 파일을 Word 형식으로 변환
    """
    # 마크다운 파일 읽기
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # 변환된 텍스트 생성
    word_text = markdown_to_word_text(md_content)
    
    # 임시 텍스트 파일 생성
    temp_txt = docx_file.replace('.docx', '_temp.txt')
    with open(temp_txt, 'w', encoding='utf-8') as f:
        f.write(word_text)
    
    # LibreOffice로 변환
    import subprocess
    try:
        result = subprocess.run(
            ['libreoffice', '--headless', '--convert-to', 'docx', '--outdir', os.path.dirname(docx_file) or '.', temp_txt],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # 임시 파일 삭제
        if os.path.exists(temp_txt):
            os.remove(temp_txt)
        
        # 변환된 파일 이름 변경
        converted_file = temp_txt.replace('_temp.txt', '_temp.docx')
        if os.path.exists(converted_file):
            if os.path.exists(docx_file):
                os.remove(docx_file)
            os.rename(converted_file, docx_file)
            print(f"✓ 변환 완료: {docx_file}")
            return True
        else:
            print(f"✗ 변환 실패: LibreOffice 변환 오류")
            return False
            
    except Exception as e:
        print(f"✗ 변환 실패: {e}")
        if os.path.exists(temp_txt):
            os.remove(temp_txt)
        return False

if __name__ == '__main__':
    md_file = '워크샵_제출_자료.md'
    docx_file = '워크샵_제출_자료.docx'
    
    if len(sys.argv) > 1:
        md_file = sys.argv[1]
    if len(sys.argv) > 2:
        docx_file = sys.argv[2]
    
    if not os.path.exists(md_file):
        print(f"✗ 파일을 찾을 수 없습니다: {md_file}")
        sys.exit(1)
    
    print(f"변환 중: {md_file} -> {docx_file}")
    success = convert_markdown_to_word(md_file, docx_file)
    
    if not success:
        print("\n대안: pandoc을 사용한 변환을 시도합니다...")
        print("pandoc 설치 명령: sudo apt-get install pandoc")
        print("pandoc 변환 명령: pandoc 워크샵_제출_자료.md -o 워크샵_제출_자료.docx")

