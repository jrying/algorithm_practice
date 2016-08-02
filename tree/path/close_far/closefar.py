
# TODO: TLE
MAXX = 10**9+1
N = input()
nodes = map(int, raw_input().split(" "))
edges = [set() for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, raw_input().split(" "))
    edges[a-1].add(b-1)
    edges[b-1].add(a-1)
path = [[] for _ in range(N)]
path[0] = [0]
visited, tovisit = set(), [0]
while tovisit:
    v = tovisit.pop()
    if v not in visited:
        visited.add(v)
        news = edges[v] - visited
        for a in news:
            path[a] = path[v] + [a]
        tovisit.extend(list(news))
# print path

Q = input()
for _ in range(Q):
    q, a, b = raw_input().split(" ")
    a, b = int(a)-1, int(b)-1
    l, r = 0, min(len(path[a]), len(path[b]))
    while l < r - 1:
        m = (l + r) / 2
        if path[a][m] != path[b][m]: r = m
        else: l = m
    s = path[a][l:] + path[b][l+1:]
    # print s
    if q == "C":
        s = sorted(map(lambda i: nodes[i], s))
        d = s[-1] - s[0]
        for i in range(len(s)-1):
            d = min(d, s[i+1]-s[i])
        print d
    else:
        M = 0
        m = MAXX
        for i in range(len(s)):
            M = max(M, nodes[s[i]])
            m = min(m, nodes[s[i]])
        print M - m
    # print M[(s, l)] - m[(s, l)]

"""10
1 2 7 4 5 3 9 10 6 8
1 2
2 3
2 4
2 5
5 6
2 7
3 8
3 9
9 10
10
C 5 1
F 1 5
C 2 4
C 1 2
F 1 3
F 3 4
F 2 4
C 4 5
C 1 6
C 1 6
1
4.
2
1
6.
5.
2.
1
time for i in {1..10}; do cat CLOSEFAR.txt  | python CLOSEFAR3.py ; done
"""
