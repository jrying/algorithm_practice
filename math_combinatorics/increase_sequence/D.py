# Source: http://codeforces.com/contest/466/problem/D

N, H = map(int, raw_input().split(" "))
A = map(int, raw_input().split(" "))

def f(a):
    for i in range((len(a)+1)/2):
        if H - a[i] > i + 1:
            return 0
        elif H - a[len(a)-i-1] > i + 1:
            return 0
    starts = []
    a = [H]+a+[H]
    rr = 1
    r = 1
    d = 1
    for i in range(1, len(a)):
        if abs(a[i] - a[i-1]) > 1:
            return 0
        if a[i] < H:
            if a[i] == a[i-1]:
                # print i, (1 + H - a[i])
                r *= (1 + H - a[i])
                r %= 1000000007
            if a[i] > a[i-1]:
                d *= (1 + H - a[i])
                d %= 1000000007
    return (r*d)%1000000007
print f(A)
