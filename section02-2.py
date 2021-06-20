import sys

# 파이썬 기본 인코딩 -> utf-8

print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 변수 선언

firstVar = '몽모리요'

# 조건문

if firstVar == '아야요':
    print(True)
else:
    print(False)

# 반복문

for i in range(1,10):
    for j in range(1,10):
        print('%d * %d = ' % (i,j), i*j)

# 함수 선언

def firstFunc():
    print(firstVar)

firstFunc()

# 클래스 선언

class Mongmori:
    pass

# 객체 생성

mong = Mongmori()

print(id(mong))
print(dir(mong))