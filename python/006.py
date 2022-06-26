def solve006():
    return sum(range(101))**2 - sum([i**2 for i in range(101)])

print(solve006())