def add(*args):
    total = 1
    for num in args:
        total += num
    return total


print("Sum: ", add(1, 5, 6, 24, 4, 5))
print("Sum: ", add(1, 2, 3))
