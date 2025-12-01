#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from weasyprint import HTML, CSS

# HTML 파일을 PDF로 변환
html_file = '/home/juke/git/Japan/워크샵_제출_자료.html'
pdf_file = '/home/juke/git/Japan/워크샵_제출_자료.pdf'

# CSS 스타일 정의
css = CSS(string='''
    @page {
        size: A4;
        margin: 20mm;
    }
    body {
        font-family: "Noto Sans KR", "Malgun Gothic", sans-serif;
        font-size: 11pt;
        line-height: 1.6;
    }
    h1, h2 {
        page-break-after: avoid;
    }
    table {
        page-break-inside: avoid;
    }
''')

HTML(filename=html_file).write_pdf(pdf_file, stylesheets=[css])
print(f'PDF 생성 완료: {pdf_file}')
