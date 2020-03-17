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


f = "Jahr: {:<15}Restschuld: {:<15.2f}Tilgung: {:<15.2f}"

def orange(start, stop, step):
    return [start-step*x for x in range(round((start-stop)/step))]

def rek(darlehen, zinssatz, jahre):
    if darlehen < rate*12:
        print(f.format(jahre, darlehen, darlehen))
        return
    else:
        print(f.format(jahre, darlehen, rate*12-darlehen*zinssatz))
        return rek((darlehen - (rate * 12 - (darlehen * zinssatz))), zinssatz, jahre + 1)
    
for d in orange(maxDarlehen, minDarlehen, 10000):
    for z in orange(maxZinssatz, minZinssatz, 0.005):
        for t in orange(maxTilgung, minTilgung, 0.005):
            rate = (z + t) * d / 12
            print(rate)
            rek(d, z, 0)

#os.mkdir("test")
#os.mkdir("test/abc")
#f = open("test/"+str(maxDarlehen)+".txt", "w", newline="\n")
#f.write("jnljnjkbnl\n")
#f.write("kshvksajjsd")
#f.close()

#print(maxDarlehen)
#print(zinssatz)
#print(tilgung)
#print(maxDarlehen * ((zinssatz + tilgung) / 100) / 12)