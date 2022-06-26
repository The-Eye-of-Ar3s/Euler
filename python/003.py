def solve003():
    N = 600851475143
    p = 2
    m = 0
    while N >= p*p:
        if N%p == 0:
            m = p
            N = N/p
        else:
            p=p+1
    return N

print(solve003())