#!/usr/bin/env python3

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