import random

# Генерация списка случайных чисел
n = 10  # Количество элементов в списке
numbers = [random.randint(1, 100) for _ in range(n)]

print("Изначальный список:", numbers)

# Поиск минимального и максимального элемента и их индексов
min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))
min_value = numbers[min_index]
max_value = numbers[max_index]

# Замена местами минимального и максимального элемента
numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

print("Измененный список:", numbers)
print(f"Поменялись элементы: минимальный ({min_value}) и максимальный ({max_value})")
