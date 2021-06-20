# 딕셔너리, json과 유사함

# 딕셔너리 특징 - 순서 없음, 중복(key) 안됨, 수정삭제 가능

a = {'name': '몽모리', 'age': 38, 'city': '의정부'}
b = {'arr': [1,2,3,4]}

print(a['name'])
print(a.get('name'))
print(a.get('몽모리'))

# 딕셔너리 추가
a['availability'] = True
print(a)

# 함수사용
print(a.keys())
print(a.values())
print(a.items())

# 형변환하여 슬라이싱
# 형 변환 이후에 인덱스에 접근 가능
alist = list(a.keys())
print(alist[:])


# 집합(set) - 순서 없고 중복 불가, 추가제거 가능
# 셋은 주로 변환을 해서 사용한다
aa = set()
bb = set([1,2,3,4])
cc = set([1,4,5,6,6])

print(bb, cc)

print()
print()
print()

s1 = set([1,2,3,4,5,6,7])
s2 = set([6,7,8,9,])
print(s1.intersection(s2)) # 교집합
print(s1 & s2) # 교집합

print(s1 | s2) #합집합
print(s1.union(s2))

print(s1 - s2)
print(s1.difference(s2)) #차집합

s3 = set([11,23,45,67])
s3.add(100)
print(s3)
s3.remove(11)
print(s3)