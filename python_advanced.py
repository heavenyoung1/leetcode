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

# ЗАДАЧА ИОСИФА ФЛАВЕЛЯ. НУЖНО ЗАПОМНИТЬ, ЗАДАЧА РЕАЛЬНО КРУТАЯ!

def opr(n, k):
  count = 0
  soldiers = [str(n - i) for i in range(n)]
  
  if k == 1:
    return soldiers[0]
  elif k != 1:
    while (len(soldiers) != 1):
      for i in range(len(soldiers)-1, -1, -1):
        count += 1
        if count == k:
          soldiers.pop(i)
          count = 0
    return soldiers[0]

n, k = int(input()), int(input())
print(opr(n, k))

# Программа должна вывести количество точек, лежащих в каждой координатной четверти, как в примерах.

def quadrant(coordinates):
    q1, q2, q3, q4 = 0, 0, 0, 0
    for x, y in coordinates:
        if x > 0 and y > 0:
            q1 += 1
        elif x < 0 and y > 0:
            q2 += 1
        elif x < 0 and y < 0:
            q3 += 1
        elif x > 0 and y < 0:
            q4 += 1
    return q1, q2, q3, q4

n = int(input())
coordinates = [map(int, input().split()) for _ in range(n)]

q1, q2, q3, q4 = quadrant(coordinates)

print(f"""
      Первая четверть: {q1}
      Вторая четверть: {q2}
      Третья четверть: {q3}
      Четвертая четверть: {q4}
""")

# На вход программе подается строка текста из натуральных чисел. Из неё формируется список чисел. Напишите программу подсчета количества чисел, которые больше предшествующего им в этом списке числа. 


count = 0
i = 0
s = str(input())
str_split = s.split()
int_split = [int(i) for i in str_split]
while i <= len(int_split) - 2:
  if int_split[i + 1] > int_split[i]:
    i += 1
    count += 1
  elif int_split[i + 1] <= int_split[i]:
    i += 1
print(count)

# На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел. Напишите программу, которая меняет местами соседние элементы списка (a[0] c a[1], a[2] c a[3] и т.д.). Если в списке нечетное количество элементов, то последний остается на своем месте.

import sys

num = [int(n) for n in input().split()]
if len(num) == 1:
  print(num[0])
  exit()
elif len(num) % 2 == 0:
  for i in range(0, len(num) - 1, 2):
    num[i], num[i + 1] = num[i + 1], num[i]
    #print(num)
elif len(num) % 2 != 0:
  for i in range(0, len(num) - 2, 2):
    num[i], num[i + 1] = num[i + 1], num[i]

# На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел. Напишите программу циклического сдвига элементов списка направо, когда последний элемент становится первым, а остальные сдвигаются на одну позицию вперед, в сторону увеличения индексов.


print(*num)

from itertools import combinations

def ring():
  n = int(input())
  list = [int(input()) for _ in range(n)]
  #print(list)
  comp = int(input())
  
  for i in combinations(list, 2):
    if i[0] * i[1] == comp:
      return "ДА"
    else:
      continue
  return "НЕТ"
    
print(ring())

m = {'к-к': 'ничья', 'к-н': 'Тимур', 'к-б': 'Руслан', 'н-н': 'ничья','н-б': 'Тимур', 'н-к': 'Руслан', "б-б": 'ничья','б-к': 'Тимур','б-н': 'Руслан'}
d1, d2 = str(input()), str(input())
res = f'{d1[0]}-{d2[0]}'

m_items = m.items()
for key, value in m_items:
  if key == res:
    print(value)


s = str(input())
c = 0
max = 0
s = list(s)
for i in s:
  if i == 'О':
    c = 0
  elif i == 'Р':
    c += 1
    if c > max:
      max = c
    
print(max)


abv = [chr(i) for i in range(ord('а'), ord('я') + 1)]
s = str(input()) + f' запретил букву'
word = f'{s}'
for i in abv:
  if i in s:
    word = f'{word} {i}'
    print(word)
    word = word.replace(i, '').replace('  ', ' ').lstrip(' ').rstrip(' ')


list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

x = 7000
list1[2][2].append(x)
print(list1)


n = int(input())
list = [[i for i in range(1, n + 1)] for j in range(n)]

for i in list:
  print(i)
print()



# ЗАДАЧА НА НАХОЖДЕНИЕ ТРЕУГОЛЬНИКА ПАСКАЛЯ

import math as ma

def pascal(n: int):
  list = []
  temp = [1, 1]
  if n == 0:
    list.append(1)
  elif n == 1:
    list.extend(temp)
  elif n > 1:
    list.extend(temp)
    c = 1
    for m in range(1, n):
      c = ma.factorial(n) / (ma.factorial(m) * ma.factorial(n - m))
      c = int(c)
      list.insert(1, c)

  return list
      
n = int(input())
print(pascal(n))


#РЕШАЕМ МАТРИЦЫ. Напишите программу, которая сначала считывает элементы матрицы один за другим, затем выводит их в виде матрицы.

row, cols = int(input()), int(input()) 
a = []

a = [[input() for j in range(cols)] for i in range(row)]

for i in range(row):
  for j in range(cols):
    print(a[i][j], end = ' ')
  print()

# Напишите программу, которая считывает элементы матрицы один за другим, выводит их в виде матрицы, выводит пустую строку, и снова ту же матрицу, но уже поменяв местами строки со столбцами: первая строка выводится как первый столбец, и так далее.

row, cols = int(input()), int(input()) #ряды, столбцы
a = []

a = [[input() for j in range(cols)] for i in range(row)]

for i in range(row):
  for j in range(cols):
    print(a[i][j], end = ' ')
  print()

print()

for i in range(cols):
  for j in range(row):
    print(a[j][i], end = ' ')
  print()

#  Напишите программу, которая выводит след заданной квадратной матрицы.

n = int(input()) #ряды, столбцы
count = 0
a = []
for i in range(n):
  temp = [int(i) for i in input().split()]
  a.append(temp)

for row_i, row in enumerate(a):
    for col_i, col in enumerate(row):
      if row_i == col_i:
        count += col
      
print(count)

# Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке, больших среднего арифметического элементов данной строки.

from functools import reduce

n = int(input()) #ряды, столбцы
max = []
count = 0
a = []
for i in range(n):
  temp = [int(i) for i in input().split()]
  a.append(temp)

for row_i, i in enumerate(a):
  count = 0
  for col_i, j in enumerate(i):
    av = reduce(lambda x, y: x + y, i) / n
    if j > av:
      count += 1
  max.append(count)

for _ in max:
  print(_)

# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.



