# Домашнее задание по теме "Позиционирование в файле"

def custom_write(file_name, strings:list):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    c_str = 0
    for i in strings:
        c_str += 1
        b = file.tell()
        strings_positions[(c_str,b)] = i
        file.write(f"{i}\n")
    file.close()
    for elem in strings_positions.items():
        print((elem))

file = open('products.txt', 'r', encoding='utf-8')
strings = file.read()
strings = strings.split('\n')
strings_list = [i for i in strings if len(i)]
file.close()
custom_write('custom.txt',strings_list)

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

custom_write('custom.txt', info)
