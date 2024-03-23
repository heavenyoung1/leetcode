import re

# Открываем файл для чтения
with open('IN_DMZ.txt', 'r') as file:
    # Читаем все строки файла
    lines = file.readlines()

# Создаем словарь для хранения значений
dictionary = {}

# Проходимся по каждой строке
for line in lines:
    # Удаляем символ новой строки
    line = line.strip()

    # Пытаемся найти совпадение с регулярным выражением
    match = re.match(r'diag\.ai\.uso3_3', line)
    if match:
        # Если совпадение найдено, присваиваем значение
        dictionary[line] = 'Корзина АИ, модуль УСО 3.3'

# Выводим результат
with open('OUT_DMZ.txt', 'w') as output_file:
    # Выводим результат в новый файл
    for key, value in dictionary.items():
        output_file.write(f'{key}: {value}\n')