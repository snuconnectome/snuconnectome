#!/usr/bin/env python3
"""
교수 목록을 표 형식으로 변환하는 스크립트
"""

import re

# 교수 데이터 직접 정의
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

# 파일 읽기
with open('워크샵_제출_자료.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 교수 목록 섹션 찾기 및 교체
lines = content.split('\n')
result = []
i = 0
in_professor_section = False
professor_section_start = -1

while i < len(lines):
    line = lines[i]
    
    # 교수 섹션 시작
    if '#### 6.2.1' in line or ('6.2.1' in line and '서울대학교' in line):
        result.append(line.lstrip('#').strip())
        i += 1
        # 빈 줄
        if i < len(lines) and not lines[i].strip():
            result.append('')
            i += 1
        
        # 교수 표 삽입
        result.append('')
        result.append('참여 교수 명단')
        result.append('')
        result.append('이름,전공,연구분야,연구실,이메일')
        for prof in professors:
            name = prof['name']
            major = prof['major']
            field = prof['field']
            office = prof['office']
            email = prof['email']
            # CSV 형식
            result.append(f'"{name}","{major}","{field}","{office}","{email}"')
        result.append('')
        
        # 기존 교수 목록 건너뛰기
        while i < len(lines):
            if '#### 6.2.2' in lines[i] or '#### 6.2.3' in lines[i]:
                break
            i += 1
        continue
    
    # 일반 라인 처리
    result.append(line)
    i += 1

# 파일 저장
with open('워크샵_제출_자료_clean.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(result))

print("교수 목록이 표 형식으로 변환되었습니다.")

