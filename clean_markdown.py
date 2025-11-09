#!/usr/bin/env python3
"""
마크다운 문법을 제거하고 깔끔한 텍스트로 변환
"""

import re
import sys

def clean_markdown(content):
    """마크다운 문법을 제거하고 깔끔한 텍스트로 변환"""
    lines = content.split('\n')
    result = []
    
    for line in lines:
        original_line = line
        
        # 코드 블록 제거
        if line.strip().startswith('```'):
            continue
            
        # 헤더 처리 (# 제거, 텍스트만 유지)
        if line.strip().startswith('#'):
            level = len(line) - len(line.lstrip('#'))
            text = line.lstrip('#').strip()
            # 헤더는 그대로 유지 (제목으로 인식)
            result.append(text)
            continue
        
        # 볼드 제거 (**text** -> text)
        line = re.sub(r'\*\*([^*]+)\*\*', r'\1', line)
        
        # 인라인 코드 제거 (`code` -> code)
        line = re.sub(r'`([^`]+)`', r'\1', line)
        
        # 링크 제거 [text](url) -> text
        line = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', line)
        
        # 수평선 제거 (---)
        if line.strip() == '---':
            result.append('')  # 빈 줄로 대체
            continue
        
        # 체크박스 제거 (- [ ] -> -)
        line = re.sub(r'-\s*\[[ x]\]\s*', '- ', line)
        
        result.append(line)
    
    return '\n'.join(result)

if __name__ == '__main__':
    input_file = '워크샵_제출_자료.md'
    output_file = '워크샵_제출_자료_clean.txt'
    
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        cleaned = clean_markdown(content)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(cleaned)
        
        print(f"✓ 정리 완료: {output_file}")
        
    except Exception as e:
        print(f"✗ 오류: {e}")
        sys.exit(1)

