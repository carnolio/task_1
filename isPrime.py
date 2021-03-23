
isPrime = True
try:
    test = int(input("Введите проверяемое число: "))
except Exception:
    print('Пожалуйста введите натуральное число')
else:
    for i in range(2,(test//2)+1,1):
        if test % i == 0:
            isPrime = False
    if isPrime:
        print(f"{test}  - Простое число")
    else:
        print(f"{test}  - Не простое число")
