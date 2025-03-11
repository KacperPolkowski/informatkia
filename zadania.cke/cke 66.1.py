def suma_cyfr(liczba): #liczba jest jako string
    suma = 0
    for cyfra in liczba:
        sum += int(cyfra)
    return suma

lista_trojke = []
with open("trojki.txt") as plik:
    for linia in plik:
        lista_trojke.append(linia.split())
print(lista_trojke)