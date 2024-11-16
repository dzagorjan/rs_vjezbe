broj = 0
while broj < 5:
    broj +=2
    print(broj)

# ispisati ce se 2, 4, 6 jer u zadnjem koraku broj ima vrijednost 4 i uvjet je još uvijek True tako da se varijabli broj dodaje 2, tek nakon toga uvjet je False


broj = 0
while broj < 5:
    broj +=1
    print(broj)
    broj -=1

# petlja je beskonacna jer vrijednost broja ostaje uvijek ista, odnosno 0, jer se u istoj iteraciji broj poveca za jedan i odmah smanji za 1


broj = 10
while broj > 0:
    broj -=1
    print(broj)
    if broj < 5:
        broj +=2
        print ("Broj")

# kada vrijednost broja postane manja od 5, dolazi do povecanja broja, tako da petlja postaje beskonacna, jer uvjet while broj > 0 nikada ne postaje false