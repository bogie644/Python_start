# coding : utf-8
import os
import psutil
import sys
import shutil
import random


def show_menu():
    print('Здорово!\n Вот, что я умею: \n '
          '1. Вывести имя директории и спискок файлов\n '
          '2. Вывести информацию о системе\n '
          '3. Вывести список процессов\n '
          '4. Продублировать файлы в текущей директории\n '
          '5. Удалить дубликаты из выбрааной директории\n '
          '6. Дублировать указанный файл\n '
          '7. Удалить слц=учайный файл из выбранной директории')


def duplication(filename):
    if os.path.isfile(filename):
        new_file = filename + '.dupl'
        shutil.copy(filename, new_file)
        if os.path.exists(new_file):
            print('Файл ', new_file, ' успешно скопирован')
        else:
            print('Ошибка копирования')


def del_dupl(directory):
    file_list = os.listdir(directory)
    x = 0
    for f in file_list:
        fullname = os.path.join(directory, f)
        if fullname.endswith('.dupl'):
            os.remove(fullname)
            x += 1
    print('Удаленно ', x, ' дубликатов', os.listdir())

def del_random_file(directory):
    file_list = os.listdir(directory)
    new_list = []
    for filename in file_list:
        if os.path.isfile(filename):
            new_list.append(filename)
    x = random.randint(0, len(new_list))
    fullname = os.path.join(directory, new_list[x])
    os.remove(fullname)
    print('Удаленно ', fullname)

def duble_files(dirname):
    file_list = os.listdir(dirname)
    for f in file_list:
        duplication(f)


def sys_info():
    print('Инофрмация о системе:'
          '\nПлатформа системы: ', sys.platform,
          '\nКодировка системы:', sys.getfilesystemencoding(),
          '\nКолличкство процессов: ', os.cpu_count(),
          '\n Логин пользователя: ', os.getlogin())


def main():
    print('Привет! Меня зовут, робот Тома!')
    name = input('А как твое имя?: ')
    print('Привет, ', name)
    answer = ''
    while answer != 'Q':
        answer = input('Хочешь со мной поработать? (Y(Да)/N(Нет)/Q(Выход)')
        if answer == 'Y':
            show_menu()
            do = int(input('Your choise: '))
            if do == 1:
                print('Текущая директория: ', os.getcwd())
                print('Список файлов в директории:', os.listdir())
            elif do == 2:
                sys_info()
            elif do == 3:
                print('Список процессов', psutil.pids())
            elif do == 4:
                print('Текущая директория: ', os.getcwd())
                duble_files('.')
                # file_list = os.listdir()
                # print('Список файлов в директории:', file_list)
                # for f in file_list:
                #     duplication(f)
            elif do == 5:
                print('Текущая директория: ', os.getcwd())
                answer = input('Хотите очистить текущую директорию? (Y/N)')
                if answer == 'Y':
                    directory = os.getcwd()
                else:
                    directory = input('Введите полдный путь к директории, которую хотите отчистить от дублей: ')
                del_dupl(directory)
            elif do == 6:
                print('Текущая директория: ', os.getcwd())
                file_list = os.listdir()
                print(file_list)
                filename = input('Введите файл, который хотите дублировать: ')
                duplication(filename)
            elif do == 7:
                filename = input('Введите директорию, в которой хотите удалить случайный файл: ')
                del_random_file(filename)

            else:
                pass
        elif answer == 'N':
            print('It is bad!')
        else:
            print('Error!')

if __name__ == '__main__':
    main()
