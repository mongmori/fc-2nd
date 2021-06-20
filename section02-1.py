# 3개도 출력됨
print("""몽모리""")

# separator 옵션을 준다
print('아', '야', '요', sep='')
print('2000', '12', '6', sep='-')

# end 옵션 사용
# 원래 프린트 함수가 끝나면 개행문자가 붙으나, 엔드옵션에 값을 비움으로써 줄바꿈을 없앴다
print('welccome', end='\n')

# format 사용
print('{}와 {}'.format('아가', '몽모리'))

# 명시적으로 format 위치를 정한다
print('{a} 그리고 {b}'.format(a='사랑', b='행복'))

# %s = 문자, %d = 정수, %f = 실수
print('%s는 아야를 %d 만큼 좋아하지요' % ('몽모리', 2000))

print("test1: %5d, test2: %4.2f" % (1234, 5544.444))
print("test1: {a: 5d}, test2: {b: 4.2f}".format(a=1234, b=2233.4444))

