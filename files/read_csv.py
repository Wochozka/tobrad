#!/usr/bin/env python3

import csv


def read_csv_file(filename):
    rows = []  # Inicializace seznamu pro ukládání řádků z CSV souboru

    try:
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter=';')
            for line in csv_reader:
                rows.append(line)
        print(f"CSV soubor '{filename}' byl úspěšně načten.")
        return rows
    except FileNotFoundError:
        print(f"Soubor '{filename}' nebyl nalezen.")
        return None
    except IOError:
        print(f"Nastala chyba při čtení souboru '{filename}'.")
        return None


if __name__ == '__main__':
    # Název CSV souboru, který chceme načíst
    csv_file = 'tabulka.csv'
    
    # Zavolání funkce pro načtení obsahu CSV souboru
    csv_data = read_csv_file(csv_file)

    # Výpis načtených dat z CSV souboru
    if csv_data:
        print("Obsah CSV souboru:")
        for row in csv_data:
            print(row)
