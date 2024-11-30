import random
n = 10  numbers = [random.randint(1, 100) for _ in range(n)]
print("Изначальный список:", numbers)
shift= [numbers[-1]] + numbers[:-1]
print("Список после циклического сдвига:", shift)
