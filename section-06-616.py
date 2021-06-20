# 함수 정의와 람다함수

#정의
def hello(str):
    print('Hello {}'.format(str))

# 함수 호출
hello('아야요')


# 값을 리턴하도록 함수 작성

def hello_return(arr):
    return_val = "Hello " + str(arr)
    return return_val

hello1 = hello_return(1234)
print(hello1)


# 다중 리턴 - 함수가 다수의 값을 계산하고 다수의 변수로 리턴해줄 수 있다

def multi(x):
    rt1 = x * 100
    rt2 = x * 200
    rt3 = x * 300
    return rt1, rt2, rt3

val1, val2, val3 = multi(100)
print(val1, val2, val3)


# *args, *kwargs를 알아보자

def args_func(*args): # 파라미터의 개수가 가변하며 별표가 한개이면 튜플로 값을 반환
    print(args)

args_func('아아요', '몽모리요')

def kwargs_func(**kwargs): # 별표가 두개이면 딕셔너리로 값을 반환
    print(kwargs)

kwargs_func(아가='오아야',몽모리='배몽모리',결혼=2017)

# 혼합 펑션

def comp_func(arr1, arr2, *args, **kwargs): # 필수 파라미터 2개, 나머지는 옵셔널
    print(arr1, arr2, args, kwargs)

comp_func('아가와', '몽모리')
comp_func('아가와', '몽모리', 233, '가나다')
comp_func('아가와', '몽모리', 233, '가나다', 아가='예쁜아가님', 몽모칭구="냐냐냐")


# 중첩함수(클로저)

def surf_func(num):
    def inner_func(num):
        print(num)
    print('processing...')
    inner_func(num ** 2)

surf_func(100)


# 람다식 -> 메모리 절약, 가독성 향상, 코드가 간결하다
# 함수는 객체가 생성되지만 람다는 즉시 실행한다 -> 메모리 절약

def exfunc(num : int) -> int:
    return num * 10

val11 = exfunc(10)
print(val11)

lambda_mul_10 = lambda num: num * 10
print(lambda_mul_10(10))