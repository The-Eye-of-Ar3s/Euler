def solve005():
    factors = [factorize(i) for i in range(1,21)]
    newfactors = {}
    for i in range(20):
        newfactors[str(i+1)] = 0
    for i in factors:
        for j in i:
            if newfactors[str(j)] < i.count(j):
                newfactors[str(j)] = i.count(j)
    cstr = ""
    for key in newfactors.keys():
        cstr += f"{int(key)}*"*newfactors[key]
    cstr = cstr[:-1]
    return(eval(cstr))
            

def factorize(n):
    r = []
    p = 2
    while n >= p**2:
        if n%p == 0:
            r.append(p)
            n//=p
        else:
            p+=1
    r.append(n)
    return r

print(solve005())