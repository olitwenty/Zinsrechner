#!/usr/bin/env python3

import os
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("-d", "--darlehen", dest="darlehen", nargs=2, type=int, required=True, help="Größe des Darlehens")
parser.add_argument("-z", "--zinssatz", dest="zinssatz", nargs=2, type=float, required=True, help="Zinssatz")
parser.add_argument("-t", "--tilgung", dest="tilgung", nargs=2, type=float, required=True, help="Anfängliche jährliche Tilgung")

args = parser.parse_args()
maxDarlehen = args.darlehen[0]
minDarlehen = args.darlehen[1]
maxZinssatz = args.zinssatz[0] / 100
minZinssatz = args.zinssatz[1] / 100
maxTilgung = args.tilgung[0] /100
minTilgung = args.tilgung[1] /100


fJahr = "Jahr: {:<15}Restschuld: {:<15.2f}Tilgung: {:<15.2f}"
fInfo = "Darlehen(Euro): {:<15.2f}Zinsatz(%): {:<15.2f}Anfängliche Tilgung(%): {:<15.2f}Monatliche Rate(Euro): {:<15.2f}"


def orange(start, stop, step):
    return [start-step*x for x in range(round((start-stop)/step))]

def rek(darlehen, zinssatz, jahre):
    if darlehen < rate*12:
        file.write(fJahr.format(jahre, darlehen, darlehen))
        file.close()
        return
    else:
        file.write(fJahr.format(jahre, darlehen, rate * 12 - (darlehen * zinssatz), rate * 12)+"\n")
        return rek((darlehen - (rate * 12 - (darlehen * zinssatz))), zinssatz, jahre + 1)
    
os.mkdir("Kreditrechnungen")
for d in orange(maxDarlehen, minDarlehen, 10000):
    os.mkdir("Kreditrechnungen/"+str(d)+"_Euro")
    for z in orange(maxZinssatz, minZinssatz, 0.005):
        os.mkdir("Kreditrechnungen/"+str(d)+"_Euro/"+str(z)+"_Zinssatz(%)")
        for t in orange(maxTilgung, minTilgung, 0.005):
            file = open("Kreditrechnungen/"+str(d)+"_Euro/"+str(z)+"_Zinssatz(%)/"+str(t)+"Tilgung(%).txt", "w", newline="\n")
            rate = (z + t) * d / 12
            file.write(fInfo.format(d, z*100, t*100, rate)+"\n")
            rek(d, z, 0)