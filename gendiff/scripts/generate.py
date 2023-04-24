#!/usr/bin/env python3
from gendiff.generate_diff import get_dict_print, generate_result
from gendiff.cli import parse_arguments



def main():
    pathes = parse_arguments()
    file_path1 = pathes.first_file
    file_path2 = pathes.second_file
    get_dict_print(file_path1, file_path2)
    

if __name__ == '__main__':
    main()