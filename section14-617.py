# 파이썬 레퍼런스

# 객체참조시 중요한 특징들
#python object referrence

print(dir()) # 현재 파이썬 파일 자체의 메소드 출력

# id vs __eq__ 증명 ( 이퀄 == )
x = {'name': '아가', 'age': 34, 'city': '의정부'}
y = x

print(id(x), id(y)) # 같은 객체임
print( x == y )
print( x is y ) # 모두 같다

x['class'] = '좋아요'
print(x, y) # x에다가 키밸류를 하나 더 넣었는데 그게 y도 반영된다
## 따라서 할당된 변수를 수정할때 주의해야 함
# 딕셔너리가 많을때는 == 로 비교하기 보다는 is로 비교하는게 좋다


# copy와 deep copy
tl1 = [10,[100, 101], (1,2,3)]
tl2 = tl1
tl3 = list(tl1)

# 비교
print(tl1 == tl2) # 값이 같기때문에 true
print(tl1 is tl2) # id가 같기 때문에 true
print(tl3 == tl1) # 값이 같기때문에 true
print(tl3 is tl1) # id가 다르기 때문에 false
print(tl3 == tl2) # 값이 같기때문에 true
# 결론 - 다른 객체로부터 값을 받아올때는 생성자를 명시적으로 사용해서 값을 받아오는게 좋다

## deep copy를 해보자

class Basket:
    def __init__(self, products=None):
        if products is None:
            self._products = []
        else:
            self._products = list(products)

    def add_product(self, prod_name):
        self._products.append(prod_name)

    def del_product(self, prod_name):
        self._products.remove(prod_name)

import copy

basket1 = Basket(['123', '345', '냥냥'])
basket2 = copy.copy(basket1)
basket3 = copy.deepcopy(basket1)

print(id(basket1))
print(id(basket2)) # 카피를 했지만 id는 다르다
print(id(basket3)) # 카피를 했지만 id는 다르다

print(id(basket1._products))
print(id(basket2._products)) # 일반 카피로 복사했을때는 카피된 객체 내의 항목 id가 같음, 인스턴스는 다르지만 값의 id가 같다. 수정 시에는 난리남.
print(id(basket3._products))


# 함수에 매개변수 전달하는 법
def mul(x,y):
    x += y
    return x

x = 10
y = 5

print(mul(x,y), x, y) # 정수 타입은 함수를 통과시킨 이후에도 원본에 변화 없음


# 이제 리스트 타입을 살펴보자

a = [1,2,3]
b = [10,20]

print(mul(a,b), a, b)
# 원본인 a에 b가 합쳐지면서 원본 자체가 변형됨
# 뭔가를 함수의 인자로 넘긴다는 것은, 해당 인자의 값을 넘기는게 아니라 해당 인자의 주소를 참조해서 넘긴다는 것
# 왜냐하면 모든 값을 다 넘기면 성능에 문제가 되기 때문
# 그래서 가변형 데이터를 함수에 넘길때는 해당 데이터의 원본이 바뀔 수 있다는 것을 염두해야 함


c = (123, 456)
d = (1,2,3)
print(mul(c,d), c, d) # 튜플은 불변형이므로 원본 변화 없음

tup1 = (1,3,4)
tup2 = (1,3,4)
st1 = '냐냐냐'
st2 = '냐냐냐'

print(id(tup1), id(tup2))
print(id(st1), id(st2))

# str, bytes, frozenset, tuple은 값이 같은 경우 id도 같다 -> 파이썬 성능을 위해