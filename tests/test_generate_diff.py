from gendiff import generate_diff
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish
import pytest


@pytest.mark.parametrize(
        "file1, file2, format, correct_result",[
            ('./tests/fixtures/flat1.json',
             './tests/fixtures/flat2.json',
             'stylish',
             './tests/fixtures/correct_result_flat.txt'
             ),
            ('./tests/fixtures/flat1.yml',
             './tests/fixtures/flat2.yaml',
             'stylish',
             './tests/fixtures/correct_result_flat.txt'
             ),
            ("./tests/fixtures/flat1.yml",
             "./tests/fixtures/flat2.json",
             'stylish',
             "./tests/fixtures/correct_result_flat.txt"
             ),
            ("./tests/fixtures/tree1.yml",
             "./tests/fixtures/tree2.yml",
             'stylish',
             "./tests/fixtures/correct_result_tree_stylish.txt",
             ),
            ("./tests/fixtures/tree1.yml",
             "./tests/fixtures/tree2.yml",
             'plain',
             "./tests/fixtures/correct_result_tree_plain.txt"
             ),
            ("./tests/fixtures/tree1.yml",
             "./tests/fixtures/tree2.yml",
             'json',
             "./tests/fixtures/correct_result_tree_json.txt"
             )
             ]
             )
def test_generate_diff(file1, file2, format, correct_result):
    with open(correct_result) as cr:
        result = cr.read()
        diff = generate_diff(file1, file2, format_name=format)
        assert result == diff
        
        
def test_unsupported_format_file():
    file1 = "./tests/fixtures/flat1.yml"
    file2 = "./tests/fixtures/flat2.txt"
    try:
        generate_diff(file1, file2)
    except ValueError as v:
        assert v
