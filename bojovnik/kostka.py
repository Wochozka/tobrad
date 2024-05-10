#!/usr/bin/env python3

import random


class Kostka:
    def __init__(self, number_of_sides=6):
        self.__number_of_sides = number_of_sides

    def roll(self):
        return random.randint(1, self.__number_of_sides)

    def __str__(self):
        return f'Toto je kostka s {self.__number_of_sides} stenami.'

    def getNum_of_sides(self):
        return self.__number_of_sides

    def setNum_of_sides(self, num_of_sides):
        if num_of_sides > 0:
            self.__number_of_sides = num_of_sides
        else:
            print('Cislo musi byt kladne.')

    def setNum_of_sides_usr(self):
        try:
            num_of_sides = int(input("Zadej pozadovany pocet sten:"))
            if num_of_sides > 0:
                self.setNum_of_sides(num_of_sides)
            else:
                print('Cislo musi byt kladne.')
        except:
            print("Zadani musi byt klandne cislo.")


if __name__ == '__main__':
    pass