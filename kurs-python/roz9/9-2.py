#Dane mutowalne/ niemutowalne
a = [1, 2]
#do tego mozemy sie odwołać, ale jak damy nawias () to stanie się
#taples i wtedy nie bd mogli się odwołaś
a[0] = 1000
print(a)

        ########
my_list = [3,4]
my_tuples = (1,2, my_list)
print(my_tuples)
my_tuples[2].append(5)
print(my_tuples)
#tu mozemy dodać "5tke" bo list jest mutowalne

