def dfs(graph, start):
    visited, tovisit = set(), [start]
    while tovisit:
        v = tovisit.pop()
        if v not in visited:
            visited.add(v)
            tovisit.extend(graph[v] - visited)
    return visited
