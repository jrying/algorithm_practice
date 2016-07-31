from fractions import gcd, Fraction
MOD = 10**9+7

def comb(n, r):
    return reduce(lambda a, b: (a*b)%MOD, (Fraction(n-i, i+1) for i in range(r)), 1)

def f():
    n, k, l = map(int, raw_input().split(" "))
    a = map(int, raw_input().split(" "))
    need = set()
    for i in range(0, n-1):
        for j in range(1, n):
            g = gcd(a[i], a[j])
            if g > l: return 0
            if g not in a: need.add(g)
    if len(need) > k: return 0
    possible = [False] * (l + 1)
    for i in range(1, (l + 1)):


    return comb(len(need|set(filter(lambda x: x <= l, a))|set([1])), k-len(need))

t = input()
for _ in range(t):
    print f()%MOD



"""Test
6
2 1 2
2 1
3 1 6
1 4 6
2 1 1
2 1
1 1 10
5
1 10 10
1
2 2 100
4 6

2
1
1
2
10
51
"""
