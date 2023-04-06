#!/usr/bin/env python3
import argparse
from gendiff.modules.gendiff import generate_result, first_file, second_file


def main():
    # Создание описания программы.
    # ArgumentParser читает аргументы КС, которые мы передаём.
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    # Назначение именовынных аргументов
    # Порядок назначения элементов влияет на очерёдность передачи.
    parser.add_argument('file1', metavar='first_file')
    parser.add_argument('file2', metavar='second_file')
    # Назначемние позиционных рагументов,
    # help - описание аргумента для представления -h
    parser.add_argument('-f', '--format', help='set format of output')
    # parse_args создаёт структуру принимающую данные.
    args = parser.parse_args()
    print(args)

 
if __name__ == '__main__':
    main()
    file1 = first_file, file2 = second_file
    generate_result(first_file, second_file)
