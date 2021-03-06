cyfry = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

podstawa = int(input("Podaj podstawę: "))
assert podstawa >= 2 and podstawa <= len( cyfry ), "Błędna podstawa {podstawa}"

liczba = input(f"Podaj liczbę o podstawie {podstawa}: ")

podstawa2 = int(input("Podaj podstawę na którą chcesz przeliczyć: "))
assert podstawa2 >= 2 and podstawa2 <= len( cyfry ), "Błędna podstawa {podstawa2}"

n = 0
for i in range( len(liczba) ):
  n *= podstawa
  cyfra = cyfry.find( liczba[i] )
  n += cyfra # zapis skrócony

print(f"Liczba {liczba} o podstawie {podstawa}: na wartość: {n} (dziesiętną)")

wynik = ""
while n > 0:
  cyfra = cyfry[ n % podstawa2 ]
  wynik = cyfra + wynik
  n = n // podstawa2

print(f"Liczba {liczba} o podstawie {podstawa}: na wartość: {wynik} (w podstawie {podstawa2})")