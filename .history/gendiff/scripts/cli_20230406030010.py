#!/usr/bin/env python3
import argparse
from gendiff.modules.gendiff import generate_result


def main():
    # Создание описания программы.
    # ArgumentParser читает аргументы КС, которые мы передаём.
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    # Назначение именовынных аргументов
    # Порядок назначения элементов влияет на очерёдность передачи.
    parser.add_argument('file1', help='first_file')
    parser.add_argument('file2', help='second_file')
    # Назначемние позиционных рагументов,
    # help - описание аргумента для представления -h
    parser.add_argument('-f', '--format', help='set format of output')
    # parse_args создаёт структуру принимающую данные.
    args = parser.parse_args()
    file1, file2 = args.first_file, args.second_file
    generate_result(file1, file2)

 
    
 
if __name__ == '__main__':
    main()
