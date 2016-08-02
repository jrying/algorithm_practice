# Source: https://www.hackerearth.com/problem/algorithm/mancunian-and-multiplicative-queries-1/
# TODO: TLE, Mos

'''
# Read input from stdin and provide input before running code

name = raw_input('What is your name?\n')
print 'Hi, %s.' % name
'''
N, C, Q = map(int, raw_input().split())
A = map(int, raw_input().split())
F = map(int, raw_input().split())

t = [[0]*(N+1)]
for a in A:
    x = t[-1][:]
    x[a] += 1
    t.append(x)

# print t
product = 1
for _ in range(Q):
    l, r = map(int, raw_input().split())
    for i in range(1, N+1):
        product *= F[t[r][i] - t[l-1][i]]
print product
