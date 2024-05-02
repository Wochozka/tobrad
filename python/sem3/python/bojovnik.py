#!/usr/bin/env python3

class Bojovnik:
  """
  Trida reprezentujici bojovnika.
  """

  def __init__(self, jmeno, zivot, utok, obrana, kostka):
    self._jmeno = jmeno
    self._zivot = zivot
    self._maxZivot = zivot
    self.__utok = utok
    self.__obrana = obrana
    self._kostka = kostka
    self._zprava = ""

  def __str__(self):
    return str(self._jmeno)

  @property
  def nazivu(self):
    return self._zivot > 0

  def grafickyUkazatel(self, aktualni, maximalni):
    celkem = 20
    pocet = int(aktualni / maximalni * celkem)
    if (pocet == 0 and self.nazivu):
      pocet = 1
    return "[{0}{1}]".format("#"*pocet, " "*(celkem-pocet))

  def branSe(self, uder):
    zraneni = uder - (self.__obrana + self._kostka.hod())
    if zraneni > 0:
      zprava = "{0} utrpel zraneni o sile {1}.".format(self._jmeno, zraneni)
      self._zivot = self._zivot - zraneni
      if self._zivot < 0:
        self._zivot = 0
        zprava = zprava[:-1] + " a zemrel."
    else:
      zprava = "{0} zcela odrazil utok.".format(self._jmeno)
    self._setZprava(zprava)


  def utoc(self, souper):
    uder = self.__utok + self._kostka.hod()
    souper.branSe(uder)

  def _setZprava(self, zprava):
    self._zprava = zprava

  def getZprava(self):
    return self._zprava

class Mag(Bojovnik):

  def __init__(self, jmeno, zivot, utok, obrana, kostka, mana, magickyUtok):
    super().__init__(jmeno, zivot, utok, obrana, kostka)
    self._mana = mana
    self._maxMana = mana
    self._magickyUtok = magickyUtok

  def utoc(self, souper):
    if self._mana < self._maxMana:
      self._mana = self._mana + 10
      if self._mana > self._maxMana:
        self._mana = self._maxMana
      super().utoc(souper)
    else:
      uder = self._magickyUtok + self._kostka.hod()  
      zprava = "{0} pouzil magii za {1}".format(self._jmeno, uder)
      self._setZprava(zprava)
      self._mana = 0
      souper.branSe(uder)      

  def grafickaMana(self):
    return self.grafickyUkazatel(self._mana, self._maxMana)




