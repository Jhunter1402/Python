def my_function(*args):
    for i in args:
        print(i)


my_function(*(1, 3, 4, 5, 6, 6,))
