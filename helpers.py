import schedule
import mysql.connector
from mysql.connector import Error
from datetime import datetime
from config import db_host, db_id, db_password, db_name

# 데이터베이스 연결
def create_connection():
    try:
        connection = mysql.connector.connect(
            host=db_host,
            user=db_id,
            password=db_password,
            database=db_name
        )
        print("데이터베이스에 연결되었습니다.")
        return connection
    except Error as e:
        print(f"데이터베이스 연결 오류: {e}")
        return None

# 사용자 ID 저장
def save_user_id(chat_id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "INSERT IGNORE INTO telegram_chat (chat_id) VALUES (%s)"
        cursor.execute(query, (chat_id,))
        connection.commit()
        cursor.close()
        connection.close()

# 모든 사용자에게 인사말 보내기
def greet_all_users(bot):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT chat_id FROM telegram_chat")
        chat_ids = cursor.fetchall()
        for chat_id in chat_ids:
            bot.send_message(chat_id[0], "안녕하세요! 이카운트 자동 업로드 봇이 시작되었습니다.")
        cursor.close()
        connection.close()

# 현재 시간 전송
def dev_run(bot):
    global browser, conn, cursor

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"현재 시간은 {current_time}입니다."
    
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT chat_id FROM telegram_chat")
        chat_ids = cursor.fetchall()
        for chat_id in chat_ids:
            bot.send_message(chat_id[0], message)
        cursor.close()
        connection.close()

# 주말 확인
def is_weekend():
    return datetime.now().weekday() >= 5

# 공지사항을 모든 사용자에게 전송
def send_notice_to_all_users(bot, notice_message):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT chat_id FROM telegram_chat")
        chat_ids = cursor.fetchall()
        for chat_id in chat_ids:
            bot.send_message(chat_id[0], notice_message)
        cursor.close()
        connection.close()

# 봇 종료 처리
def cleanup(bot):
    print("봇 종료 중...")
    schedule.clear()
