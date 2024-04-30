#!/usr/bin/nv python3

class Uzivatel:

  def __init__(self, jmeno, heslo, vek):
    self.__jmeno = jmeno
    self.__heslo = heslo
    self.__vek = vek

  def prihlasit(self, heslo):
    pass

  def odhlasit(self):
    pass

  def nastav_vahu(self, zvire):
    pass

class Administrator(Uzivatel):

  def __init__(self, jmeno, heslo, vek, telefon):
    super().__init__(jmeno, heslo, vek)
    self.__telefon = telefon

  def pridej_zvire(self, zvire):
    pass

  def vymaz_zvire(self, zvire):
    pass
