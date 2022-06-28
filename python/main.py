import sys

def prime_factorize(n):
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


def solve001():
    return sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])


def solve002():
    fib = [1,2]
    while fib[-1] < 4000000:
        fib.append(fib[-1] + fib[-2])
    fib.pop()
    ret_sum = 0
    for i in fib:
        if i%2 == 0:
            ret_sum += i
    return ret_sum


def solve003():
    N = 600851475143
    return max(prime_factorize(N))


def solve005():
    factors = [prime_factorize(i) for i in range(1,21)]
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


def solve006():
    return sum(range(101))**2 - sum([i**2 for i in range(101)])


def solve016():
    return sum(int(i) for i in str(2**1000))


def main():
    p_map = {
        "1":  solve001,
        "2":  solve002,
        "3":  solve003,
        "5":  solve005,
        "6":  solve006,
        "16": solve016
        }
    if sys.argv[1] in p_map.keys():
        print(p_map[sys.argv[1]]())
    else:
        print("NA")


main()