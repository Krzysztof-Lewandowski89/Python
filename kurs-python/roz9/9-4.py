#funkcja jako obiekt pierwszej klasy
def add(a,b):
    return a + b

def multiply(a,b):
    return a * b

def apply(fn, a, b):
    #tu w miejsce fn musimy podac którąś z wczesniej zdefiniowanych
    #funkcji add lub multiply
    return fn(a,b)

r1 = apply(add, 3, 4)
r2 = apply(multiply, 3, 4)
print(r1, r2)