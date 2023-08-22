from gendiff import generate_diff


def test_json_generate_some():
    file1 = '../tests/fixtures/file1.json'
    file2 = '../tests/fixtures/file2.json'
    with open('../tests/fixtures/correct_result.txt') as cr:
        result = cr.read()
        diff = generate_diff(file1, file2)
        assert result == diff


def test_json_generate_different():
    file1 = '../tests/fixtures/file1.json'
    file2 = '../tests/fixtures/file3.json'
    with open('../tests/fixtures/correct_result2.txt') as cr:
        result = cr.read()
        diff = generate_diff(file1, file2)
        assert result == diff


def test_json_generate_same():
    file1 = '../tests/fixtures/file1.json'
    file2 = '../tests/fixtures/file1.json'
    with open('../tests/fixtures/correct_result3.txt') as cr:
        result = cr.read()
        diff = generate_diff(file1, file2)
        assert result == diff
        
        
def test_yml_generate_diff():
    file1 = "../tests/fixtures/file1.yml"
    file2 = "../tests/fixtures/file2.yml"
    with open("../tests/fixtures/correct_result.txt") as cr:
        result = cr.read()
        diff = generate_diff(file1, file2)
        assert result == diff
        
def test_yaml_different_format():
    file1 = "../tests/fixtures/file1.yml"
    file2 = "../tests/fixtures/file2.yml"
    with open("../tests/fixtures/correct_result.txt") as cr:
        result = cr.read()
        diff = generate_diff(file1, file2)
        assert result == diff