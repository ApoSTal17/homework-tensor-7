
import os

print(f'Имя операционной системы: {os.uname().sysname}')  # Имя операционной системы: Linux
print(f'Имя пользователя, вошедшего в терминал: {os.getlogin()}')  # Имя пользователя, вошедшего в терминал: antoni
print(f'Список файлов и директорий в директории python-progs: {os.listdir(path="/home/antoni/python-progs")}')
# Список файлов и директорий в директории python-progs: ['lesson-7', 'lesson-3', 
# 'lesson-5', 'test1.py', 'lesson-4', 'lesson-6', 'lesson-2', 'hello-app']