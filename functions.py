# functions.py
def inf(dc):
    for k, v in dc.items():
        print(f"{k}:  {v}")

def srednie(dc):
    srednia_m = sum(dc['matematyka']) / len(dc['matematyka'])
    print(f"Matematyka srednia {srednia_m}")
    srednia_a = sum(dc['angielski']) / len(dc['angielski'])
    print(f"Angielski srednia {srednia_a}")
    srednia_p = sum(dc['polski']) / len(dc['polski'])
    print(f"Polski srednia {srednia_p}")

def edycja(dc):
    print("wprowadz klucz jaki chcesz edytować")
    print("===" * 25)
    inf(dc)
    print("===" * 25)
    inp = input()
    dc[inp] = input("Podaj nowe dane")

def edycja_listy(lst):
    while True:
        print(lst)
        print('a - dodaj element')
        print('u - usun element')
        print('e - wyjdz z edycji list')
        inp = input()
        if 'a' == inp:
            ocena = float(input())
            lst.append(ocena)
            print('ocena dodana')
        elif 'u' == inp:
            ocena = float(input())
            lst.remove(ocena)
            print('ocena usunieta')
        elif 'e' == inp:
            break
        else:
            print("Nie ma takiej komendy")

def dodaj_nowe_oceny(dc):
    print("Edytuj oceny")
    print("Matematyka - a")
    print("Angielski - b")
    print("Polski - c")
    inp = input()
    if inp == 'a':
        edycja_listy(dc['matematyka'])
    elif inp == 'b':
        edycja_listy(dc['angielski'])
    elif inp == 'c':
        edycja_listy(dc['polski'])
    print("dodaj_nowe_oceny - zakonczylo dzialanie")

