print('''
P1 - "W Pythonie, jak nazywa si� 'pude�ko' w kt�rym trzymamy dane?
a - tekst
b - zmienna
c - pude�ko na buty
''')
odpowiedz = input().lower()

if odpowiedz == "a":
    print(" Niestety - tekst to typ danych :( ")
elif odpowiedz == "b":
    print(" Zgadza sie!! :) ")
elif odpowiedz == "c":
    print(" Chyba si� wyg�upiasz... :( ")
else:
    print(" Nie wybra�a�/wybra�e� a, b or c :( ")

