# 예외처리

# try: 에러 발생 가능성이 있는 코드블록
# except: 에러 발생시 처리하게 되는 부분으로 에러명을 출력하는 용도로 사용
# else: 에러기 없을때 실행하는 부분
# finally: 항상 실행하는 부분


# name = ['아가', '몽모리', '콤콤']

# try:
#     z = 'dd'
#     x = name.index(z)
#     print('{}가 {} 번째에 있습니다.'.format(z, x+1))
# except ValueError:
#     print('ValueError입니다')
# else:
#     print('잘 실행되는군요')
# finally:
#     print('ok')


# 자체적으로 에러 발생시킴 - raise

try:
    a = 'ㄴㄴ'
    if a == '아가':
        print('ok')
    else:
        raise ValueError
except ValueError:
    print('문제')