# 데이터 타입들

str1 = "아야와 몽모리"
v_bool = True
str2 = "냐냐냐 냐냐냐 냐냐냐"
v_int = 7

v_dict = {
    "name": "배",
    "age": 38
}
v_tuple = 3, 4, 5
v_set = {1, 2, 3}
list = [9, 8, 12]

print(type(str1))
print(type(v_bool))
print(type(v_int))
print(type(v_dict))
print(type(v_tuple))
print(type(v_set))
print(type(list))


# 연산을 해보자

int1 = 123
int2 = 45
bigint1 = 3937858483949892893738748723
bigint2 = 982379689289927839078947982347875

f1 = 3.14
f2 = 1.46579

print(bigint1 + bigint2)
print(int2 + f1) # 타입이 달라도 연산이 된다 -> 자동으로 캐스팅(형변환)이 이루어짐
print(type(int2 + f1))

# 나눗셈의 몫만 출력
print(int1 // int2)
# 나눗셈의 나머지만 출력
print(int1 % int2)

# 제곱 연산 == 익스포낸셜
print(2 ** 3)


# 형변환을 해보자

a = 21.223
b = 5

result = a + b
print(result, type(result))

result2 = int(result)
print(result2, type(result2))
print(float(result2), type(result2))

# 문자 형태인 숫자를 캐스팅 할 수도 있다
print(int('3'), type('3'))

m, n = divmod(100, 8)
print(m, n)

import math
print(math.ceil(5.6))