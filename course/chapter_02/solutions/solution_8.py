a = int(input())
b = input()
if (a >= 18) and (b == "Y"):
    print("Добро пожаловать в клуб!")
elif (0 < a < 18) or (b == "N"):
    print("Извините, вход запрещен.")
else:
    print("Введите корректные значения.")