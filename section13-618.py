# 파이썬 게임 제작

import random
import datetime

words = [] #리스트를 만들어놓고 여기에 단어 파일을 할당한다

n = 1 #게임 시도 횟수 초기화
right_count = 0 # 정답 개수 초기화
wrong_count = 0


# 파일 불러온다
with open('./resource/word.txt', 'r') as f:
    for word in f:
        words.append(word.strip())

# print(words)

input("엔터를 누르면 게임을 시작합니다") # 엔터 눌러야 다음 라인으로 넘어감

start = datetime.datetime.now() # 시작시간 기록

while n <= 5:
    random.shuffle(words)
    question = random.choice(words)
    print()
    print('문제 {}번: '.format(n))
    print(question)

    answer = input("문제에서 제시한 단어를 그대로 입력해주세요 --> ")
    n += 1

    if str(answer).strip() == str(question).strip():
        right_count += 1
        print("정답입니다")
    else:
        wrong_count += 1
        print("멍충아")

end = datetime.datetime.now() # 종료시간 기록
time_spending = end - start
print('최종 결과: 정답 {}개, 오답 {}개'.format(right_count, wrong_count))
print('소요시간: {}, 시작시간 {}, 종료시간: {}'.format(time_spending, start, end))

# 실행 조건
if __name__ == '__main__':
    pass
