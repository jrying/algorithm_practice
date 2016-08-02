def bfs(graph, start):
    visited, tovisit = set(), [start]
    seq = []
    while tovisit:
        v = tovisit.pop(0)
        seq.append(v)
        if v not in visited:
            visited.add(v)
            tovisit.extend(graph[v] - visited)
    return seq
