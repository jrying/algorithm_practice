# Non-binary Tree
N = 100
result = []
result.append(str(N))
result.append(" ".join(map(str, range(1, N+1))))
for i in range(2, N+1):
    result.append(str(i) +" " + str((N*N)%(i-1)+1))

print "\n".join(result)
