# 6/15

str1 = "아야와 몽모리"
str2 = "우리는 천생연분이지요"
str3 = ''

# 길이 구하기
print(len(str1 + str2), len(str3))


# 이스케이프

escape_str1 = "그 사람은 \"나는 잘 모르는데\" 라고 이야기 했지"
print(escape_str1)
escape_str2 = "탭을\t주자"
print(escape_str2)

# raw string
raw_str1 = r'd:\아가와몽모리\결혼식 식순.doc'
print(raw_str1)

# 멀티라인

mul = \
'''동해물과

백두산'''

print(mul)

# 문자열 연산
str_o1 = '*'
str_o2 = '아가와'
str_o3 = '몽모리'
print((str_o2 + ' ' + str_o3) * 3)

print('아가' in str_o2)
print('아가' not in str_o3)

# 문자열 형변환

print(str(77) + 'a')


# 문자열 함수 테스트

aa = 'Los Angeles Dodgers'
bb = 'the redsox'

print(aa.islower(), bb.islower())
print(aa.endswith('s'))
print(bb.capitalize())
print(aa.replace('Dodgers', 'Angels'))
print(list(reversed(bb)))


# 문자열 슬라이싱

cc = "아야와 몽모리"
dd = "the cowhill"

print(cc[0:2])
print(cc[0:3])
print(cc[0:])

print(aa[::2])