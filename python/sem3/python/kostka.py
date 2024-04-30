#!/usr/bin/env python3

class Kostka:
  """
  Trida reprezentujici hraci kostku.
  """

  def __init__(self, pocetSten=6):
    self.setPocetSten(pocetSten)

  def hod(self):
    import random
    return random.randint(1, self.__pocetSten)

  def getPocetSten(self):
    return self.__pocetSten

  def setPocetSten(self, novyPocetSten):
    try:
      novyPocetSten = int(novyPocetSten)
      if novyPocetSten > 0:
        self.__pocetSten = novyPocetSten
      else:
        print("Pocet sten musi byt kladny.")
    except:
      print("Pocet sten musi byt datovy typ INT!")

  def __str__(self):
    return "Kostka s {0} stenami.".format(self.__pocetSten)

