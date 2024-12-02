# Домашнее задание по теме "Файлы в операционной системе"

import os
import time

excluded_dirs = {'.git', '.idea', '.venv'}

for root, dirs, files in os.walk('.'):
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
