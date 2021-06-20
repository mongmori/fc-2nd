# 리스트, 튜플 등 자료형
# 리스트는 순서가 있고, 중복을 허용하고, 수정이 가능하고, 삭제도 된다

# 리스트 선언
a = []
b = list()
c = [1,2,3,4]
d = [5, 6, ['아가', '몽모리', 456]]

# 리스트 인덱싱
print(d[2][1]) #3번째 내에 있는 2번째
print(c[0] + d[1])

# 리스트 슬라이싱
print(d[1:3])


# 리스트 연산
print(c + d)
print(c * 2)
print(str(c) + '이열')

# 수정, 삭제
c[0] = 888
print(c)

c[1:2] = [66, 77, 88]
print(c)

del c[0]
print(c)
print()
print()
print()
print()

# 리스트 관련 함수
y = [1, 5, 3, 4, 8]
y.append(9)
print(y)
y.sort()
print(y)
y.reverse()
print(y)

y.insert(2,10)
print(y)

y.remove(10)
print(y)

print(y.pop()) # 리스트의 맨 마지막 원소를 꺼내버린다
print(y)

z = [123, 456]
y.extend(z) # 익스텐드는 append와는 다르게 대상 리스트에 원소로 값을 넣는다
# 어펜드는 리스트 자체를 붙여넣음
print(y)



# 튜플의 특성 - 순서가 있고 중복을 허용한다. 그러나 수정 삭제가 불가능.
# 일반적으로 key값들을 튜플로 만든다

aa = ()
bb = (1, )
cc = (1,2,3,4)
dd = (12, 13, 13, (1,2,3))

print(dd.index(13))
print(dd.count(13))