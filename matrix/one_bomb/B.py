# N = input()
N, M = map(int, raw_input().split(" "))
arr = []
rr = -1
cc = -1
r1 = set()
c1 = set()
points = []
flag = True
# for i in range(N): r1[i] = 0
# for j in range(M): c1[j] = 0
for i in range(N):
    line = raw_input()
    for j in range(M):
        if line[j] == "*":
            if i in r1 and i != rr:
                if rr == -1:
                    rr = i
                else:
                    flag = False
                    break
            if j in c1 and j != cc:
                if cc == -1:
                    cc = j
                else:
                    flag = False
                    break
            r1.add(i)
            c1.add(j)
            points.append((i, j))
# print points
for p in points:
    if p[0] != rr and p[1] != cc:
        if rr == -1:
            rr = p[0]
        elif cc == -1:
            cc = p[1]
        else:
            flag = False
if flag:
    rr, cc = max(0,rr), max(0,cc)
    print "YES"
    print rr+1, cc+1
else:
    print "NO"
