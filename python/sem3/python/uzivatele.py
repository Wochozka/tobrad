#!/usr/bin/env python3
"""
Program zadava uzivatele do csv souboru
Umi je oddelit strednikem nebo carkou
"""
class Uzivatel:

  def __init__(self, poradi):
    self.jmeno = input("Zadej jmeno {0}. uzivatele:".format(poradi))
    self.prijmeni = input("Zadej prijmeni {0}. uzivatele:".format(poradi))

def main(vystup, carka=False):
  uzivatele = []

  pocet = int(input("Kolik bude uzivatelu:"))

  for a in range(pocet):
    u = Uzivatel(a+1)
    uzivatele.append(u)

  f = open(vystup, "w")
  if carka:
    f.write("Jmeno,Prijmeni\n")
  else:
    f.write("Jmeno;Prijmeni\n")

  for a in range(len(uzivatele)):
    print(uzivatele[a].jmeno, uzivatele[a].prijmeni)
    if carka:
        f.write(uzivatele[a].jmeno + "," + uzivatele[a].prijmeni + "\n")
    else:
        f.write(uzivatele[a].jmeno + ";" + uzivatele[a].prijmeni + "\n")

  f.close()

def processArgs():
    import argparse
    
    p = argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
    
    p.add_argument("-v", "--verbosity", type=int, choices=[0,1,2], default=0, help="vybere vyrecnost programu")
    p.add_argument("-o", "--output", help="nazev vystupniho souboru")
    p.add_argument("--comma", action="store_true", help="pouzije carku namisto stredniku")

    return p.parse_args()

if __name__ == "__main__":
    args = processArgs()
    print(args)
    main(args.output, carka=args.comma)
