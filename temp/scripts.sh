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
