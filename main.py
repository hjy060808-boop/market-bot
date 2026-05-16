import schedule
import time
from openai import OpenAI
from telegram import Bot
from datetime import datetime
import os

client = OpenAI(
    api_key=os.environ["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"]
)

bot = Bot(
    token=os.environ["send_message():
"]
)

CHAT_ID = os.environ["7730167846"]

def generate_market_news():

    prompt = """
    오늘 미국 증시와 거시경제 뉴스를 한국어로 핵심만 정리해줘.

    반드시 포함:
    
    1. 나스닥 흐름
    2. S&P500 흐름
    3. 미국 국채금리(10년물) 관련 이슈
    4. 유가(WTI/브렌트유) 관련 이슈
    5. 금리에 영향을 줄 수 있는 경제 뉴스
    6. 연준(FED) 관련 발언
    7. 반도체주 관련 뉴스
    8. AI/반도체 섹터 분위기
    9. NVIDIA, AMD, Broadcom, TSMC 관련 핵심 이슈
    10. 시장 리스크 요인
    11. 안전 투자 관점에서의 한줄 의견

    형식:
    - 짧고 핵심만
    - 불필요한 설명 금지
    - 보기 쉽게 정리
    """

    response = client.chat.completions.create(
        model="gpt-5.5",
        messages=[
            {
                "role": "system",
                "content": "You are a professional macro and semiconductor market analyst."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

def send_message() :

    news = generate_market_news()

    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    message = f"""
📈 데일리 미국증시 브리핑
🕒 {now}

{news}
"""

    bot.send_message(
        chat_id=CHAT_ID,
        text=message
    )

    print("Sent!")

send_message()

schedule.every().day.at("07:00").do(send_message)

while True:
    schedule.run_pending()
    time.sleep(30)
