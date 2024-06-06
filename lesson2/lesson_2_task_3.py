import math
side = float(input("Введите сторону квадрата: "))

def square(a):
    return math.ceil(a*a)

print(square(side))
