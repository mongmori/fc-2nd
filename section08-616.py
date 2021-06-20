# 모듈과 패키지
# 상대경로 -> .. 부모 디렉토리, . 현재 디렉토리

# 클래스 불러오기
from pkg.fibonacci import Fibonacci as fb

fb.fib(300)
print(fb.fib2(10000))