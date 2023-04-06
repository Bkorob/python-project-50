#!/usr/bin/python3
from cli import parser
from gendiff.modules.gendiff import generate_result


def main():
    generate_result(parser.firs_file, parser.second_file)
