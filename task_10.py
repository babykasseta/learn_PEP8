import time

def timer(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f"Function {function.__name__} took {end - start: .4f} seconds")
        return result
    return wrapper

@timer
def heavy_computation(num):
    return sum(num ** 2 for num in range(num))

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
filtered = list(filter(lambda x: x > 10, squared))