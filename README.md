
# 이카운트 자동 업로드 봇 (TeleBot)

이 프로젝트는 Python으로 작성된 텔레그램 봇입니다. 사용자는 봇을 통해 특정 명령을 입력하고, XAMPP 서버 제어 및 자동화 작업을 수행할 수 있습니다. 사용자는 데이터베이스에 연결된 텔레그램 사용자들의 ID를 저장하고, 공지사항을 보낼 수 있습니다. 이 봇은 특정 시간에 작업을 자동으로 수행할 수 있는 스케줄링 기능도 포함하고 있습니다.

## 주요 기능
- 텔레그램 봇을 통한 XAMPP 서버 제어 (Apache, MySQL, FileZilla 등)
- 데이터베이스(MySQL)를 사용하여 사용자 ID 관리
- 공지사항 및 메시지를 텔레그램 사용자에게 전송
- 특정 시간에 자동 작업을 수행하는 스케줄링 기능
- 주기적으로 서버 상태를 체크하고, 주말에 특정 작업을 건너뛰는 기능

## 프로젝트 구조

```bash
.
├── bot.py                  # 메인 봇 실행 스크립트
├── commands.py             # 텔레그램 명령어 핸들링
├── helpers.py              # 데이터베이스 연결, 사용자 ID 저장 및 메시지 전송 기능
├── config.py               # 봇의 설정 (API 키 및 데이터베이스 정보)
├── requirements.txt        # 필요한 파이썬 패키지 목록
└── README.md               # 프로젝트 설명 파일
```

## 파일 설명

- **bot.py**: 봇의 진입점으로, 텔레그램 봇을 실행하고 메시지를 처리합니다. 
- **commands.py**: 텔레그램 봇에서 사용자의 명령(예: `/start`, "가져오기" 등)을 처리하는 로직이 포함된 파일입니다.
- **helpers.py**: 데이터베이스 연결, 사용자 ID 저장, 메시지 전송 등과 같은 기능을 담당하는 유틸리티 함수들이 포함된 파일입니다.
- **config.py**: 텔레그램 봇 토큰, 데이터베이스 접속 정보 등 설정을 정의하는 파일입니다. 이 파일은 민감한 정보가 포함되어 있으므로 `.gitignore`에 추가해야 합니다.
- **requirements.txt**: 프로젝트가 필요로 하는 Python 라이브러리 목록을 포함합니다.

## 사전 요구 사항

이 프로젝트를 실행하기 전에 다음 소프트웨어가 설치되어 있어야 합니다:
- Python 3.7 이상
- MySQL 서버
- XAMPP 설치 (Apache, MySQL, FileZilla)

### 필수 Python 패키지

다음은 프로젝트에 필요한 주요 Python 패키지입니다:
- `mysql-connector-python`: MySQL 데이터베이스와 Python 간의 연결을 처리하는 패키지
- `pyTelegramBotAPI`: 텔레그램 봇 API와 상호작용하기 위한 패키지
- `schedule`: 작업 스케줄링을 위한 패키지
- `psutil`: 프로세스 제어를 위한 패키지
- `selenium`: 웹 브라우저 자동화를 위한 패키지 (필요한 경우)

필요한 패키지들은 `requirements.txt` 파일에 정의되어 있습니다.

## 설치 방법

1. **프로젝트 클론**
    ```bash
    git clone https://github.com/your-repo/telebot.git
    cd telebot
    ```

2. **가상 환경 설정 및 패키지 설치**
    ```bash
    python -m venv venv
    source venv/bin/activate   # (Windows: venv\Scripts\activate)
    pip install -r requirements.txt
    ```

3. **MySQL 데이터베이스 설정**
    - MySQL에 `telegram_chat` 테이블을 생성해야 합니다. 아래 명령어를 사용하여 테이블을 생성합니다:
    ```sql
    CREATE DATABASE your_database_name;

    USE your_database_name;

    CREATE TABLE telegram_chat (
        id INT AUTO_INCREMENT PRIMARY KEY,
        chat_id BIGINT NOT NULL UNIQUE
    );
    ```

4. **config.py 파일 설정**
    `config.py` 파일을 생성하고, 텔레그램 봇 토큰과 데이터베이스 정보를 입력합니다.

    ```python
    # config.py
    telegram_token = 'your_telegram_bot_token'
    telegram_chat_id = 'your_chat_id'
    
    db_host = 'localhost'
    db_id = 'root'
    db_password = 'your_mysql_password'
    db_name = 'your_database_name'
    ```

5. **XAMPP 설치**
   XAMPP를 설치하고, `xampp-control.exe`가 `C:\xampp\xampp-control.exe` 경로에 있는지 확인하세요.

## 실행 방법

1. **봇 실행**
    ```bash
    python bot.py
    ```

2. **텔레그램 명령어**
    텔레그램에서 봇과 대화하여 다음과 같은 명령을 사용할 수 있습니다:
    - `/start`: 봇을 시작하고 사용자에게 인사말을 전송
    - "가져오기": 현재 시간을 모든 사용자에게 전송
    - "종료": 봇을 종료
    - "공지사항": 특정 공지사항을 모든 사용자에게 전송

3. **스케줄링 작업**
    - 스케줄링 작업은 월요일~금요일에 하루 5번 자동으로 수행되며, 주말에는 작업이 건너뛰어집니다.
    - 스케줄링 작업은 `schedule` 라이브러리를 사용하여 설정됩니다.

## 테스트

- 봇이 실행 중인 상태에서 텔레그램에서 봇에 `/start`를 입력하여 봇이 정상적으로 작동하는지 확인합니다.
- MySQL 데이터베이스에서 `telegram_chat` 테이블에 사용자 `chat_id`가 저장되는지 확인합니다.

## 문제 해결

- **ImportError**: 특정 모듈을 찾을 수 없다는 오류가 발생하면, `requirements.txt`에 정의된 패키지가 제대로 설치되지 않았는지 확인하세요.
    ```bash
    pip install -r requirements.txt
    ```

- **데이터베이스 연결 오류**: 데이터베이스 설정이 올바른지, MySQL 서버가 실행 중인지 확인하세요.

## 기여

이 프로젝트에 기여하고 싶다면, 이 저장소를 포크한 후 PR(Pull Request)을 보내주세요.

## 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다.
