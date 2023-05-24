from gendiff import generate_diff

file1 = 'tests/fixtures/file1.json'
file2 = 'tests/fixtures/file2.json'

def test_generate():
    result = open('tests/fixtures/correct_result.txt').read()
    assert result == generate_diff(file1, file2)