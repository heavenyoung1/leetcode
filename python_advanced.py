# Oh shitt, we here going again

from math import sqrt

a = int(input())
b = int(input())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(sqrt(a**10 + b**10))

#Короткое решение

print(*(lambda a, b: (a + b, a - b, a * b, a / b, a // b, a % b, (a ** 10 + b ** 10)** 0.5))(int(input()), int(input())), sep = '\n')

m = float(input())
h = float(input())
bdi = m / (h ** 2)
if (bdi >= 18.5 and bdi <= 25) :
  print('Оптимальная масса')
elif (bdi < 18.5) :
  print('Недостаточная масса')
else:
  print('Избыточная масса')

s = str(input())
rub = (len(s) * 60) // 100
cop = (len(s) * 60) % 100
print(f'{rub} руб. {cop} коп.')

