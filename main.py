# -*- coding: utgit branch --show-currentf-8 -*-
"""
Created on Fri Jul 30 15:26:36 2021

@author: espje
"""

from pylab import *
from math import pi

# Informasjon om konstanter, konstante krefter og gjenstanden.
# Konstanter
g = 9.81  # tyngdeakselerasjonen i m/s^2
ro_luft = 1.2 # lufttethet i kg/m3
Cd = 0.47 # dragtallet for kuleforme
# Målingene
masse_gummi = 1.8380 * 10 ** -3 # massen til ballongen selv(bare gummi)
omkretsen = 0.38 # omkretsen i meter

Vo = omkretsen ** 3 / (6 * pi ** 2)

masse_ballong_totalt = masse_gummi + Vo * ro_luft  # massen til gjenstanden i kg

G = masse_ballong_totalt * g  # gravitasjonskraften i N

A = omkretsen / (4 * pi) # tverrsnittarealet
#d = omkretsen / pi # diameter fra omkretsen

Od = ro_luft * Vo * g


def a(v):
    L = 0.5 * ro_luft * Cd * A * v ** 2
    sum_F = L + Od - G  # kraftsum i N
    return sum_F / masse_ballong_totalt  # akselerasjon i m/s^2


# Startverdier for bevegelsen
s = 0.59  # startposisjon i m
v = 0  # startfart i m/s
t = 0.2  # starttid i s

# Simuleringsteknisk
t_slutt = 0.65  # tidspunktet simuleringen stopper ved i s
dt = 0.01  # tidssteg i s
s_verdier = [s]  # liste for lagring av posisjoner
v_verdier = [v]  # liste for lagring av farter
t_verdier = [t]  # liste for lagring av tidspunkt

# Løkke som kalkulerer alle t-, v-, og x-verdier
while t < t_slutt:
    v = v + a(v) * dt  # regner ut neste v og overskriver gammel
    s = s + v * dt  # regner ut neste x og overskriver gammel
    t += dt  # regner ut neste t og overskriver gammel

    t_verdier.append(t)  # legger til ny t-verdi i listen for t
    v_verdier.append(v)  # legger til ny v-verdi i listen for v
    s_verdier.append(s)  # legger til ny s-verdi i listen for s

# Leser inn data fra filen og legger dem inn i arrayer.
# Det lages en array for hver måling.
# skiprows = 1 hopper over første rad i tekstfilen (med beskrivelse av dataene).
data = loadtxt("Ballong forsøk.txt", skiprows = 1)

# Graftegning
plot(data[0:, 0], data[0:, 1], "*")
plot(t_verdier, s_verdier)
title("Strekning som funksjon av tid")
xlabel("$t$ / s")  # navn på førsteaksen, $ gir kursiv tekst
ylabel("$s$ / m")  # navn på andreaksen, $ gir kursiv tekst
grid()
show()
