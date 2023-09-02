from gendiff import generate_diff


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
        
        
def test_generate_tree_yml_tree():
    file1 = "./tests/fixtures/tree1.yml"
    file2 = "./tests/fixtures/tree2.yml"
    with open("./tests/fixtures/correct_result_tree.txt") as cr:
        result = cr.read()
        diff = generate_diff(file1, file2)
        assert result == diff