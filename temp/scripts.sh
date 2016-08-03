# Prepare
touch {1..4}.py
touch {1..4}.txt

# Test
cat 1.txt | 1.py
cat 2.txt | 2.py
cat 3.txt | 3.py
cat 4.txt | 4.py

# C/P
map(int, raw_input().split(" "))
