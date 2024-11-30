import re

# Функция для разбора email
def pochtafinder(email):
    # Регулярное выражение для разбора email
    pattern = r'^([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$'
    match = re.match(pattern, email)
    if match:
        username, domain = match.groups()
        return username, domain
    else:
        return None, None

# Основная программа
print("Добро пожаловать в приложение для разбора email!")
email = input("Введите ваш email: ")

username, domain = pochtafinder(email)

if username and domain:
    print(f"Username: {username}")
    print(f"Domain: {domain}")
else:
    print("Введён некорректный email. Пожалуйста, попробуйте снова.")
