# N = input()
# N, M = map(int, raw_input().split(" "))
# A = map(int, raw_input().split(" "))
# arr = []
# for _ in range(N):
#     a, b = map(int, raw_input().split(" "))
#     arr.push((a, b))


S = raw_input()
a, b = S.split("e")
b = int(b)
if "." in a:
    a, d = a.split(".")
else:
    a = a
    d = "0"
new = a+d
point = len(a)+b
if len(new) < point:
    new = new + "0"*(point-len(new))
elif len(new) != point:
    new = new[:point]+"."+new[point:]
while new[0] == "0" and len(new) > 1 and new[1] != ".":
    new = new[1:]
if new[-2:] == ".0":
    new = new[:-2]
print new
