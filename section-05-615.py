# 조건문

if False:
    print('yes')
else:
    print('nope')


# 관계연산자 >, >=, <, <=, ==, !=

# 참 - 내용이 있는 자료형
# 거짓 - "", '', [], {}, (), 0

# 연산 순서
# 산술 > 관계(크다, 같다) > 논리 연산 순으로 적용한다

# 반복문 while, for
val1 = 1
while val1 < 11:
    print("현재 값은 {} 입니다.".format(val1))
    val1 += 1

print()

for v in range(0,10):
    print(v)
    v += 1

# 1부터 100까지 합계

sum1 = 0
count = 1
while count <= 100:
    sum1 += count
    count += 1

print(sum1)

print(sum(range(1, 101)))


# 시퀀스 자료형 반속 - 리스트, 튜플, 셋, 딕셔너리

names = ['몽모리', '아가', '백호', '천수'] # 리스트

for name in names:
    print(name)

words = '아가와-몽모리' # 스트링
for s in words:
    print(s)

dicts = {
    '아가': '본인',
    '몽모리': '배우자'
}

for k,v in dicts.items():
    print(k,v)


# 홀수만 리스트에 넣기

hol = [x for x in range(1, 101) if x % 2 != 0]
print(hol)