import sys
from struct import *

input_file = sys.argv[1]

# mudar para ser por stdin no futuro :D
file = open(input_file, 'rb')

dictionary = {
    0: 'broken-\n',
    1: 'on-----\n',
    2: 'off----\n',
    3: 'unknown\n',
}
compressed_data = []

while True:
    rec = file.read(2)
    if len(rec) != 2:
        break

    p1 = rec[0]
    p2 = rec[1]

    p1 = p1 >> 1
    short = (p1 << 8) ^ p2
    to_unpack = short >> 1

    compressed_data.append(to_unpack)

decompressed_data = ""
string = ""
next_code = len(dictionary)

for current_code in compressed_data:

    if not (current_code in dictionary):
        dictionary[current_code] = string + (string[:8])
    decompressed_data += dictionary[current_code]

    if not (len(string) == 0):
        dictionary[next_code] = string + (dictionary[current_code][:8])
        next_code += 1
    string = dictionary[current_code]

print(decompressed_data, end='')
file.close()

with open('file.txt', 'w') as file:
    file.write(decompressed_data)
