import random

n = 10  
numbers = [random.randint(1, 100) for _ in range(n)]

print("Изначальный список:", numbers)

min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))
min_value = numbers[min_index]
max_value = numbers[max_index]


numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

print("Измененный список:", numbers)
print(f"Поменялись элементы: минимальный ({min_value}) и максимальный ({max_value})")
