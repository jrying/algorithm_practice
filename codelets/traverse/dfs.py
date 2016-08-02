def dfs(graph, start):
    visited, tovisit = set(), [start]
    seq = []
    while tovisit:
        v = tovisit.pop()
        seq.append(v)
        if v not in visited:
            visited.add(v)
            tovisit.extend(graph[v] - visited)
    return seq

def preorder(graph, start):
    return dfs(graph, start)

def postorder(graph, start):
    visited, tovisit = set(), [start]
    seq = []
    while tovisit:
        v = tovisit[-1]
        if v not in visited:
            visited.add(v)
            tovisit.extend(graph[v] - visited)
        else:
            tovisit.pop()
            seq.append(v)
    return seq


# Binary tree
# TODO
def inorder(graph, start):
    visited, tovisit = set(), [start]
    seq = []
    while tovisit:
        v = tovisit.pop()
        seq.append(v)
        if v not in visited:
            visited.add(v)
            tovisit.extend(graph[v] - visited)
    return seq
