#!/usr/bin/env python3
"""
마크다운을 정리하고 표를 CSV 형식으로 변환
참여 교수 목록도 표 형식으로 변환
"""

import re
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

def process_professor_list(lines, start_idx):
    """교수 목록을 표 형식으로 변환"""
    professors = []
    i = start_idx
    current_field = ""
    current_professor = {}
    
    while i < len(lines):
        line = lines[i].strip()
        
        # 섹션 종료 조건
        if line.startswith('####') or line.startswith('##') or line.startswith('---') or \
           (line.startswith('*') and '참고' in line) or line.startswith('##'):
            break
        
        # 분야 헤더 (예: **인지심리학 분야**)
        if line.startswith('**') and '분야' in line:
            current_field = line.replace('**', '').replace('분야', '').strip()
            i += 1
            continue
        
        # 교수 정보 라인 (예: - **박주용 교수** (인지심리학))
        if line.startswith('- **') and '교수' in line:
            # 교수 이름과 전공 추출
            match = re.match(r'-\s*\*\*([^*]+)\*\*\s*\(([^)]+)\)', line)
            if match:
                name = match.group(1).strip()
                major = match.group(2).strip()
                current_professor = {
                    'name': name,
                    'major': major,
                    'field': current_field,
                    'office': '',
                    'email': ''
                }
            i += 1
            continue
        
        # 연구실 정보
        if current_professor and '연구실:' in line:
            office = line.replace('연구실:', '').replace('-', '').strip()
            current_professor['office'] = office
            i += 1
            continue
        
        # 이메일 정보
        if current_professor and '이메일:' in line:
            email = line.replace('이메일:', '').strip()
            current_professor['email'] = email
            professors.append(current_professor)
            current_professor = {}
            i += 1
            continue
        
        # 빈 줄이나 다른 내용은 건너뛰기
        if not line or line.startswith('-') and '교수' not in line:
            i += 1
            continue
        
        i += 1
    
    return professors, i

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
        
        # 일정표 처리
        if '| 시간 |' in line or (i > 0 and '|' in lines[i-1] and '|' in line and '시간' in line):
            table_data, new_i = process_table_to_csv(lines, i)
            if table_data:
                result.append('')
                result.append('일정표')
                result.append('')
                for row in table_data:
                    csv_row = []
                    for cell in row:
                        if ',' in cell or '"' in cell:
                            cell = '"' + cell.replace('"', '""') + '"'
                        csv_row.append(cell)
                    result.append(','.join(csv_row))
                result.append('')
            i = new_i
            continue
        
        # 참석자 명단 섹션에서 교수 목록 처리
        if '#### 6.2.1' in line or ('참석 예정자' in line and i + 1 < len(lines) and '####' in lines[i+1]):
            result.append(line.lstrip('#').strip() if line.strip().startswith('#') else line)
            i += 1
            # 다음 줄 확인
            if i < len(lines) and '####' in lines[i]:
                result.append(lines[i].lstrip('#').strip())
                i += 1
            # 교수 목록 처리
            if i < len(lines) and ('인지심리학' in lines[i] or '교수' in lines[i]):
                professors, new_i = process_professor_list(lines, i)
                if professors:
                    result.append('')
                    result.append('참여 교수 명단')
                    result.append('')
                    # 표 헤더
                    result.append('이름,전공,연구분야,연구실,이메일')
                    # 교수 데이터
                    for prof in professors:
                        name = prof.get('name', '')
                        major = prof.get('major', '')
                        field = prof.get('field', '')
                        office = prof.get('office', '')
                        email = prof.get('email', '')
                        # CSV 형식으로 변환
                        row = f'"{name}","{major}","{field}","{office}","{email}"'
                        result.append(row)
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
        print("참여 교수 명단이 표 형식으로 변환되었습니다.")
        
    except Exception as e:
        print(f"✗ 오류: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

