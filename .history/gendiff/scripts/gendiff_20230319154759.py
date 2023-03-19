#!/usr/bin/env python3
import argparse


def main():
    # Создание описания программы.
    parser = argparse.ArgumentParser(
        description = "Compares two configuration files and shows a difference."
        )
    # Назначение именовынных аргументов (позиционные обозначаются, как "-..."/"--...").
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    print(args)
if __name__ == '__main__':
    main()