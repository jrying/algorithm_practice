def kmp(s, w):
    # Prepare table
    t = [-1] * len(w)
    j = 0
    for i in range(1, len(w)):
        if w[i] == w[j]:
            t[i] = j
            j += 1
        else:
            if j > 0:
                # sequence stopped
                t[i] = j
                j = 0
            else:
                # not matched
                t[i] = 0
    # print t
    i = 0
    m = 0
    while m < len(s) - len(w) + 1:
        if s[m + i] == w[i]:
            # matched
            if i == len(w) - 1:
                return m
            else:
                i += 1
        else:
            # not matched
            m = m + i - t[i]
            i = 0
    return -1

print "answer: ", "ABC ABCDAB ABCDABCDABDE".index("ABCDABD")
print kmp("ABC ABCDAB ABCDABCDABDE", "ABCDABD")
print "answer: ", "ABC ABCDAB ABCDABCDABDE".index("ABDE")
print kmp("ABC ABCDAB ABCDABCDABDE", "ABDE")
