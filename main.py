# main.py
from functions import inf, srednie, edycja, edycja_listy, dodaj_nowe_oceny

uczen = {
    'imie': 'Sebastian',
    'nazwisko': 'Weroński',
    'wiek': 14,
    'matematyka': [5, 3, 2, 3, 4, 5],
    'angielski': [2, 3, 4, 5, 6, 1],
    'polski': [5, 3, 2, 4]
}

while True:
    print("===" * 25)
    print("e - wyjdź z programu")
    print("i - informacje o uczniu")
    print("s - średnia ocen")
    print("ed - edytuj dane")
    print("oc - edytuj oceny")
    print("===" * 25)
    inp = input().lower()
    if 'e' == inp:
        break
    elif 's' == inp:
        srednie(uczen)
    elif 'i' == inp:
        inf(uczen)
    elif 'ed' == inp:
        edycja(uczen)
    elif 'oc' == inp:
        dodaj_nowe_oceny(uczen)
    else:
        print("Program zakończył działanie")
        break

