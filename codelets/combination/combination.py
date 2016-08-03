from fractions import Fraction
import itertools

# With MOD
MOD = 10**9+7
def ncomb(n, r):
    return reduce(lambda a, b: (a*b)%MOD, (Fraction(n-i, i+1) for i in range(r)), 1)

# No MOD
def ncomb(n, r):
    return reduce(lambda a, b: (a*b), (Fraction(n-i, i+1) for i in range(r)), 1)

def comb(a, l):
    return [subset for subset in itertools.combinations(a, l)]

def comball(a):
    r = []
    for l in range(0, len(a)+1):
        r.extend(comb(a, l))
    return r
