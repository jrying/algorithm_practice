# Enter your code here. Read input from STDIN. Print output to STDOUT
def lcs(a, b):
    t = [[0]*(len(b)+1) for _ in xrange(len(a)+1)]
    r = [[""]*(len(b)+1) for _ in xrange(len(a)+1)]
    for i in xrange(1, len(a)+1):
        for j in xrange(1, len(b)+1):
            if a[i-1] == b[j-1]:
                t[i][j] = t[i-1][j-1] + 1
                r[i][j] = r[i-1][j-1] + a[i-1]
            else:
                if t[i][j-1] > t[i-1][j]:
                    t[i][j] = t[i][j-1]
                    r[i][j] = r[i][j-1]
                elif t[i-1][j] > t[i][j-1]:
                    t[i][j] = t[i-1][j]
                    r[i][j] = r[i-1][j]
                else:
                    r[i][j] = min(r[i-1][j], r[i][j-1])
    return r[-1][-1]

def sed(a, b):
    t = [[0] * (len(b)+1) for _ in range(len(a)+1)]
    # Insert all
    for i in range(len(a)+1):
        t[i][0] = i
    for j in range(len(b)+1):
        t[0][j] = j
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            t[i][j] = min(t[i-1][j], t[i][j-1])
            if a[i-1] != b[j-1]:
                t[i][j] += 1
    return t[len(a)][len(b)]


a = raw_input()
b = raw_input()
s = lcs(a, b)
result = sed(b,s)
print result
