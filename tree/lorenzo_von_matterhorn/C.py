# N, M = map(int, raw_input().split(" "))
# A = map(int, raw_input().split(" "))
# S = raw_input()
# arr = []
nodes = {}
N = input()

for _ in range(N):
    s = raw_input()
    if s[0] == "1":
        t, a, b, x = map(int, s.split(" "))
        a, b = max(a, b), min(a, b)
        while a != b:
            if a in nodes:
                nodes[a] += x
            else:
                nodes[a] = x
            a, b = max(a/2, b), min(a/2, b)
        # print nodes
    else:
        t, a, b = map(int, s.split(" "))
        a, b = max(a, b), min(a, b)
        s = 0
        while a != b:
            if a in nodes:
                s += nodes[a]
            a, b = max(a/2, b), min(a/2, b)
        print s
