# Source: https://www.hackerearth.com/problem/algorithm/mancunian-and-naughty-numbers-1/
# AC

'''
# Read input from stdin and provide input before running code

name = raw_input('What is your name?\n')
print 'Hi, %s.' % name
'''
prime = [2,3]
for i in range(5, 100001):
    si = i**0.5
    for x in prime:
        if i % x == 0: break
        elif x > si:
            prime.append(i)
            break

def pf(n):
    count = 0
    l = len(str(n))
    for x in prime:
        if n % x == 0:
            count += 1
            while n % x == 0: n /= x
        if x > n: break
    return l == count

nr = [0, 1]+[-1]*100000
# for i in range(2, 100001):
#     nr.append(pf(i))

Q = input()
qs = []
for _ in range(Q):
    l, r = map(int, raw_input().split())
    # print nr[l:r+1]
    # print len(filter(lambda x: x, nr[l:r+1]))
    qs.append((l, r))

def cs(a,b):
    if a[1] > b[1]: return 1
    elif a[1] < b[1]: return -1
    if a[0] > b[0]: return 1
    else: return -1
sq = sorted(qs, cs)
print qs, sq
def f(n):
    if nr[n] == -1:
        nr[n] = pf(n)
    return nr[n]

result = {}
currentL = currentR = 0
count = 0
for l, r in sq:
    while currentL < l:
        count -= f(currentL)
        currentL += 1
    while currentL > l:
        count += f(currentL-1)
        currentL -= 1
    while currentR > r + 1:
        count -= f(currentR)
        currentR -= 1
    while currentR < r + 1:
        count += f(currentR)
        currentR += 1
    print l, r, count, currentL, currentR
    result[(l,r)] = count

for q in qs:
    print result[q]
