
from random import randint

poczatek=["Uważam, że", "Wydaje mi się, że", "Moim zdaniem", "Jak wszyscy wiemy"]
srodek=["każdy może mieć rację","szkoła wymaga dużo pracy","szła dzieweczka do laseczka","słońce wschodzi na wschodzie a zachodzi na zachodzie","Ala ma kota", "jesteś szalona"]
koniec=["i to tyle.",", nie mam nic do dodania.", ", hej!",", co należało udowodnić!","a kot ma Alę.",", mówię Ci."]

poczatek_len=len(poczatek)
srodek_len=len(srodek)
koniec_len=len(koniec)


while True:
    poczatek_wybor=randint(0,poczatek_len-1)
    srodek_wybor=randint(0,srodek_len-1)
    koniec_wybor=randint(0,koniec_len-1)
    print(poczatek[poczatek_wybor],srodek[srodek_wybor],koniec[koniec_wybor])
    input()

