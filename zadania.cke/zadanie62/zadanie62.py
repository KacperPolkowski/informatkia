liczby8 = []
with open("C:\\Users\\DELL\\Documents\\PyGame\\informatkia\\zadania.cke\\zadanie62\\liczby2.txt") as plik:
    for linia in plik:
        liczby8.append(linia.strip())
print(liczby8)
minimum = int(liczby8[0])
maks = int(liczby8[0])
for i in range (1,len(liczby8)):
    if minimum > int(liczby8[i]):
        minimum = int(liczby8[i])
    if maks < int(liczby8[i]):
        maks = int(liczby8[i])
print(minimum, maks)
pierwszy = int(liczby8[0])
ilosc = 1
maksymalnaIlosc = 1
for i in range(len(liczby8)-1):
    if int(liczby8[i])<=int(liczby8[i+1]):
        ilosc +=1
        if ilosc > maksymalnaIlosc:
            maksymalnaIlosc = ilosc
            pierwszyMaks = pierwszy
    else:
        pierwszy = int(liczby8[i+1])
        ilosc = 1 
print(maksymalnaIlosc, pierwszyMaks)