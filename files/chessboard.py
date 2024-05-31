#!/usr/bin/env python3

def num_row():
    for field in range(1, 65):
        if field == 64:
            print(f'{field}.')
        else:
            print(f'{field}, ', end='')

def num_fields():
    fields = range(1, 65)
    for row in range(1,9):
        for column in range(1,9):
            print(fields[column-1], end='')
        print()

1 12345678
2 910111213141516
3 1718192021222324

if __name__ == '__main__':
    num_fields()

