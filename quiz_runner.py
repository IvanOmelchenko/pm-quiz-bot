import os
import random
import urllib.request
import urllib.parse
from questions_pool import QUESTIONS

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = urllib.parse.urlencode({"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}).encode()
    urllib.request.urlopen(urllib.request.Request(url, data=data))

def main():
    q = random.choice(QUESTIONS)
    labels = ["A", "B", "C", "D"]
    text = f"<b>PM Quiz</b>\n\n{q['q']}\n\n"
    for i, opt in enumerate(q['options']):
        text += f"{labels[i]}) {opt}\n"
    idx = labels.index(q['answer'])
    text += f"\n<tg-spoiler>Answer: {q['answer']}) {q['options'][idx]}\n{q.get('explanation','')}</tg-spoiler>"
    send_message(text)

if __name__ == "__main__":
    main()
