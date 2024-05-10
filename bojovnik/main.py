#!/usr/bin/env python3

from bojovnik import Bojovnik
from kostka import Kostka


class Mag(Bojovnik):
    def __init__(self, jmeno, zivot, utok, obrana, kostka, mana, magicky_utok):
        super().__init__(jmeno, zivot, utok, obrana, kostka)
        self._mana = mana
        self._max_mana = mana
        self._magicky_utok = magicky_utok

    def utoc(self, souper):
        if self._mana < self._max_mana:
            self._mana = self._mana + 10
            if self._mana > self._max_mana:
                self._mana = self._max_mana
            super().utoc(souper)
        else:
            uder = self._magicky_utok + self._kostka.roll()
            zprava = f'{self._jmeno} utoci magii za {uder} hp.'
            self.nastav_zpravu(zprava)
            self._mana = 0
            souper.bran_se(uder)

    def graficka_mana(self):
        return self.graficky_ukazatel(self._mana, self._max_mana)


class Arena:

    def __init__(self, bojovnik_1, bojovnik_2, kostka):
        self._bojovnik_1 = bojovnik_1
        self._bojovnik_2 = bojovnik_2
        self._kostka = kostka

    def _vykresli(self):
        self._vycisti()
        print('----------------- Arena ----------------- \n')
        print('Bojovnici: \n')
        self._vypis_bojovnika(self._bojovnik_1)
        self._vypis_bojovnika(self._bojovnik_2)

    def _vycisti(self):
        import sys as _sys
        import subprocess as _subprocess
        if _sys.platform.startswith('win'):
            _subprocess.call(['cmd.exe', '/C', 'cls'])
        else:
            _subprocess.call(['clear'])

    def _vypis_zpravu(self, zprava):
        import time as _time
        print(zprava)
        _time.sleep(0.75)

    def zapas(self):
        import random as _random
        print('Vítejte v Areně!')
        print(f'Dnes se utkají {self._bojovnik_1} a {self._bojovnik_2}!')
        print('Zápas může začít...', end=' ')
        input()

        if _random.randint(0, 1):
            self._bojovnik_1, self._bojovnik_2 = self._bojovnik_2, self._bojovnik_1

        while self._bojovnik_1.je_nazivu() and self._bojovnik_2.je_nazivu():
            self._bojovnik_1.utoc(self._bojovnik_2)
            self._vykresli()
            self._vypis_zpravu(self._bojovnik_1.vypis_zpravu())
            self._vypis_zpravu(self._bojovnik_2.vypis_zpravu())
            if self._bojovnik_2.je_nazivu():
                self._bojovnik_2.utoc(self._bojovnik_1)
                self._vykresli()
                self._vypis_zpravu(self._bojovnik_2.vypis_zpravu())
                self._vypis_zpravu(self._bojovnik_1.vypis_zpravu())

    def _vypis_bojovnika(self, bojovnik):
        print(bojovnik)
        print(f'Zivot: {bojovnik.graficky_zivot()}')
        if isinstance(bojovnik, Mag):
            print(f'Mana: {bojovnik.graficka_mana()}')


kostka = Kostka(10)
bojovnik = Bojovnik("Zalgoren", 100, 20, 10, kostka)
souper = Bojovnik('Shadow', 60, 18, 15, kostka)
mag = Mag('Gandalf', 60, 15, 12, kostka, 30, 45)

a = Arena(mag, souper, kostka)
a.zapas()