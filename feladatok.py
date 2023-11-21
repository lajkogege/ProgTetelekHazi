import math

##1-	Számold meg, hogy hány darab 7-tel osztható szám van 1-1000 között!
def elso():
    print("1.feladat:")
    hettel_oszthato=0
    for i in range(1 ,1000, 1):
        if i %7 ==0:
            hettel_oszthato+=1
    print(f"1 és 1000 között {hettel_oszthato} dh héttel osztható szám van.", hettel_oszthato)
    return hettel_oszthato

#2-	Számold meg, hogy hány darab 12-vel osztható szám van 2000-20000 között!
def masodik():
    print("2.feladat")
    tizenektovel_oszthato=0
    for i in range (2000, 20000, 1):
        if i %12 ==0:
            tizenektovel_oszthato+=1
    print(f"2000 és 2000 között {tizenektovel_oszthato} db 12-vel osztható szám van.", tizenektovel_oszthato)
    return tizenektovel_oszthato

#3-	Írd ki az első 20 3-mal osztható szám négyzetének összegét!
def harmadik():
    print("3.feladat:")
    harommal_osztahto=0
    szam=0
    while not (harommal_osztahto != 20):
        if szam%3 ==0:
            szam:int = szam + szam
        harommal_osztahto+=1
    print(math.sqrt(szam))
    return szam

#4-	Keresd meg egy szám egész osztóit!
def negyedik():
    print("4.feladat:")
    szam:int=int(input("Kérek egy számot: "))
    for i in range (0, 1, szam):
        if szam % 1 ==0:
            print(f"{i}")
    return szam

#5-	Keresd meg egy szám legnagyobb egész osztóját!
def otodik():
    print("5.feladat:")
    szam:int=int(input("Kérek egy számot: "))
    osztoja:int= 0
    for i in range (0,szam,0):
        if szam % i ==0:
            if osztoja < i:
                osztoja == i
            i +=1
    print(f"A {szam} legnagyobb osztoja: {osztoja}")
    return szam

#6-	Vizsgáljuk meg, hogy egy adott szám prímszám-e!
def hatodik():
    print("6.feladat:")
    szam:int=int(input("Kérek egy számot: "))
    if szam<2:
        print(f"{szam} nem prímszám.")
    else:
        primszam:bool=True
        for i in range(2, int(szam**0.5) + 1):
        if szam % i == 0:
            primszam = False
       if primszam:
           print(f"{szam} prímszám.")
       else:
           print(f"{szam} nem prímszám.")
        return szam

#7-	Számold meg, hogy hány négyzetszám van 0-100000 között!
def hetedik():
    print("7.feladat:")
    szam:int=int(input("Kérek egy számot: "))
    negyzett:int=0
    negyzett_osszesen:int=0
    for i in range (0, 100001, 1):
        negyzett=szam **2
        if negyzett <=100000:
            negyzett_osszesen+=1
    print(f"0-tól 100000-ig {negyzett_osszesen} négyzett szám van")
    return negyzett_osszesen




