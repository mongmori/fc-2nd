## sqlite 테이블 조회

import sqlite3

# db 파일 조회
conn = sqlite3.connect('c:/Users/ntgat/workspace/nklcb/resource/database.db')
print(type(conn))

# 커서 바인딩
cursor = conn.cursor()

# 데이터 조회(전체)
cursor.execute("SELECT * FROM users")

# 커서 위치 변경을 확인해보자
# row 1개 선택
# print(cursor.fetchone())

# # 특정 row 지정
# print(cursor.fetchmany(size=3))

# # 모든 row 지정
# print(cursor.fetchall())

# 데이터베이스 순회
# rows = cursor.fetchall()
# for row in rows:
#     print('retrive: ', row)

# 데이터베이스 순회 다른방법

# for row in cursor.execute("SELECT * FROM users ORDER BY id desc"):
#     print('retrive: ', row)


# where절 retrive1 튜플
param1 = (3, )
cursor.execute("SELECT * FROM users WHERE id=?", param1)
print(cursor.fetchone())

# where절 retrive2 문자열, 정수
param2 = 1
cursor.execute("SELECT * FROM users WHERE id='%s'" % param2)
print(cursor.fetchone())

# where절 retrive3 딕셔너리
cursor.execute("SELECT * FROM users WHERE id=:id", {'id': 5})
print(cursor.fetchone())

# where절 retrive4 합집합 in 절
param4 = (3, 5)
cursor.execute("SELECT * FROM users WHERE id IN(?,?)", param4)
print(cursor.fetchall())


# dump 출력
with conn:
    with open('c:/Users/ntgat/workspace/nklcb/resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('dump complete')
