from gendiff import generate_diff
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish



def test_generate_json_flat_diff():
    file1 = './tests/fixtures/flat1.json'
    file2 = './tests/fixtures/flat2.json'
    with open('./tests/fixtures/correct_result_flat.txt') as cr:
        result = cr.read()
        diff = generate_diff(file1, file2)
        assert result == diff


def test_generate_different_yml_formats_diff():
    file1 = './tests/fixtures/flat1.yml'
    file2 = './tests/fixtures/flat2.yaml'
    with open('./tests/fixtures/correct_result_flat.txt') as cr:
        result = cr.read()
        diff = generate_diff(file1, file2)
        assert result == diff

        
def test_different_format_file():
    file1 = "./tests/fixtures/flat1.yml"
    file2 = "./tests/fixtures/flat2.json"
    with open("./tests/fixtures/correct_result_flat.txt") as cr:
        result = cr.read()
        diff = generate_diff(file1, file2)
        assert result == diff
        
        
def test_generate_tree_yml_stylish_format():
    file1 = "./tests/fixtures/tree1.yml"
    file2 = "./tests/fixtures/tree2.yml"
    with open("./tests/fixtures/correct_result_tree_stylish.txt") as cr:
        result = cr.read()
        diff = generate_diff(file1, file2, formatter=stylish)
        assert result == diff
        
        
def test_unsupported_format_file():
    file1 = "./tests/fixtures/flat1.yml"
    file2 = "./tests/fixtures/flat2.txt"
    try:
        generate_diff(file1, file2)
    except ValueError as v:
        assert v

def test_generate_plain_format():
    file1 = "./tests/fixtures/tree1.yml"
    file2 = "./tests/fixtures/tree2.yml"
    with open("./tests/fixtures/correct_result_tree_plain.txt") as cr:
        result = cr.read()
        diff = generate_diff(file1, file2, formatter=plain)
        assert result == diff