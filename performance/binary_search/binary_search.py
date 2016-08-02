def test(x):
    return x

def right_most_bs(arr):
    l, r = 0, len(arr)
    while l < r - 1:
        m = (l + r) / 2
        if test(arr[m]): r = m
        else: l = m
    return l
