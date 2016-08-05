MAX = 10**9
n, w, v, u = map(float, raw_input().split(" "))
vs = []
for i in xrange(int(n)):
    vv = map(int, raw_input().split(" "))
    vs.append(vv)
# u, v >= 1
a = u/v
# Try pass before bus come
def canpass():
    for x in vs:
        if x[1] > x[0]*a: return False
    return True

if canpass():
    print w/u
else:
    # TODO: y = ax-b
    maxb = -MAX*10
    for x in vs:
        maxb = max(maxb, (a*x[0]-x[1]))
    print (w+max(maxb, 0))/u
