import random
ticket = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]
def ioop():
    print("Выберите по одному числу из каждой строки:")
    usern = []
    for i, row in enumerate(ticket):
        print(f"Строка {i + 1}: {row}")
        while True:
            try:
                num = int(input(f"Введите число из строки {i + 1}: "))
                if num in row and num not in usern:
                    usern.append(num)
                    break
                else:
                    print("Число не из строки или уже выбрано. Попробуйте снова.")
            except ValueError:
                print("Пожалуйста, введите корректное число.")
    return usern

def random_choice():
    return [random.choice(row) for row in ticket]

print("Добро пожаловать в лотерею!")
usern = ioop()
randnum = random_choice()
matches = set(usern) & set(randnum)
print("\nВаш выбор:", usern)
print("Случайный выбор:", randnum)
print(f"Совпавшие числа: {list(matches)} (всего {len(matches)})")
