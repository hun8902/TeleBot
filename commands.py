# commands.py
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from helpers import save_user_id, dev_run, send_notice_to_all_users

def send_welcome(message, bot):
    chat_id = message.chat.id
    save_user_id(chat_id)  # 사용자 ID를 저장

    # 사용자에게 표시할 버튼 설정
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("가져오기"), KeyboardButton("종료"), KeyboardButton("전체"))
    bot.reply_to(message, "원하는 작업을 선택하세요.", reply_markup=markup)

def handle_message(message, bot):
    if message.text == "가져오기":
        dev_run(bot)
        bot.send_message(message.chat.id, "바로 가져오기가 실행됩니다.")
    elif message.text == "종료":
        bot.send_message(message.chat.id, "이카운트 자동 업로드 봇이 종료됩니다.")
        sys.exit(0)
    elif message.text == "전체":
        send_notice_to_all_users(bot, "공지사항 내용입니다.")
    else:
        bot.reply_to(message, "올바른 명령을 선택해주세요.")
