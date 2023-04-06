import json

filename1 = json.load(open('gendiff/files/json/file1.json', 'r'))
filename2 = json.load(open('gendiff/files/json/file2.json', 'r'))

# def generate_result(file1, file2):
#     # объявляем конечный словарь который будем возращать.
#     result = dict()
#     # проходим в цикле по ключам первого файла, сравнивая их с ключами во втором.
#     for key1 in file1:
#         if key1 in file2:
#             if file1[key1] == file2[key1]:
#                 result["  " + key1] = file1[key1]
#             else:
#                 result["- " + key1] = file1[key1]
#                 result["+ " + key1] = file2[key1]
#             result["- " + key1] = file1[key1]
#     # проходим по ключам второго файла, выполняя те же действия.
#     for key2 in file2:
#         if key2 in file1:
#             continue
#         result["+ " + key2] = file2[key2]
#     return json.dumps(result, indent=2)
# m = generate_result(file1, file2)
# print(generate_result(file1, file2))

# for x in m:
#     if x == '"':
#         x.replace('"', '')
# print(m)

import json

def generate_diff(filename1, filename2):
	print('{')
	result = {}
	for key in filename1:
		if (key in filename2) and filename2[key] == filename1[key]:
			result['  ' + key] = filename1[key]
			del filename2[key]
		elif (key in filename2) and filename2[key] != filename1[key]:
			result['- ' + key] = filename1[key]
			result['+ ' + key] = filename2[key]
			del filename2[key]
		else:
			result['- ' + key] = filename1[key]
	filename2_reduction = {f'+ {key}': v for key, v in filename2.items()}
	result.update(filename2_reduction)
	result = dict(sorted(result.items(), key=lambda x: x[0][2]))
	for key in result:
		print(key,':', result[key])
	print('}')
print(generate_diff(filename1, filename2))
# if __name__ == '__main__':
#     generate_diff(filename1, filename2)