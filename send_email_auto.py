#!/usr/bin/env python3
"""
이메일 자동 전송 스크립트 (PDF 첨부)
"""

import sys
from pathlib import Path

# Emailer 경로 추가
emailer_path = Path.home() / "git" / "Emailer"
sys.path.insert(0, str(emailer_path))

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64
import pickle
import os
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Gmail API scopes (read + send)
SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.send'
]

def authenticate_gmail():
    """Gmail API 인증 (send 권한 포함)"""
    creds = None
    token_file = emailer_path / "token.pickle"
    credentials_file = emailer_path / "credentials.json"
    
    # 기존 토큰 로드
    if token_file.exists():
        with open(token_file, 'rb') as token:
            creds = pickle.load(token)
    
    # 토큰이 없거나 만료된 경우
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not credentials_file.exists():
                raise FileNotFoundError(
                    f"{credentials_file} not found. "
                    "Download from Google Cloud Console"
                )
            flow = InstalledAppFlow.from_client_secrets_file(
                str(credentials_file), SCOPES
            )
            creds = flow.run_local_server(port=0)
        
        # 토큰 저장
        with open(token_file, 'wb') as token:
            pickle.dump(creds, token)
    
    return build('gmail', 'v1', credentials=creds)

def create_message_with_attachment(sender, to, subject, body_text, file_path):
    """이메일 메시지 생성 (첨부파일 포함)"""
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    
    # 본문 추가
    msg_body = MIMEText(body_text, 'plain', 'utf-8')
    message.attach(msg_body)
    
    # 첨부파일 추가
    if file_path and os.path.exists(file_path):
        with open(file_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
        
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename= {os.path.basename(file_path)}'
        )
        message.attach(part)
    
    # Base64 인코딩
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
    return {'raw': raw_message}

def send_email(service, sender, to, subject, body_text, file_path=None):
    """이메일 전송"""
    try:
        message = create_message_with_attachment(sender, to, subject, body_text, file_path)
        send_message = service.users().messages().send(
            userId='me',
            body=message
        ).execute()
        
        print(f"✅ 이메일 전송 완료!")
        print(f"   Message ID: {send_message['id']}")
        return send_message
    except HttpError as error:
        print(f"❌ 이메일 전송 실패: {error}")
        return None

def main():
    """메인 함수"""
    print("=" * 60)
    print("이메일 전송 스크립트")
    print("=" * 60)
    
    # Gmail 인증
    print("\n1. Gmail API 인증 중...")
    try:
        service = authenticate_gmail()
        print("✅ 인증 완료")
    except Exception as e:
        print(f"❌ 인증 실패: {e}")
        return
    
    # 발신자 이메일 확인
    profile = service.users().getProfile(userId='me').execute()
    sender_email = profile['emailAddress']
    print(f"\n발신자: {sender_email}")
    
    # 수신자
    to_email = "cha.jiook@gmail.com"
    
    # 제목
    subject = "심리학과 학사 협의회 개최 신청서"
    
    # 본문
    body_text = """안녕하세요.

심리과학연구소·심리학과 공동 주최 심리학과 학사 협의회 개최 신청서를 첨부하여 보내드립니다.

본 학사 협의회는 인공지능, 심리학, 뇌과학의 융합을 통한 서울대학교 심리학과 교육과 연구의 혁신을 모색하고, 관련 분야 전문가들과의 심도 있는 논의를 통해 학과의 미래 발전 방향을 수립하는 것을 목적으로 합니다.

일본 하코네에서 개최되며, RIKEN Isomura 박사의 "Active Inference and AI" 초청 강의를 포함한 다양한 프로그램으로 구성됩니다.

자세한 내용은 첨부된 신청서를 참고해 주시기 바랍니다.

감사합니다.

차지욱
서울대학교 심리학과"""
    
    # 첨부파일 경로
    pdf_path = Path.home() / "git" / "Japan" / "워크샵_제출_자료.pdf"
    if not pdf_path.exists():
        print(f"\n❌ PDF 파일을 찾을 수 없습니다: {pdf_path}")
        return
    
    print(f"\n📎 첨부파일: {pdf_path.name}")
    
    # 전송 정보 확인
    print("\n" + "=" * 60)
    print("전송 정보 확인:")
    print(f"  수신자: {to_email}")
    print(f"  제목: {subject}")
    print(f"  첨부파일: {pdf_path.name}")
    print("=" * 60)
    
    # 전송
    print("\n2. 이메일 전송 중...")
    result = send_email(service, sender_email, to_email, subject, body_text, str(pdf_path))
    
    if result:
        print("\n✅ 이메일이 성공적으로 전송되었습니다!")
    else:
        print("\n❌ 이메일 전송에 실패했습니다.")

if __name__ == "__main__":
    main()

