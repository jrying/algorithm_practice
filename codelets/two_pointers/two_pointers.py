nr = [-1]*MAX_N

def cs(a,b):
    if a[1] > b[1]: return 1
    elif a[1] < b[1]: return -1
    if a[0] > b[0]: return 1
    else: return -1

sq = sorted(qs, cs)
def memorise(n):
    if nr[n] == -1:
        nr[n] = pf(n)
    return nr[n]

result = {}
currentL = currentR = 0
count = 0
for l, r in sq:
    while currentL < l:
        count -= memorise(currentL)
        currentL += 1
    while currentL > l:
        count += memorise(currentL-1)
        currentL -= 1
    while currentR > r + 1:
        count -= memorise(currentR)
        currentR -= 1
    while currentR < r + 1:
        count += memorise(currentR)
        currentR += 1
    # print l, r, count, currentL, currentR
    result[(l,r)] = count

for q in qs:
    print result[q]
