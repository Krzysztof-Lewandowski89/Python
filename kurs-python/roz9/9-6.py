# Generatory
def number_generator(end):
    n = 0
    nums = []
    while n < end:
        nums.append(n)
        n += 1
    return nums

values = number_generator(10)
print(values)
###################################
def number_gen(end):
     n = 0
     while n < end:
         yield n
         n += 1

val = number_gen(12)
#print(next(val))
#print('cos innego')
#print(next(val))
#print(next(val))
#print(next(val))
for v in val:
    print(v)
