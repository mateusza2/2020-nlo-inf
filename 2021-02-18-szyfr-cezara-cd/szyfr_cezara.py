# Praca domowa

def szyfr_cezara(klucz, napis):
    wynik = ""
    for x in napis:
        if x.isalpha():
            kodlitery = ord(x)
            # sprawdzamy, czy mamy mala czy wielka litere
            # sprawdzić, czy kod litery >= 65 oraz <= 90
            
            koda = ord('A' if 'A' <= x <= 'Z' else 'a')

            numerlitery = kodlitery - koda

            numerliterysz = numerlitery + klucz
            if numerliterysz > 25:
                numerliterysz = numerliterysz - 26
            if numerliterysz < 0:
                numerliterysz = numerliterysz + 26

            kodliterysz = numerliterysz + koda

            literasz = chr(kodliterysz)
            #print(x, kodlitery, numerlitery, numerliterysz, kodliterysz, literasz)
            wynik = wynik + literasz
        else:
            wynik = wynik + x
    return wynik

wiadomosc = "Kraer nzrufdfjt, tzvbrnv bkf futqpkr."

for k in range(1, 25):
    x = szyfr_cezara(-k, wiadomosc)
    print(k, x)


# Szyfr Cezara w przeglądarce:
# https://cryptii.com/pipes/caesar-cipher