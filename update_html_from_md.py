#!/usr/bin/env python3
"""
마크다운 파일을 읽어서 HTML 파일을 업데이트
"""

import re
import sys

def markdown_to_html(md_content):
    """마크다운을 HTML로 변환"""
    lines = md_content.split('\n')
    html_lines = []
    in_table = False
    table_rows = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # 표 처리
        if '| 시간 |' in line or (i > 0 and '|' in lines[i-1] and '|' in line and '시간' in line):
            if not in_table:
                in_table = True
                table_rows = []
            
            # 헤더 라인
            if '| 시간 |' in line:
                cells = [cell.strip() for cell in line.split('|') if cell.strip()]
                table_rows.append('<tr>' + ''.join([f'<th>{cell}</th>' for cell in cells]) + '</tr>')
                i += 1
                # 구분선 건너뛰기
                if i < len(lines) and '|--' in lines[i]:
                    i += 1
                continue
            
            # 데이터 행
            if '|' in line and '|--' not in line:
                # <br> 태그 처리
                line_processed = line.replace('<br>', ' / ')
                cells = [cell.strip() for cell in line_processed.split('|') if cell.strip()]
                # ** 제거
                cells = [re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', cell) for cell in cells]
                table_rows.append('<tr>' + ''.join([f'<td>{cell}</td>' for cell in cells]) + '</tr>')
                i += 1
                continue
        else:
            if in_table:
                html_lines.append('<table border="1" style="border-collapse: collapse; width: 100%; margin: 20px 0;">')
                html_lines.extend(table_rows)
                html_lines.append('</table>')
                in_table = False
                table_rows = []
        
        # 헤더 처리
        if line.startswith('# '):
            html_lines.append(f'<h1>{line[2:].strip()}</h1>')
        elif line.startswith('## '):
            html_lines.append(f'<h2>{line[3:].strip()}</h2>')
        elif line.startswith('### '):
            html_lines.append(f'<h3>{line[4:].strip()}</h3>')
        elif line.startswith('#### '):
            html_lines.append(f'<h4>{line[5:].strip()}</h4>')
        # 볼드 처리
        elif '**' in line:
            line = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', line)
            if line.strip():
                html_lines.append(f'<p>{line}</p>')
        # 수평선
        elif line.strip() == '---':
            html_lines.append('<hr>')
        # 빈 줄
        elif not line.strip():
            if html_lines and html_lines[-1] != '':
                html_lines.append('')
        # 일반 텍스트
        elif line.strip():
            # 이미 <p> 태그가 있으면 그대로
            if line.strip().startswith('<'):
                html_lines.append(line)
            else:
                html_lines.append(f'<p>{line}</p>')
        
        i += 1
    
    # 마지막 표 처리
    if in_table:
        html_lines.append('<table border="1" style="border-collapse: collapse; width: 100%; margin: 20px 0;">')
        html_lines.extend(table_rows)
        html_lines.append('</table>')
    
    return '\n'.join(html_lines)

def main():
    # 마크다운 파일 읽기
    with open('워크샵_제출_자료.md', 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # HTML 헤더와 본문 분리
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

