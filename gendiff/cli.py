import argparse


def parse_arguments():
    # Создание описания программы.
    # ArgumentParser читает аргументы КС, которые мы передаём.
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    # Назначение именовынных аргументов
    # Порядок назначения элементов влияет на очерёдность передачи.
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    # Назначемние позиционных рагументов,
    # help - описание аргумента для представления -h
    # создание именованного аргумента
    parser.add_argument('-f', '--format', help='set format of output')
    # parse_args создаёт структуру принимающую данные.
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    parse_arguments()