#!/usr/bin/python3
import json
from gendiff.modules.gendiff.py import generate_result


file1 = json.load(open('gendiff/files/json/file1.json', 'r'))
file2 = json.load(open('gendiff/files/json/file2.json', 'r'))

def main():
    generate_result(file1, file2)


if __name__ == '__main__':
    main()