#
counter = 1
while counter<=10 :
    
    counter +=1
    # %2 sprawdzamy czy liczba jest podzielna przez 2
    if counter % 2 !=0:
        continue
    print('Pętla działa, counter równy: ', counter)
