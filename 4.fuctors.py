from pymonad.tools import curry, List
from pymonad.maybe import Just

@curry
def add(x, y):
    return x + y

add10 = add * Just(10)

#print(add10 & Just(3))
#print(add10 & List(1, 2, 3))