#!/usr/bin/env python3
"""
마크다운을 정리하고 표를 CSV 형식으로 변환하여 LibreOffice가 표로 인식하도록 함
"""

import re
import csv
import sys

def process_table_to_csv(lines, start_idx):
    """표를 CSV 형식으로 변환"""
    table_data = []
    i = start_idx
    
    # 헤더 라인
    if i < len(lines) and '|' in lines[i]:
        header = [cell.strip() for cell in lines[i].split('|') if cell.strip()]
        table_data.append(header)
        i += 1
        
        # 구분선 건너뛰기
        if i < len(lines) and '|--' in lines[i]:
            i += 1
        
        # 데이터 행들
        while i < len(lines) and '|' in lines[i] and '|--' not in lines[i]:
            row = lines[i].strip()
            cells = []
            # <br> 태그를 줄바꿈으로 변환
            row = row.replace('<br>', ' / ')
            row = row.replace('<br/>', ' / ')
            # ** 제거
            row = re.sub(r'\*\*([^*]+)\*\*', r'\1', row)
            # 셀 분리
            for cell in row.split('|'):
                cell = cell.strip()
                if cell:
                    cells.append(cell)
            if cells:
                table_data.append(cells)
            i += 1
    
    return table_data, i

def clean_markdown_with_table(content):
    """마크다운을 정리하고 표를 CSV로 변환"""
    lines = content.split('\n')
    result = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # 코드 블록 제거
        if line.strip().startswith('```'):
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                i += 1
            if i < len(lines):
                i += 1
            continue
        
        # 표 처리
        if '| 시간 |' in line or (i > 0 and '|' in lines[i-1] and '|' in line and '시간' in line):
            table_data, new_i = process_table_to_csv(lines, i)
            if table_data:
                result.append('')
                result.append('일정표')
                result.append('')
                # CSV 형식으로 출력 (쉼표로 구분)
                for row in table_data:
                    # CSV 형식: 셀 내용에 쉼표가 있으면 따옴표로 감싸기
                    csv_row = []
                    for cell in row:
                        if ',' in cell or '"' in cell:
                            cell = '"' + cell.replace('"', '""') + '"'
                        csv_row.append(cell)
                    result.append(','.join(csv_row))
                result.append('')
            i = new_i
            continue
        
        # 헤더 처리
        if line.strip().startswith('#'):
            text = line.lstrip('#').strip()
            result.append(text)
            i += 1
            continue
        
        # 볼드 제거
        line = re.sub(r'\*\*([^*]+)\*\*', r'\1', line)
        
        # 인라인 코드 제거
        line = re.sub(r'`([^`]+)`', r'\1', line)
        
        # 링크 제거
        line = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', line)
        
        # 수평선 제거
        if line.strip() == '---':
            result.append('')
            i += 1
            continue
        
        # 체크박스 제거
        line = re.sub(r'-\s*\[[ x]\]\s*', '- ', line)
        
        # <br> 태그 처리
        line = line.replace('<br>', ' / ')
        line = line.replace('<br/>', ' / ')
        
        result.append(line)
        i += 1
    
    return '\n'.join(result)

if __name__ == '__main__':
    input_file = '워크샵_제출_자료.md'
    output_file = '워크샵_제출_자료_clean.txt'
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        cleaned = clean_markdown_with_table(content)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(cleaned)
        
        print(f"✓ 정리 완료: {output_file}")
        print("표가 CSV 형식으로 변환되었습니다.")
        
    except Exception as e:
        print(f"✗ 오류: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

