N = input()
A = map(int, raw_input().split(" "))
parentof = {}
selfs = []
visits = [False] * (N+1)
leaves = set(range(1, N+1))

for i in range(1, N+1):
    parentof[i] = A[i-1]
    if parentof[i] == i:
        selfs.append(i)
        visits[i] = True
    leaves.discard(A[i-1])

cuts = []

def visit(r):
    visited = set()
    while visits[r] == 0:
        # print r, visited, unvisited
        visits[r] = 1
        visited.add(r)
        if parentof[r] in visited:
            cuts.append(r)
            break
        r = parentof[r]

for leaf in leaves:
    visit(leaf)

for i in range(1, N+1):
    if not visits[i]:
        visit(i)


if len(selfs):
    selfp = selfs[0]
    cuts += selfs[1:]
elif len(cuts):
    selfp = cuts[0]
for cut in cuts:
    A[cut-1] = selfp

# print cuts
print len(cuts)
print " ".join(map(str, A))
