N, C = map(int, raw_input().split(" "))
bs = map(int, raw_input().split(" "))
cs = set(map(lambda x: int(x)-1, raw_input().split(" ")))

total = sum(bs)
r = 0
for c in cs:
    total -= bs[c]
    r += bs[c]*(total)

# print r
for i in range(N):
    if i not in cs and (i+1)%N not in cs:
        r += bs[i]*bs[(i+1)%N]
print r
