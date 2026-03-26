#!/usr/bin/env python3
"""
한국 음악 산업 주간 뉴스레터 자동 생성기 (Claude API)
매주 금요일 오후 4시 실행
"""

import os
from datetime import datetime, timedelta
import anthropic
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 환경 변수 설정
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD")
RECIPIENT_EMAIL = "bluejeans.signup@gmail.com"

def get_date_range():
    """지난 7일 날짜 범위 반환"""
    today = datetime.now()
    week_ago = today - timedelta(days=7)
    return week_ago.strftime("%Y-%m-%d"), today.strftime("%Y-%m-%d")

def generate_newsletter():
    """Claude API로 뉴스레터 생성"""
    
    start_date, end_date = get_date_range()
    
    # Claude API 클라이언트 초기화
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    
    prompt = f"""당신은 한국 음악 산업 뉴스레터 전문 에디터입니다.

**목표:** {start_date}부터 {end_date}까지 지난 7일간의 한국 음악 저작권, 음악 비즈니스 관련 뉴스를 수집하고 정리해주세요.

**필수 검색 키워드:**
- 음저협 OR 함저협 최신 뉴스
- AI 음악 저작권 분쟁
- OTT PP 음악 저작권료
- 큐시트 BROMIS
- 문체부 저작권 정책
- 음악 저작권 소송

**콘텐츠 선정 우선순위:**

**1순위 (반드시 포함):**
✓ 음저협/함저협 정책 발표, 조직 개편, 업무 지적, 개선명령
✓ 금액/수치가 명시된 저작권료 이슈 (예: "5,200곡", "₩150억")
✓ 정부/문체부 저작권법 개정, 안내서 발표, 감사 결과

**2순위 (중요도 높음):**
✓ AI 음악 저작권 (생성형 AI 학습, 분쟁, 검증 시스템, 옵트아웃)
✓ OTT/PP 저작권료 (BROMIS, 큐시트, 정산 구조)
✓ 저작권 분쟁/소송 (국내외, 판결, 새로운 분쟁 유형)

**3순위 (포함 고려):**
✓ 시스템/인프라 변화 (블록체인, 통합 징수)
✓ 국제 협력/동향 (CISAC, 해외 판례)
✓ 업계 구조 개편 (협회 통합, 신규 단체)

**절대 제외:**
✗ 음반 판매량/차트 순위
✗ 아이돌 개인 활동/데뷔
✗ 콘서트/공연 일정
✗ 가수 개인 논란
✗ 엔터사 주가/실적 (저작권 무관한 것)

**작업 절차:**
1. 웹 검색으로 최신 뉴스 수집 (반드시 {start_date} 이후만)
2. 우선순위 기준으로 필터링
3. 같은 사건의 중복 기사 제거 (1개만 선택)
4. 최종 3-4개 핵심 뉴스만 선별
5. 아래 포맷으로 작성

**뉴스레터 포맷:**

```
[월]월 [주]주차 뉴스클리핑 전달드립니다.

1. [뉴스 제목]
<URL>

   -
   
   [핵심 내용 1: 사실 중심, 100-150자]
   
   -
   
   [핵심 내용 2: 추가 세부사항, 100-150자]


2. [두 번째 뉴스 제목]
<URL>

   -
   
   [내용]


3. [세 번째 뉴스 제목]

...
```

**중요 규칙:**
- 뉴스 개수: 3-4개 (최대 4개, 5개 금지)
- 각 뉴스: 간결하고 객관적, 사실 중심
- 숫자/금액/수치 반드시 명시
- URL 포함 필수
- 날짜 명시 불필요 (이미 최신 뉴스만 검색)
- 반드시 지난 7일 이내만

지금 바로 시작해주세요."""

    # Claude API 호출
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=16000,
        temperature=0.3,
        tools=[
            {
                "type": "web_search_20250305",
                "name": "web_search"
            }
        ],
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    
    # 응답에서 텍스트 추출
    newsletter_content = ""
    for block in message.content:
        if hasattr(block, 'text'):
            newsletter_content += block.text
    
    return newsletter_content

def send_email(newsletter_content):
    """Gmail로 뉴스레터 발송"""
    
    # 이메일 설정
    sender_email = "bluejeans.signup@gmail.com"  # 본인 Gmail
    sender_password = GMAIL_APP_PASSWORD
    recipient_email = RECIPIENT_EMAIL
    
    # 날짜 정보
    today = datetime.now()
    month = today.month
    week_of_month = (today.day - 1) // 7 + 1
    
    # 이메일 생성
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f"🎵 한국 음악 산업 뉴스레터 | {month}월 {week_of_month}주차"
    msg['From'] = sender_email
    msg['To'] = recipient_email
    
    # HTML 버전
    html_content = f"""
    <html>
    <body style="font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px;">
        <pre style="white-space: pre-wrap; font-family: 'Malgun Gothic', sans-serif; line-height: 1.6;">
{newsletter_content}
        </pre>
        <hr style="margin-top: 40px; border: none; border-top: 1px solid #ccc;">
        <p style="color: #666; font-size: 12px;">
        본 뉴스레터는 자동으로 생성되어 발송되었습니다.<br>
        생성 시간: {today.strftime('%Y-%m-%d %H:%M')}<br>
        Powered by Claude AI
        </p>
    </body>
    </html>
    """
    
    # 텍스트 버전 (HTML 미지원 클라이언트용)
    text_content = newsletter_content
    
    part1 = MIMEText(text_content, 'plain', 'utf-8')
    part2 = MIMEText(html_content, 'html', 'utf-8')
    
    msg.attach(part1)
    msg.attach(part2)
    
    # SMTP 발송
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print(f"✅ 뉴스레터 발송 완료: {recipient_email}")
        return True
    except Exception as e:
        print(f"❌ 이메일 발송 실패: {str(e)}")
        return False

def main():
    """메인 실행 함수"""
    print(f"🚀 뉴스레터 생성 시작: {datetime.now()}")
    
    try:
        # 1. 뉴스레터 생성
        print("📰 뉴스 수집 및 정리 중...")
        newsletter = generate_newsletter()
        
        if not newsletter:
            print("❌ 뉴스레터 생성 실패")
            return
        
        print(f"✅ 뉴스레터 생성 완료 ({len(newsletter)} 글자)")
        
        # 2. 이메일 발송
        print("📧 이메일 발송 중...")
        success = send_email(newsletter)
        
        if success:
            print("🎉 모든 작업 완료!")
        else:
            print("⚠️ 발송 실패")
            
    except Exception as e:
        print(f"❌ 오류 발생: {str(e)}")
        raise

if __name__ == "__main__":
    main()
