#!/usr/bin/env python3

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("-d", "--darlehen", dest="darlehen", nargs=1, type=int, required=True, help="Größe des Darlehens")
parser.add_argument("-z", "--zinssatz", dest="zinssatz", nargs=1, type=float, required=True, help="Zinssatz")
parser.add_argument("-t", "--tilgung", dest="tilgung", nargs=1, type=float, required=True, help="Anfängliche jährliche Tilgung")

args = parser.parse_args()
darlehen = args.darlehen[0]
zinssatz = args.zinssatz[0] / 100
tilgung = args.tilgung[0] /100
rate = (zinssatz + tilgung) * darlehen / 12

print(rate)

def rek(darlehen, jahre):
    if darlehen < rate:
        return jahre
    else:
        print(jahre, darlehen, rate-darlehen*zinssatz)
        return rek((darlehen - (rate * 12 - (darlehen * zinssatz))), jahre + 1)
    
rek(darlehen, 0)

print(darlehen)
print(zinssatz)
print(tilgung)
print(darlehen * ((zinssatz + tilgung) / 100) / 12)