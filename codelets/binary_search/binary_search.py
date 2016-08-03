#  m
# [1]
#  m
# [1,2]
#    m
# [1,2,3]
#    m
# [1,2,3,4]

# -1: go left, 0: match, 1: go right
def test(x):
    return x

# [l, r)
def bs(arr):
    l, r = 0, len(arr)
    while l < r - 1:
        m = (l + r) / 2
        if test(arr[m]) < 0: r = m
        else: l = m
    return l

def right_most_bs(arr):
    l, r = 0, len(arr)
    while l < r - 1:
        m = (l + r) / 2
        if test(arr[m]): r = m
        else: l = m
    return l
