import functools

def log_function_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}'")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def add(a, b):
    return a + b

sum = add(3, 4)
print(sum)