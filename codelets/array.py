# Check neighbours
def check(c):
    return c == "."

neighbour = "n"
not_neighbour = "."
for i in xrange(R):
    a2.append(a[i][:])
    for j in xrange(C):
        if check(a[i][j]): a2[i][j] = neighbour
        elif i > 0 and check(a[i-1][j]): a2[i][j] = neighbour
        elif j > 0 and check(a[i][j-1]): a2[i][j] = neighbour
        elif i < R-1 and check(a[i+1][j]): a2[i][j] = neighbour
        elif j < C-1 and check(a[i][j+1]): a2[i][j] = neighbour
        else: a2[i][j] = not_neighbour
    a = a2
