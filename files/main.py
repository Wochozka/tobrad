#!/usr/bin/env python3

cinnost = "cteni"

if cinnost == 'cteni':
    f = open('test', 'r')
    obsah = f.read()
    for char in obsah:
        print(char)


elif cinnost == 'zapis':
    f = open('test', 'w')
    f.write('Hello world!\n')
    f.write('dalsi radek')
    f.close()
