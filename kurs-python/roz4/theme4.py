# name = input('Podaj swoje imie:')
# if len(name) < 3:
#     print('Podaj minimum trzy znaki!')
# else: 
#     print(name)



a = int(input('Podaj liczbę całkowitą a: '))
b = int(input('Podaj kolejną liczbę całkowitą b: '))
if a == b:
    print('Liczby a i b są równe')
else:
    if a>b:
        c = a-b
        print('Liczba a jest większa o:',c)
    else:
        if a<b:
            c = b-a
            print('Liczba b jest większa o:',c)