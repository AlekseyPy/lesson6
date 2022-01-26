print("Summa = 1+3+5+7+...+n")
n = int(input("Введите значение n: "))
x = 1
summa = 0
while x<=n:
    summa += x     #summa=summa+x
    x += 2
    print(summa)
