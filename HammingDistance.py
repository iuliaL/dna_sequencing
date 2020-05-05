def HammingDistance(p, q):
    mismatches = 0
    for i in range(len(p)):
        if not (p[i] == q[i]):
            mismatches +=  1
    return mismatches 