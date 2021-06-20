# # 클래스

class UserInfo:
    # 클래스는 속성과 메소드로 구성된다
    def __init__(self, name): # 초기화 필수
        self.name = name
    def userName(self):
        print("Name: ", self.name)

user1 = UserInfo('배승민')
user1.userName()


# # 클래스 상속
# # 부모 클래스 = 수퍼 클래스, 자식 클래스 = 서브 클래스
# # 자식 클래스는 부모의 모든 속성과 메소드를 사용할 수 있다

# class Car:
#     """parent class"""
#     def __init__(self, type, color):
#         self.type = type
#         self.color = color
#     def show(self):
#         return 'Car 클래스 show 메소드'

# class BMWCar(Car):
#     """sub class"""
#     def __init__(self, car_name, type, color):
#         super().__init__(type, color)
#         self.car_name = car_name
#     def show_model(self) -> None:
#         return '자동차 이름은: {} 입니다'.format(self.car_name)

# class MercedesCar(Car):
#     """sub class"""
#     def __init__(self, car_name, type, color):
#         super().__init__(type, color)
#         self.car_name = car_name
#     def show_model(self) -> None:
#         return '자동차 이름은: {} 입니다'.format(self.car_name)
#     def show(self):
#         print(super().show())
#         return '부모 메소드 오버라이딩'





# # 일반적인 사용 방법

# model1 = BMWCar('베엠베', '세단', '그레이')
# model2 = MercedesCar('벤츠', '세단', '옐로우')

# print(model1.car_name, model1.type, model1.color, model1.show())
# print(model2.car_name, model2.type, model2.color)

# car1_info = model1.show_model()
# print(car1_info)

# # 메소드 오버라이딩
# print(model1.show())
# print(model2.show())


# # parent method direct call
# model3 = MercedesCar('벤츠2', 'SUV', '검정')
# print(model3.show())

# # 상속 관계를 조회하는 메소드 inheritence info
# print(BMWCar.mro())



