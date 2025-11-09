#!/usr/bin/env python3
"""
PDF 생성을 위한 최종 정리 스크립트
- 모든 마크다운 문법 제거
- 표를 LibreOffice Writer가 인식할 수 있는 형식으로 변환
"""

import re
import sys

def clean_text(text):
    """모든 마크다운 문법 제거"""
    # 볼드 제거
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    # 인라인 코드 제거
    text = re.sub(r'`([^`]+)`', r'\1', text)
    # 링크 제거
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    # <br> 태그를 줄바꿈으로
    text = text.replace('<br>', '\n').replace('<br/>', '\n')
    return text

def process_table(lines, start_idx):
    """표를 LibreOffice Writer 표 형식으로 변환"""
    table_data = []
    i = start_idx
    
    # 헤더
    if i < len(lines) and '|' in lines[i]:
        header = [cell.strip() for cell in lines[i].split('|') if cell.strip()]
        table_data.append(header)
        i += 1
        
        # 구분선 건너뛰기
        if i < len(lines) and '|--' in lines[i]:
            i += 1
        
        # 데이터 행
        while i < len(lines) and '|' in lines[i] and '|--' not in lines[i]:
            row = lines[i].strip()
            # <br> 처리
            row = row.replace('<br>', ' / ').replace('<br/>', ' / ')
            # ** 제거
            row = clean_text(row)
            cells = [cell.strip() for cell in row.split('|') if cell.strip()]
            if cells:
                table_data.append(cells)
            i += 1
    
    return table_data, i

def process_professor_table():
    """교수 목록을 표 형식으로 반환"""
    professors = [
        {'name': '박주용', 'major': '인지심리학', 'field': '인지심리학', 'office': '16동 M405호 / 02-880-9050', 'email': 'jooypark@snu.ac.kr'},
        {'name': '한소원', 'major': '인지심리학', 'field': '인지심리학', 'office': '16동 M511호 / 02-880-6439', 'email': 'swhahn@snu.ac.kr'},
        {'name': '이수현', 'major': '인지신경과학', 'field': '인지신경과학', 'office': '16동 M408호 / 02-880-9108', 'email': 'suehlee@snu.ac.kr'},
        {'name': '차지욱', 'major': '신경과학', 'field': '신경과학', 'office': '16동 M512호 / 02-880-8618', 'email': 'connectome@snu.ac.kr'},
        {'name': '최진영', 'major': '임상신경과학', 'field': '신경과학', 'office': '16동 M407호 / 02-880-6432', 'email': 'jychey@snu.ac.kr'},
        {'name': '오성주', 'major': 'Perception', 'field': '지각심리학', 'office': '16동 M411호 / 02-880-6430', 'email': 'songjoo@snu.ac.kr'},
        {'name': '김향숙', 'major': '임상심리학', 'field': '임상심리학', 'office': '16동 M506호 / 02-880-8764', 'email': 'hyangkim@snu.ac.kr'},
        {'name': '안우영', 'major': '임상심리학', 'field': '임상심리학', 'office': '16동 M505호 / 02-880-2538', 'email': 'wahn55@snu.ac.kr'},
        {'name': '이훈진', 'major': '임상상담심리학', 'field': '임상심리학', 'office': '16동 M507호 / 02-880-5997', 'email': 'hjlee83@snu.ac.kr'},
        {'name': '최인철', 'major': '사회심리학', 'field': '사회심리학', 'office': '16동 M406호, 220동 642호 / 02-880-6437, 02-880-6399', 'email': 'ichoi@snu.ac.kr'},
        {'name': '김가원', 'major': '조직심리학', 'field': '조직심리학', 'office': '16동 M510호 / 02-880-8273', 'email': 'kawon@snu.ac.kr'},
        {'name': '이해연', 'major': '발달심리학', 'field': '발달심리학', 'office': '16동 M509호 / 02-880-5792', 'email': 'haeyeon.lee@snu.ac.kr'},
        {'name': '고성룡', 'major': '언어심리학', 'field': '언어심리학', 'office': '16동 M505호 / 02-880-9107', 'email': 'koh@snu.ac.kr'},
        {'name': '석혜원', 'major': '계량심리학', 'field': '계량심리학', 'office': '16동 423호 / 02-880-6076', 'email': 'hwsuk@snu.ac.kr'},
    ]
    return professors

def convert_markdown_to_clean_text(content):
    """마크다운을 완전히 정리된 텍스트로 변환"""
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
            table_data, new_i = process_table(lines, i)
            if table_data:
                result.append('')
                result.append('일정표')
                result.append('')
                # LibreOffice Writer가 인식할 수 있도록 탭으로 구분
                for row in table_data:
                    result.append('\t'.join(row))
                result.append('')
            i = new_i
            continue
        
        # 교수 목록 처리
        if '#### 6.2.1' in line or ('6.2.1' in line and '서울대학교' in line):
            result.append(line.lstrip('#').strip())
            i += 1
            if i < len(lines) and not lines[i].strip():
                result.append('')
                i += 1
            
            # 교수 표 삽입
            professors = process_professor_table()
            result.append('')
            result.append('참여 교수 명단')
            result.append('')
            result.append('이름\t전공\t연구분야\t연구실\t이메일')
            for prof in professors:
                row = f"{prof['name']}\t{prof['major']}\t{prof['field']}\t{prof['office']}\t{prof['email']}"
                result.append(row)
            result.append('')
            
            # 기존 교수 목록 건너뛰기
            while i < len(lines):
                if '#### 6.2.2' in lines[i] or '#### 6.2.3' in lines[i]:
                    break
                i += 1
            continue
        
        # 헤더 처리
        if line.strip().startswith('#'):
            text = line.lstrip('#').strip()
            result.append(text)
            i += 1
            continue
        
        # 일반 라인 처리
        line = clean_text(line)
        
        # 수평선 제거
        if line.strip() == '---':
            result.append('')
            i += 1
            continue
        
        # 체크박스 제거
        line = re.sub(r'-\s*\[[ x]\]\s*', '- ', line)
        
        result.append(line)
        i += 1
    
    return '\n'.join(result)

if __name__ == '__main__':
    input_file = '워크샵_제출_자료.md'
    output_file = '워크샵_제출_자료_final.txt'
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        cleaned = convert_markdown_to_clean_text(content)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(cleaned)
        
        print(f"✓ 최종 정리 완료: {output_file}")
        print("모든 마크다운 문법이 제거되었고, 표가 탭 구분 형식으로 변환되었습니다.")
        
    except Exception as e:
        print(f"✗ 오류: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

