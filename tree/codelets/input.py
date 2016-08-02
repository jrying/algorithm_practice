N = input()
nodes = map(int, raw_input().split(" "))
edges = [set() for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, raw_input().split(" "))
    edges[a-1].add(b-1)
    edges[b-1].add(a-1)
