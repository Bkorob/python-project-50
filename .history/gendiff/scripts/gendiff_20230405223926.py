#!/usr/bin/python3
from cli import parser
from gendiff.modules.gendiff import generate_result


def main():
    generate_result(parser.add_argument('first_file'), 
                    parser.add_argument('second_file')
                    )
