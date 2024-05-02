#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Zdravici():

	def pozdrav(self, jmeno, prijmeni):
		print("Ahoj osobo jmenem {0} {1}!".format(jmeno, prijmeni)

zdrav = Zdravici()
jmenoAPrijmeni = input("Zadej jmeno a prijmeni:")
zdrav.pozdrav(jmenoAPrijmeni.split(" ")[0], jmenoAPrijmeni.split(" ")[1])



