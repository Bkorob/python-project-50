#!/usr/bin/env python3
from generate_diff import get_print, generate_result
from cli import parse_arguments



def main():
    args = parse_arguments()
    file_path1 = args.first_file
    file_path2 = args.second.file
    get_print(generate_result(file_path1, file_path2))
    

if __name__ == '__main__':
    main()