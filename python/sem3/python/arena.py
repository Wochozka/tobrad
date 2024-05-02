#!/usr/bin/env python3

import kostka
import bojovnik

class Arena():
  
  def __init__(self, bojovnik1, bojovnik2, kostka):
    self.__bojovnik1 = bojovnik1
    self.__bojovnik2 = bojovnik2
    self._kostka = kostka

  def __vykresli(self):
    self.__vycistiObrazovku()
    print("-------------- Arena s bojovniky --------------\n")
    print("Bojovnici:")
    self.__vykresliBojovnika(self.__bojovnik1)
    self.__vykresliBojovnika(self.__bojovnik2)

  def __vycistiObrazovku(self):
    import sys as _sys
    import subprocess as _subprocess
    if _sys.platform.startswith("win"):
      _subprocess.call(["cmd.exe", "/C", "cls"])
    else:
      _subprocess.call("clear")

  def __vypisZpravu(self, zprava):
    import time as _time
    print(zprava)
    _time.sleep(1)

  def __vykresliBojovnika(self, bojovnik):
    print(bojovnik)
    print("Zivot {0}".format(bojovnik.grafickyUkazatel(bojovnik._zivot, bojovnik._maxZivot)))
    if bojovnik.__class__.__name__=="Mag":
      print("Mana {0}".format(bojovnik.grafickaMana()))

  def zapas(self):
    import random as _random

    self.__vykresli()
    print("Vitejte v Arene!")
    print("Dnes se utkaji {0} a {1}.".format(self.__bojovnik1, self.__bojovnik2))

    if _random.randint(0, 1):
      (self.__bojovnik1, self.__bojovnik2) = (self.__bojovnik2, self.__bojovnik1)

    while (self.__bojovnik1.nazivu and self.__bojovnik2.nazivu):
      self.__bojovnik1.utoc(self.__bojovnik2)
      self.__vykresli()
      self.__vypisZpravu(self.__bojovnik1.getZprava())
      self.__vypisZpravu(self.__bojovnik2.getZprava())
      if (self.__bojovnik2.nazivu):
        self.__bojovnik2.utoc(self.__bojovnik1)
        self.__vykresli()
        self.__vypisZpravu(self.__bojovnik2.getZprava())
        self.__vypisZpravu(self.__bojovnik1.getZprava())


k = kostka.Kostka(20)
b1 = bojovnik.Bojovnik("Adam", 100, 50, 40, k)
b2 = bojovnik.Mag("Dan", 80, 55, 45, k, 50, 100)

a = Arena(b1, b2, k)
a.zapas()























