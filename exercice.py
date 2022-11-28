#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math


# TODO: Définissez vos fonction ici
def compute_volume_and_mass(a, b, c, masse_vol):
    volume = 4/3 * math.pi * a * b * c
    masse = masse_vol * volume
    return volume, masse

def valide(saisie):
    v = 'atgc'
    if len(saisie) != 0 and set(saisie).issubset(v):
        result = True
    else:
        result = False
    return result

def saisie(type):
    inp = input(f"Entrez une {type} d'ADN valide: ")
    inp = input('saisir')
    if valide(inp):
        return inp
    else:
        return 'not valide'

    #print(f"La {ìnp} n'est pas valide")
    return saisie(type)

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
        print(compute_volume_and_mass(2,4,6,10))
        print(valide('at'))
        print(valide(''))
        print(valide('g'))
        print(valide('s'))



