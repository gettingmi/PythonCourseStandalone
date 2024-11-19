a = int(input())
b = int(input())
c = int(input())
if (a <= b + c) and (b <= a + c) and (c <= a + b):
    print("Такой треугольник существует")
else:
    print("Такой треугольник не существует")