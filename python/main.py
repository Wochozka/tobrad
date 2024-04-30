#!/usr/bin/env python3

from bojovnik import Bojovnik
from kostka import Kostka

class Arena:

    def __init__(self, bojovnik_1, bojovnik_2, kostka):
        self._bojovnik_1 = bojovnik_1
        self._bojovnik_2 = bojovnik_2
        self._kostka = kostka

    def _vykresli(self):
        self._vycisti()
        print('----------------- Arena ----------------- \n')
        print('Zdraví bojovníků: \n')
        print(f'{self._bojovnik_1} {self._bojovnik_1.graficky_zivot()}')
        print(f'{self._bojovnik_2} {self._bojovnik_2.graficky_zivot()}')

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


kostka = Kostka(10)
bojovnik = Bojovnik("Zalgoren", 100, 20, 10, kostka)
souper = Bojovnik('Shadow', 60, 18, 15, kostka)

a = Arena(bojovnik, souper, kostka)
a.zapas()