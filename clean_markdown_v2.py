#!/usr/bin/env python3
"""
마크다운 문법을 제거하고 깔끔한 텍스트로 변환
표 형식은 유지하되 LibreOffice가 인식할 수 있도록 처리
"""

import re
import sys

def process_table(lines, start_idx):
    """표를 처리하여 LibreOffice가 인식할 수 있는 형식으로 변환"""
    table_lines = []
    i = start_idx
    
    # 표 헤더 찾기
    if i < len(lines) and '|' in lines[i]:
        # 헤더 라인
        header = lines[i].strip()
        table_lines.append(header)
        i += 1
        
        # 구분선 제거 (|---|---|)
        if i < len(lines) and '|' in lines[i] and '---' in lines[i]:
            i += 1
        
        # 데이터 라인들
        while i < len(lines) and '|' in lines[i]:
            line = lines[i].strip()
            if line and not line.startswith('|--'):
                table_lines.append(line)
            i += 1
    
    return table_lines, i

def clean_markdown(content):
    """마크다운 문법을 제거하고 깔끔한 텍스트로 변환"""
    lines = content.split('\n')
    result = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        original_line = line
        
        # 코드 블록 제거
        if line.strip().startswith('```'):
            i += 1
            # 코드 블록 끝까지 건너뛰기
            while i < len(lines) and not lines[i].strip().startswith('```'):
                i += 1
            if i < len(lines):
                i += 1
            continue
            
        # 표 처리
        if '|' in line and i + 1 < len(lines) and '|' in lines[i + 1]:
            table_lines, new_i = process_table(lines, i)
            if table_lines:
                result.append('')  # 표 전에 빈 줄
                result.extend(table_lines)
                result.append('')  # 표 후에 빈 줄
            i = new_i
            continue
        
        # 헤더 처리 (# 제거, 텍스트만 유지)
        if line.strip().startswith('#'):
            level = len(line) - len(line.lstrip('#'))
            text = line.lstrip('#').strip()
            # 헤더는 그대로 유지 (제목으로 인식)
            result.append(text)
            i += 1
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
            i += 1
            continue
        
        # 체크박스 제거 (- [ ] -> -)
        line = re.sub(r'-\s*\[[ x]\]\s*', '- ', line)
        
        # <br> 태그를 줄바꿈으로 변환
        line = line.replace('<br>', '\n')
        line = line.replace('<br/>', '\n')
        
        result.append(line)
        i += 1
    
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
        import traceback
        traceback.print_exc()
        sys.exit(1)

