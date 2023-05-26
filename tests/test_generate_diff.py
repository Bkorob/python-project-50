from gendiff import generate_diff
# import os

# with open(os.path.dirname(os.path.abspath(__file__))
#           + "/tests/fixtures/correct_result.txt", "r", encoding='utf-8') as f:
file1 = './tests/fixtures/file1.json'
file2 = './tests/fixtures/file1.json'
   
with open('./tests/fixtures/correct_result.txt') as f:
        result = f.read()
print(result)
a = generate_diff(file1, file2)
print(a)
def test_generate():
    with open('./tests/fixtures/correct_result.txt') as f:
        result = f.read()
        assert result == generate_diff(file1, file2)
