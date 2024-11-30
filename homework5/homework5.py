import random


n = 10  
numbers = [random.randint(1, 100) for _ in range(n)]

print("Список чисел:", numbers)
result = [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i - 1]]

print("Элементы, которые больше предыдущего:", result)
