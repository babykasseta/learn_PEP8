numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = [num ** 2 for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]

def generate_data(num):
    return [num ** 2 for num in range(num) if num > 0]

data = generate_data(100)
filtered = [num for num in data if num % 10 == 0]