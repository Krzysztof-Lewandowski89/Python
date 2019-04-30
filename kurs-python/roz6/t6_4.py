#tuple ("krotka")
values = (1, 2, 3, 'abc, True')
for v in values:
    print(v)
values[2] = 45
#tu wyrzuci błąd bo w tuples nie można modyfikować danych
print(values[2])