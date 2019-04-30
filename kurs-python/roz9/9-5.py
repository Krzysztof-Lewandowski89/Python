#Dekoratory

def my_decorator(fn):
    def wrapper():
        print('początek odliczania')
        fn()
        print('koniec odliczania')
    return wrapper

@my_decorator
#dodajemy dekorator przed funkcja ktora chcemy "udekorować"
def get_5_values():
    for v in range(1,6):
        print(v)

#get_5_values_decorated = my_decorator(get_5_values)
#get_5_values_decorated()
get_5_values()