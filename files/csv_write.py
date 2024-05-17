#!/usr/bin/env python3

import csv


def write_csv_file(filename, data):
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        csv_writer = csv.writer(file, delimiter=';')
        csv_writer.writerows(data)
    print('Writing Ok.')

if __name__ == '__main__':
    output_filename = 'data.csv'

    data = [
        ['Jmeno', 'Prijmeni', 'Vek'],
        ['David', 'Svarc', '39'],
        ['Tobias', 'Radkovsky', '13']
    ]

    write_csv_file(output_filename, data)

