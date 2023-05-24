#!/usr/bin/env python3
import gendiff  # импортиуем в скрипт модуль gendiff, предварительно
# импортировав в __init__ функции get_dict_print и parse_arguments
# из файлов модуля.


def main():
    pathes = gendiff.parse_arguments()  # присваиваем переменной pathes
    # функцию-парсер
    # присваиваем пееменным пути файлов, прочитанные парсером
    file_path1 = pathes.first_file
    file_path2 = pathes.second_file
    # принтуем вызов основной фунции, с указанными ранее переменными
    gendiff.get_final_result(file_path1, file_path2)


if __name__ == '__main__':
    main()
