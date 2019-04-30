#return - wartości zwracane

def fn(a, b):
    return a + b, a*b, a-b
    #return jest to funkcja zakanczajaca funkcje! Nic co po niej nie bedzie wykonane w tej funkcji.
    #print(ok!)
    #Ok nie zostanie zwrocone bo jest PO return

r = fn(3,4)
print("r równa się: ", r)
#tu zwroci Tample z 3 wartościami z return
print(r[1])
#tu zwroci wartość z indeksu 1