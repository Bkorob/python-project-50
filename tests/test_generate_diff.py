from gendiff import generate_diff


def test_generate_some():
    file1 = './tests/fixtures/file1.json'
    file2 = './tests/fixtures/file2.json'
    with open('./tests/fixtures/correct_result.txt') as f:
        result = f.read()
        diff = generate_diff(file1, file2)
        assert result == diff


def test_generate_different():
    file1 = './tests/fixtures/file1.json'
    file2 = './tests/fixtures/file3.json'
    with open('./tests/fixtures/correct_result2.txt') as f:
        result = f.read()
        diff = generate_diff(file1, file2)
        assert result == diff


def test_generate_same():
    file1 = './tests/fixtures/file1.json'
    file2 = './tests/fixtures/file1.json'
    with open('./tests/fixtures/correct_result3.txt') as f:
        result = f.read()
        diff = generate_diff(file1, file2)
        assert result == diff