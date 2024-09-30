# bot.py
import os
import schedule
import time
import sys
from telebot import TeleBot
from commands import send_welcome, handle_message
from helpers import greet_all_users, is_weekend, dev_run, cleanup

from config import telegram_token

TOKEN = telegram_token  # Telegram 봇의 토큰
bot = TeleBot(TOKEN)

# 메인 실행 부분
if __name__ == "__main__":
    script_path = os.path.abspath(__file__)
    os.chdir(os.path.dirname(script_path))

    print("이카운트 자동 업로드 봇이 시작되었습니다.")
    greet_all_users(bot)  # 모든 사용자에게 인사말 전송

    try:
        bot.add_message_handler({"function": send_welcome, "filters": {"commands": ['start']}})
        bot.add_message_handler({"function": handle_message, "filters": {"func": lambda message: True}})
        bot.polling(none_stop=True)

        # 스케줄 설정
        schedule.every().day.at("08:00").do(lambda: dev_run(bot) if not is_weekend() else None)
        schedule.every().day.at("11:00").do(lambda: dev_run(bot) if not is_weekend() else None)
        schedule.every().day.at("13:00").do(lambda: dev_run(bot) if not is_weekend() else None)
        schedule.every().day.at("15:00").do(lambda: dev_run(bot) if not is_weekend() else None)
        schedule.every().day.at("17:00").do(lambda: dev_run(bot) if not is_weekend() else None)

        while True:
            schedule.run_pending()
            time.sleep(1)

    except Exception as e:
        print(f"봇 실행 중 오류 발생: {e}")
        cleanup(bot)
        sys.exit(1)
