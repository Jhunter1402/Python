def fibonacci(limit):
    a, b = 0, 1
    for i in range(0,limit):
        yield a
        a , b = b , a + b

l = int(input("Enter the limit for the Fibonacci sequence: "))
fib = fibonacci(l)
for i in fib:
    print(i)