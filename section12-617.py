# 파이썬 데이터베이스 연동 (SQLite)

import sqlite3
import datetime

# 날짜 생성
now = datetime.datetime.now()
print(now)

# 데이트타임 포맷 결정
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)

# DB 생성 & 오토 커밋
conn = sqlite3.connect('C:/Users/ntgat/workspace/nklcb/resource/database.db', isolation_level=None)

# 파일을 읽어올 커서를 가져온다
cursor = conn.cursor()
print(type(cursor))


# 테이블 생성
# sqlite는 text, numeric, integer, real, blob 타입이 있다
cursor.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, \
    username text, email text, phone text, website text, regdate text)')

# 데이터 삽입
# cursor.execute('INSERT INTO users VALUES(1, "몽모칭구", "mongmori@protonmail.com", \
#     "010-3333-4444", "https://mongmori.com", ?)', (nowDatetime, ))


# 데이터 삽입 두번째 방법
# cursor.execute("INSERT INTO users(id, username, email, phone, website, regdate) \
#     VALUES(?,?,?,?,?,?)", (2, '아야요', 'come@naver.com', '010-2345-6789', 'https://www.naver.com',nowDatetime))


# may 삽입 - 대용량 데이터를 한번에 삽입 (튜플, 리스트 모두 가능)

userList = (
    (3, '콤콤', 'comcom@daum.net', '010-3300-4567', 'www.kakao.com', nowDatetime),
    (4, '냐냐냐', 'nana@daum.net', '010-3300-4567', 'www.kakao.com', nowDatetime),
    (5, '진또배기', 'jonddo@daum.net', '010-3300-4567', 'www.kakao.com', nowDatetime)
)

# cursor.executemany("INSERT INTO users(id, username, email, phone, website, regdate) \
#     VALUES(?,?,?,?,?,?)", userList)


# 데이터 삭제
# print('db deleted count: ', conn.execute("DELETE FROM users").rowcount)


# 커밋 - isolation_level=None 일 경우 자동으로 커밋함
# 그렇지 않다면 conn.commit() 으로 명시적 실행함
# 명시적으로 커밋한 경우 conn.rollback() 으로 되돌릴 수 있음
# 작업을 마친 경우 커넥션을 끊어서 메모리를 반환한다. conn.close()
