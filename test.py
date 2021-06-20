class A:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return True



x = [1]

a = A(x)
b = A(a.x)
c = A(x[:])
d = A(a.x[:])


print(a == b, b == c, c == d)
