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

def f(a, s):
    j = 0
    result = 0
    repetive = 0
    s = s + "."
    used = set()
    for i in xrange(len(a)):
        if j > 0 and s[j] == s[j-1]:
            repetive += 1
        if a[i] == s[j]:
            j += 1
            used = set()
        else:
            if j > 0 and s[j-1] == a[i]:
                result += repetive + 1
            elif a[i] not in used:
                result += 1
                used.add(a[i])
            repetive = 0

    return result

a = raw_input()
b = raw_input()
s = lcs(a, b)
"""
start/end: 1
middle: repetive + 1
"""

result = f(b,s)
print result
