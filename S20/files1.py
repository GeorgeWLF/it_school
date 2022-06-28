# TEXT
# biti pe HD ----> decodare ----> vizualizare
#                    UTF-8

# BINAR
# biti pe HD ----> decodare ----> vizualizare
#                    codec

# Mod de lucru
# w = write
# r = read
# a = append

# Mod de lucru binar
# wb = write binary
# rb = read binary
# ab = append binary

# IO = input/output

# SEEK
# din modulul os
# os.SEEK_SET - inceputul fis.
# os.SEEK_CUR - pozitia curenta
# os.SEEK_END - sfarsitul fisierului

import os

file_txt = "E:\Python it-school\S20\practice.txt"

file_descriptor = open(file_txt)

# print(type(file_descriptor))
# print(file_descriptor)
content = file_descriptor.read()

# citim poz curenta a cursorului
print(file_descriptor.tell())

# ne miscam in fisier
file_descriptor.seek(0, os.SEEK_SET)


# CLOSE THE FILE !!!!
file_descriptor.close()

# 1 caracter = 1 byte

# print(f"Fisierul are dimensiunea: {len(content)} bytes")
