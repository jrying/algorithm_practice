N = input()
A = map(int, raw_input().split(" "))
con = [0]*N
gym = [0]*N
for i in range(N):
    if i == 0:
        gym[i] = 1
        con[i] = 1
        if A[i] / 2 == 1: gym[i] = 0
        if A[i] % 2 == 1: con[i] = 0
    else:
        if A[i] / 2 == 1:
            gym[i] = con[i-1]
        else:
            gym[i] = min(gym[i-1], con[i-1])+1
        if A[i] % 2 == 1:
            con[i] = gym[i-1]
        else:
            con[i] = min(gym[i-1], con[i-1])+1

print min(gym[-1], con[-1])
