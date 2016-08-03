def rk(s, w):
    hashd = 103
    hw = 0
    for i in len(w):
        hw *= hashd
        hw += ord(w[i])

    
