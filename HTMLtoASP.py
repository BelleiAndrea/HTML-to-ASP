#!/usr/bin/python
import sys
def Succ(pos):
    a = file_r.read(1)
    file_r.seek(pos,0)
    return a

def raccogliASP(indice):
    global c
    while not (c == "%" and Succ(file_r.tell()) ==">"):
        file_w.write(c)
        c = file_r.read(1)
    file_w.write("%>\n")
    return 0
try:
    nomefile = str(sys.argv[1])
    dirout = str(sys.argv[2])
except IndexError:
        print "\033[91mERRORE: Sintassi HTMLtoASP.py [File input] [Directory output]\033[0m"
        sys.exit()
file_r = open(nomefile,"rt")
file_w = open(dirout + "solo_asp.asp","wt")
while 1:
    c = file_r.read(1)
    if not c:
        break
    if c == "<" and Succ(file_r.tell()) == "%":
        raccogliASP(file_r.tell())
print "\03392m[SUCCESSO: Salvato in " + dirout + "/solo.asp\033[0m"
file_r.close()
file_w.close()