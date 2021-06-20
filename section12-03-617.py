# 데이터베이스 테이블 수정, 삭제

import sqlite3

conn = sqlite3.connect('c:/Users/ntgat/workspace/nklcb/resource/database.db')
cursor = conn.cursor()

## 데이서 수정 1
cursor.execute("UPDATE users SET username = ? WHERE id = ?", ('냥냥이', 5))

## 데이서 수정 2 딕셔너리
cursor.execute("UPDATE users SET username = :name WHERE id = :id", {'name': '진또배기', 'id': 4})

## 데이서 수정 3 문자열
cursor.execute("UPDATE users SET username = '%s' WHERE id = '%s'" % ('종종냐', 2))



# 데이터 삭제

cursor.execute('DELETE FROM users WHERE id = ?', (5,))
conn.commit()