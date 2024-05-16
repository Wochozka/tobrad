#!/usr/bin/env python3

import csv


def write_csv_file(filename, data):
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file, delimiter=';')
            csv_writer.writerows(data)
        print(f"Data byla úspěšně uložena do CSV souboru '{filename}'.")
    except IOError:
        print(f"Nastala chyba při zápisu do souboru '{filename}'.")


if __name__ == "__main__":
    # Název CSV souboru, do kterého chceme uložit data
    output_csv_file = 'output_data.csv'
    
    # Testovací data k uložení do CSV souboru (seznam seznamů)
    data_to_save = [
        ['Name', 'Age', 'City'],
        ['John', 30, 'New York'],
        ['Alice', 25, 'Los Angeles'],
        ['Bob', 35, 'Chicago']
    ]
    
    # Zavolání funkce pro uložení dat do CSV souboru
    write_csv_file(output_csv_file, data_to_save)
