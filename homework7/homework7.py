import random

# Генерация списка случайных чисел
n = 10  # Количество элементов в списке
numbers = [random.randint(1, 100) for _ in range(n)]

print("Изначальный список:", numbers)

# Циклический сдвиг элементов вправо
shift= [numbers[-1]] + numbers[:-1]

print("Список после циклического сдвига:", shift)
