# для проверки корректности ввода по хорошему необходимо использовать try except, но мы данную конструкцию не проходили
# тем не менее в логику сию проверку я добавлю.
test = int(input())
isPrime = True
if type(test) is not int:
    print ("Вы ввели не число")
else:
    for i in range(2,(test+1)//2,1):
        if test % i == 0:
            isPrime = False
    if isPrime:
        print(f"{test}  - Простое число")
    else:
        print(f"{test}  - Не простое число")
