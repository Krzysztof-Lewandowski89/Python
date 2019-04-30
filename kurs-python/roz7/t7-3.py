#funkcje, argumenty kluczowe
def fn(a,b=0,c=0):
    print('a:', a, 'b:', b, 'c:', c)

fn(2)
fn(2, c=4)
#do a przypisze 2, b bedzie domyslne, c =4
fn(2,c=5, b=3)
# mozna tez przypisywac wartosci do argumentów w roznej kolejności