# Source: http://codeforces.com/contest/466/problem/C
N = input()
A = map(int, raw_input().split(" "))
S =  A[0]
ss = [A[0]]
for a in A[1:]:
    ss.append(a + ss[-1])
    S += a
if S % 3 != 0: print 0
else:
    t = S / 3
    first = []
    result = 0
    for i in range(N-1):
        if ss[i] == t*2:
            result += len(first)
        if ss[i] == t:
            first.append(i)
    print result
