#!/usr/bin/env python3

class Uzivatel:

  def __init__(self, poradi):
    self.jmeno = input("Zadej jmeno {0}. uzivatele:".format(poradi))
    self.prijmeni = input("Zadej prijmeni {0}. uzivatele:".format(poradi))

uzivatele = []

pocet = int(input("Kolik bude uzivatelu:"))

for a in range(pocet):
  u = Uzivatel(a+1)
  uzivatele.append(u)

x = ""
try:
  f = open("uzivatele.csv", "r")
  x = f.readline()
  f.close()
  mod = "a"
except:
  mod = "w"
f = open("uzivatele.csv", mod)
if x == ("Jmeno;Prijmeni\n"):
  pass
else:
  f.write("Jmeno;Prijmeni\n")

for a in range(len(uzivatele)):
  print(uzivatele[a].jmeno, uzivatele[a].prijmeni)
  f.write(uzivatele[a].jmeno + ";" + uzivatele[a].prijmeni + "\n")

f.close()


