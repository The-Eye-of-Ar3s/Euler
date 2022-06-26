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


print(solve002())