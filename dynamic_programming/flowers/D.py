# Source: http://codeforces.com/problemset/problem/474/D

from fractions import Fraction
MAX = 100000
MOD = 10**9+7

T, K = map(int, raw_input().split(" "))
arr = []
for _ in range(T):
    a, b = map(int, raw_input().split(" "))
    arr.append((a-1, b-1))

r = [1]*K
s = range(1, K+1)[:]
for l in range(K, MAX+1):
    # TODO only keep last k
    x = r[-1] + r[-K]
    r.append(x % MOD)
    s.append((x + s[-1]) % MOD)

# TODO Mo's
for (a, b) in arr:
    print (s[b+1] - s[a]) % MOD
