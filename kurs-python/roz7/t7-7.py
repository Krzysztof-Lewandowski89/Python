# Scope, zasięg zmiennych
x = 1

def fn():
    global x
    #teraz mozemy pracowac na "x" z zasięgu globalnego
    x += 1
    y = 3
    print(x,y)

fn()
print(x)
