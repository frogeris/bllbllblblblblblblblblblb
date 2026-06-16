

#pq tu regarde le code de cette merde frr 

from functools import reduce 
import itertools

class Swamp:
    def __new(cls): return super().__new__(cls)
    def get(self): return reduce(lambda a, b : a + b, itertools.chain ("Groak", "🐸"))

print((lambda f=Swamp(): f.get())())
