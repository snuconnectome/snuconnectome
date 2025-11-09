#!/usr/bin/env python3
"""
마크다운 파일을 읽어서 HTML 파일을 생성 (표 포함)
"""

import re

def process_table(lines, start_idx):
    """표를 HTML 테이블로 변환"""
    table_rows = []
    i = start_idx
    
    # 헤더 라인
    if i < len(lines) and '|' in lines[i]:
        header_line = lines[i]
        cells = [cell.strip() for cell in header_line.split('|') if cell.strip()]
        if len(cells) > 1:  # 실제 표인지 확인
            # ** 제거하고 <strong>으로 변환
            cells = [re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', cell) for cell in cells]
            table_rows.append('<tr>' + ''.join([f'<th>{cell}</th>' for cell in cells]) + '</tr>')
            i += 1
            
            # 구분선 건너뛰기
            if i < len(lines) and ('|--' in lines[i] or '|---' in lines[i]):
                i += 1
            
            # 데이터 행들
            while i < len(lines) and '|' in lines[i] and '|--' not in lines[i] and '|---' not in lines[i]:
                row_line = lines[i].strip()
                if not row_line or row_line.startswith('#'):
                    break
                
                # <br> 태그를 <br/>로 변환 (HTML 표준)
                row_line = row_line.replace('<br>', '<br/>')
                cells = [cell.strip() for cell in row_line.split('|') if cell.strip()]
                if len(cells) > 1:  # 실제 데이터 행인지 확인
                    # ** 제거하고 <strong>으로 변환
                    cells = [re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', cell) for cell in cells]
                    table_rows.append('<tr>' + ''.join([f'<td>{cell}</td>' for cell in cells]) + '</tr>')
                i += 1
    
    if table_rows:
        html_table = '<table border="1" style="border-collapse: collapse; width: 100%; margin: 20px 0;">\n'
        html_table += '\n'.join(table_rows)
        html_table += '\n</table>'
        return html_table, i
    return None, start_idx + 1

def process_professor_list_to_table(lines, start_idx):
    """교수 목록을 표 형식으로 변환"""
    professors = []
    i = start_idx
    
    # 교수 목록 섹션 찾기
    while i < len(lines):
        line = lines[i]
        
        # 섹션 끝 확인
        if line.startswith('##') or line.startswith('---'):
            break
        
        # 교수 정보 추출
        if line.strip().startswith('- **') and '교수' in line:
            # 교수 이름과 분야 추출
            match = re.search(r'\*\*([^*]+)\*\*.*?\(([^)]+)\)', line)
            if match:
                name = match.group(1)
                field = match.group(2)
                
                # 다음 줄들에서 연구실과 이메일 추출
                lab = ''
                email = ''
                j = i + 1
                while j < len(lines) and (lines[j].strip().startswith('-') or lines[j].strip().startswith('  -')):
                    if '연구실' in lines[j]:
                        lab_match = re.search(r'연구실[:\s]+([^\n/]+)', lines[j])
                        if lab_match:
                            lab = lab_match.group(1).strip()
                    if '이메일' in lines[j]:
                        email_match = re.search(r'이메일[:\s]+([^\n]+)', lines[j])
                        if email_match:
                            email = email_match.group(1).strip()
                    j += 1
                
                professors.append({
                    'name': name,
                    'field': field,
                    'lab': lab,
                    'email': email
                })
                i = j
                continue
        
        i += 1
    
    if professors:
        html_table = '<table border="1" style="border-collapse: collapse; width: 100%; margin: 20px 0;">\n'
        html_table += '<tr><th>이름</th><th>전공 분야</th><th>연구실</th><th>이메일</th></tr>\n'
        for prof in professors:
            html_table += f'<tr><td><strong>{prof["name"]}</strong></td><td>{prof["field"]}</td><td>{prof["lab"]}</td><td>{prof["email"]}</td></tr>\n'
        html_table += '</table>'
        return html_table, i
    
    return None, start_idx

def markdown_to_html(md_content):
    """마크다운을 HTML로 변환"""
    lines = md_content.split('\n')
    html_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # 표 처리 (일정표)
        if '| 시간 |' in line or (i > 0 and '|' in lines[i-1] and '|' in line and '시간' in line):
            table_html, new_i = process_table(lines, i)
            if table_html:
                html_lines.append(table_html)
                i = new_i
                continue
        
        # 일반 표 처리 (다른 표들)
        if '|' in line and not line.strip().startswith('|') and i > 0:
            # 이전 줄이 표의 일부인지 확인
            if '|' in lines[i-1] and '|--' not in lines[i-1] and '|---' not in lines[i-1]:
                table_html, new_i = process_table(lines, i-1)
                if table_html:
                    # 이미 추가했는지 확인
                    if html_lines and html_lines[-1] != table_html:
                        html_lines.append(table_html)
                    i = new_i
                    continue
        
        # 표 처리 (교수 명단 포함, 모든 표 처리)
        if '|' in line and not line.strip().startswith('|') and i > 0:
            # 이전 줄이 표의 일부인지 확인
            if '|' in lines[i-1] and '|--' not in lines[i-1] and '|---' not in lines[i-1]:
                table_html, new_i = process_table(lines, i-1)
                if table_html:
                    # 이미 추가했는지 확인
                    if html_lines and html_lines[-1] != table_html:
                        html_lines.append(table_html)
                    i = new_i
                    continue
        
        # 표 시작 라인 처리 (헤더 라인)
        if '|' in line and line.strip().startswith('|'):
            table_html, new_i = process_table(lines, i)
            if table_html:
                html_lines.append(table_html)
                i = new_i
                continue
        
        # 헤더 처리
        if line.startswith('# '):
            text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', line[2:].strip())
            html_lines.append(f'<h1>{text}</h1>')
        elif line.startswith('## '):
            text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', line[3:].strip())
            html_lines.append(f'<h2>{text}</h2>')
        elif line.startswith('### '):
            text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', line[4:].strip())
            html_lines.append(f'<h3>{text}</h3>')
        elif line.startswith('#### '):
            text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', line[5:].strip())
            html_lines.append(f'<h4>{text}</h4>')
        # 수평선
        elif line.strip() == '---':
            html_lines.append('<hr>')
        # 빈 줄
        elif not line.strip():
            html_lines.append('')
        # 볼드가 포함된 텍스트
        elif '**' in line:
            text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', line)
            if text.strip() and not text.strip().startswith('-'):
                html_lines.append(f'<p>{text}</p>')
            else:
                html_lines.append(f'<p>{text}</p>')
        # 리스트 항목
        elif line.strip().startswith('- '):
            text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', line[2:].strip())
            html_lines.append(f'<p>- {text}</p>')
        # 일반 텍스트
        elif line.strip():
            text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', line)
            html_lines.append(f'<p>{text}</p>')
        
        i += 1
    
    return '\n'.join(html_lines)

def main():
    # 마크다운 파일 읽기
    with open('워크샵_제출_자료.md', 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # HTML 헤더
    html_header = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>심리학과 학사 협의회 개최 신청서</title>
<style>
body { font-family: "Malgun Gothic", "맑은 고딕", sans-serif; line-height: 1.6; margin: 40px; }
h1 { font-size: 24px; border-bottom: 2px solid #333; padding-bottom: 10px; }
h2 { font-size: 20px; margin-top: 30px; border-bottom: 1px solid #ccc; padding-bottom: 5px; }
h3 { font-size: 18px; margin-top: 20px; }
h4 { font-size: 16px; margin-top: 15px; }
table { border-collapse: collapse; width: 100%; margin: 20px 0; border: 1px solid #000; }
th, td { border: 1px solid #000; padding: 8px; text-align: left; }
th { background-color: #f0f0f0; font-weight: bold; }
p { margin: 10px 0; }
ul, ol { margin: 10px 0; padding-left: 30px; }
</style>
</head>
<body>"""
    
    html_footer = """</body>
</html>"""
    
    # 마크다운을 HTML로 변환
    html_body = markdown_to_html(md_content)
    
    # 전체 HTML 조합
    full_html = html_header + '\n' + html_body + '\n' + html_footer
    
    # HTML 파일 저장
    with open('워크샵_제출_자료_final.html', 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print("✓ HTML 파일 업데이트 완료: 워크샵_제출_자료_final.html")

if __name__ == '__main__':
    main()

