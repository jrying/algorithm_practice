
def f():
    n, p, q = map(int, raw_input().split(" "))
    a = sorted(map(int, raw_input().split(" ")))
    count = 0
    for x in a:
        t = x
        if p + 2 * q >= x:
            if (x % 2 == 0 or p):
                mq = min(q, t/2)
                t -= mq * 2
                q -= mq
                p -= t
                count += 1
        else: break
    return count
t = input()
for _ in range(t):
    print f()

"""
6
3 3 0
1 2 2
3 2 1
1 2 1
4 5 4
2 3 4 5
4 2 2
1 2 3 4
4 2 2
1 1 2 2
4 2 2
1 2 3 4

2
3
3
3
4
3
"""
