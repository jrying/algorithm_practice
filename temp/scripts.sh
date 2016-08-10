# Prepare
touch {1..10}.py
touch {1..10}{0..9}.txt
touch {1..5}.txt

# Test
cat 1.txt | python 1.py
cat 2.txt | python 2.py
cat 3.txt | python 3.py
cat 4.txt | python 4.py

# C/P
N = input()
 = map(int, raw_input().split(" "))
 = map(int, raw_input().split(" "))
 = map(int, raw_input().split(" "))



print "\n".join(map(lambda x: str(int(random()*2**20)), range(1000)))
print " ".join(map(lambda x: str(int(random()*2**20)), range(1000)))

N = 3000
result = []
# result.append(" ".join(map(str, range(1, N+1))))
for i in range(2, 30000+1):
    result.append(str(i%N+1) +" " + str((N*N)%(i-1)%N+1))

print "\n".join(result)
