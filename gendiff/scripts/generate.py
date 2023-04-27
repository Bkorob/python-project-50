#!/usr/bin/env python3
import gendiff


def main():
    pathes = gendiff.parse_arguments()
    file_path1 = pathes.first_file
    file_path2 = pathes.second_file
    gendiff.get_dict_print(file_path1, file_path2)


if __name__ == '__main__':
    main()
