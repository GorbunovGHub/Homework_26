import os
import time

directory = 'D:\\PythonProjects\\Urban_University\\Homework_26'


for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)
        file_time = os.path.getctime(file_path)
        formatted_time = time.strftime('%d.%m.%Y %H:%M', time.localtime(file_time))
        file_size = os.path.getsize(file_path)
        parent_dir = os.path.dirname(file_path)
        print(f'Обнаружен файл: {file}, Путь: {file_path}, '
              f'Размер: {file_size} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
