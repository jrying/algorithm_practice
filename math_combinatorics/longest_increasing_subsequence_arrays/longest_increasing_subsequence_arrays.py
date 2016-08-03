# Source: https://www.hackerrank.com/contests/world-codesprint-5/challenges/longest-increasing-subsequence-arrays
# TODO: TLE

# Enter your code here. Read input from STDIN. Print output to STDOUT
from fractions import Fraction
MOD = 10**9+7
P = input()

def com(n, k):
    k = min(n-k, k)
    r = reduce(lambda a, b: a*b, (Fraction(n-i, i+1) for i in range(k)), 1) % MOD
    return r
for _ in xrange(P):
    result = 0
    m, n = map(int, raw_input().split())
    bad = 1
    comb = 1
    # n: correct, i: bad, m: len
    for i in xrange(m-n+1):
        result += (n**(m-n-i)%MOD)*bad*comb%MOD
        comb = comb*(n+i)/(i+1)%MOD
        bad = bad*(n-1)%MOD
#        print (n**(m-n-i)),((n-1)**i),com(n+i-1, n-1)
    print result%MOD
