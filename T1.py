import random

random_numbers = [random.randint(30, 90) for _ in range(20)]

result_numbers = [num for num in random_numbers]

print(result_numbers)
