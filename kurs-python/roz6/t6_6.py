#tuple przydatne operacje
my_list = [10, 4, 5, 17, 7, 2, 5, 2]
my_tuple = tuple(my_list)
print(min(my_tuple))
print(sum(my_tuple))
a,b,c,d,e,f,g,h, = my_tuple
#przypisuje wartości z tuple do kolejnych zmiennych
print(a,b,c,d,e,f,g,h,)