from fractions import Fraction
# With MOD
MOD = 10**9+7
def comb(n, r):
    return reduce(lambda a, b: (a*b)%MOD, (Fraction(n-i, i+1) for i in range(r)), 1)

# No MOD
def comb(n, r):
    return reduce(lambda a, b: (a*b), (Fraction(n-i, i+1) for i in range(r)), 1)
