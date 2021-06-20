# # 파일 읽기 쓰기
# # 읽기

# f = open('./resource/review.txt', 'r')
# content = f.read()
# print(content)

# print(type(f))
# print(dir(f)) # 해당 인스턴스에서 사용할 수 있는 메소드 목록

# content = f.close()

# print(type(f))
# print(dir(f)) # 해당 인스턴스에서

# print('------------------------------------------------')

# with open('./resource/review.txt', 'r') as f:
#     c = f.read()
#     print(iter(c))

# print('------------------------------------------------')

# with open('./resource/review.txt', 'r') as f:
#     for c in f:
#         print(c)
#         print(c.strip()) # f 내에 있는 한 라인을 순회

# print('------------------------------------------------')

# with open('./resource/review.txt', 'r') as f:
#     line = f.readline()
#     while line:
#         print(line, end='!!! ')
#         line = f.readline()

print('------------------------------------------------')

with open('./resource/review.txt', 'r') as f:
    contents = f.readlines() # 라인들을 리스트 형태로 반환
    print(contents)
    for line in contents:
        print(line)

print('------------------------------------------------')

# with open('./resource/score.txt', 'r') as f:
#     score = []
#     for num in f:
#         score.append(int(num))
#     print(len(score), score)
#     summation = sum(score)
#     print(summation)
#     print(summation / len(score))


# ## 파일 쓰기
# with open('./resource/text1.txt', 'w') as f:
#     f.write('아가와 몽모리요\n')

# ## 파일 수정
# with open('./resource/text1.txt', 'a') as f:
#     f.write('야야의 평화를 빌어주는\n')


# from random import randint
# with open('./resource/text2.txt', 'w') as f:
#     for count in range(6):
#         f.write(str(randint(1, 46)))
#         f.write('\n')

# # 리스트를 파일로 저장
# with open('./resource/text3.txt', 'w') as f:
#     list1 = ['아가님\n', '몽모칭구\n', '예쁜아가님이요\n']
#     f.writelines(list1)