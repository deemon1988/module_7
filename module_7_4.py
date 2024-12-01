import os
import time
from itertools import count

# print('Текущая директория:', os.getcwd())
# if os.path.exists('second'):
#     os.chdir('second')
# else:
#     os.mkdir('second')
#     os.chdir('second')
# print('Текущая директория:', os.getcwd())
# #os.makedirs(r'third\fourth')
# print(os.listdir())
# for i in os.walk('.'):
#     print(i)
#
# os.chdir(r'D:\PythonProjects\Urban_university\module_7')
# print('Текущая директория:', os.getcwd())
#
# file =  [f for f in os.listdir() if os.path.isfile(f)]
# dirs =  [d for d in os.listdir() if os.path.isdir(d)]
# print(file)
# print(dirs)
# #os.startfile(file[0])
# print(os.stat(file[0]).st_size)
# os.system('pip install random2')

print('Текущая директория:', os.getcwd())


def print_directories(path):
    # Проверяем, является ли path директорией
    if os.path.isdir(path):
        print(f'Директория: {path}')
        # Проходим по всем элементам в каталоге
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):  # Если это подкаталог
                print_directories(item_path)  # Рекурсивный вызов


# Запуск с текущей директории
print_directories(os.getcwd())


excluded_dirs = {'.git', '.idea', '.venv'}

for root, dirs, files in os.walk('.'):
    print(dirs)
    # Удаляем из обхода все папки из списка исключений
    dirs[:] = [d for d in dirs if d not in excluded_dirs]
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(root)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}')
