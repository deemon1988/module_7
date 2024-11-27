encode_str = [1055, 1086, 1078, 1072, 1083, 1091, 1081, 1089, 1090, 1072, 32, 1079, 1072, 1082, 1086, 1076, 1080, 1088, 1091, 1081, 32, 1101, 1090, 1086, 1090, 32, 1090, 1077, 1082, 1089, 1090]
decode_str = ''.join(chr(i) for i in encode_str)

print(decode_str)

str_ = 'Пожалуйста закодируй этот текст'
chars = []
for i in str_:
    chars.append(ord(i))
print(chars)

s = ''
for i in chars:
    s += chr(i)
print(s)

bb = b'\x68'
print(bb.decode())

from pprint import pprint

name = 'simple.txt'
file = open(name,'a')
file.write('\nHello World 2')
file.close()

file = open(name,'r')
print(file.tell())
print(file.seek(180))
pprint(file.read())
print(file.tell())
pprint(file.read())
file.close()
# print(s)