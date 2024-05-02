#!/usr/bin/env python3

"""
Bojovnik
"""


class Bojovnik:
    """
    Trida reprezentujici bojovnika do areny.
    """

    def __init__(self, jmeno, zivot, utok, obrana, kostka):
        self._jmeno = jmeno
        self._zivot = zivot
        self._max_zivot = zivot
        self._utok = utok
        self._obrana = obrana
        self._kostka = kostka
        self._zprava = ''

    def __str__(self):
        return str(self._jmeno)

    def je_nazivu(self):
        if self._zivot > 0:
            return True
        else:
            return False

    def graficky_zivot(self):
        celkem = 20
        pocet = int(self._zivot / self._max_zivot * celkem)
        if pocet == 0 and self.je_nazivu():
            pocet = 1
        return f"[{'#'*pocet}{' '*(celkem-pocet)}]"

    def bran_se(self, uder):
        zraneni = uder - (self._obrana + self._kostka.roll())
        if zraneni > 0:
            zprava = f'{self._jmeno} utrpel poskozeni o sile {zraneni} hp.'
            self._zivot = self._zivot - zraneni
            if self._zivot < 0:
                self._zivot = 0
                zprava = f'{zprava[:-1]} a zemrel.'
        else:
            zprava = f'{self._jmeno} odrazil utok.'
        self.nastav_zpravu(zprava)

    def utoc(self, souper):
        uder = self._utok + self._kostka.roll()
        zprava = f'{self._jmeno} utoci s uderem za {uder} hp.'
        self.nastav_zpravu(zprava)
        souper.bran_se(uder)

    def nastav_zpravu(self, zprava):
        self._zprava = zprava

    def vypis_zpravu(self):
        return self._zprava










