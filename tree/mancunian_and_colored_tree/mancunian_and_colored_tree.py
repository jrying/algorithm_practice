# Source: https://www.hackerearth.com/august-easy-16/algorithm/mancunian-and-colored-tree/
# TODO: TLE

'''
# Read input from stdin and provide input before running code

name = raw_input('What is your name?\n')
print 'Hi, %s.' % name
'''
N, C = map(int, raw_input().split())
Ps = map(lambda x: int(x)-1, raw_input().split())
Cs = map(lambda x: int(x)-1, raw_input().split())

t = [[]]*N
t[0] = [-2]*C
r = ["-1"]
for i in xrange(1, N):
    x = t[Ps[i-1]][:]
    x[Cs[Ps[i-1]]] = Ps[i-1]
    t[i] = x
    r.append(str(x[Cs[i]]+1))
print " ".join(r)
