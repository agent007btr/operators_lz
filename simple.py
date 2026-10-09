print("Введите число n от 1 до 25:")
n = int(input())
# Проверяем число
if 1 <= n <= 25:
    c = 0
    for i in range(2, n):
        if n % i == 0:
            c = c + 1
    if n >= 2 and c== 0:
        print("Y")
    else:
        print("N")
else:
    print("Ошибка")