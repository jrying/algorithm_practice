# Source: http://codeforces.com/contest/701/problem/A

N = input()
cards = map(int, raw_input().split(" "))
target = sum(cards)*2/N
d = {}

for i in range(0, 100):
    d[i+1] = []

for i in range(N):
    if len(d[target - cards[i]]) > 0:
        got = d[target - cards[i]].pop()
        print got+1, i+1
    else:
        d[cards[i]].append(i)
