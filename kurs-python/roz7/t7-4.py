#funkcje
def fn(a, *args):
    #*args pozwala na wstawianie dowolnej ilosci zmiennych o róznym typie
    #*args wstawia nam "Taples"
    print(a)
    print(args[0:4])

fn(3,2,4,6,12, True, 'cx')

def fn1(a, *args, **dict_args):
    for arg in args:
        print(arg)
    for key in dict_args:
        print(dict_args[key])

fn1(3,5,6,8, True, 9, 'cx', user='admin', ver=1.0, db='sql')
