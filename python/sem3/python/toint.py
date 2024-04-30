#!/usr/bin/env python3

def toInt(string):
  vysledek = ""
  for char in string:
    try:
      pomocna = int(char)
    except:
      continue
  
    vysledek = vysledek + str(pomocna)

  return(int(vysledek))


