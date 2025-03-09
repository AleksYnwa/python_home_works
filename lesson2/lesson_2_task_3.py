from math import ceil

def square(x):
    s = x ** 2
    return s

x = float(input("Длина стороны квадрата: "))
result = square(x)
rounded_result = ceil(result)
print(f"Площадь квадрата округленная в большую сторону: {rounded_result}")

