# SET (zbiór)
a = set([1,2,3,4,2,4,3,5,6])
b = set([1,3,7,9])
print(a)
print(b)
#zwróci zbiór liczb (bez powtórzeń)
print(type(a))

print(a.intersection(b))
#pokaże część wspolna zbiorów a i b
print(a.union(b))
#dodanie zbiorów
print(a.difference(b))
#róznica zbiorów
print(a.symmetric_difference(b))
#róznica symetryczna (jakie wartości są unikalne w a oraz b )