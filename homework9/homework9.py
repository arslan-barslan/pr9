import re
def pochtafinder(email):
    pattern = r'^([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$'
    match = re.match(pattern, email)
    if match:
        username, domain = match.groups()
        return username, domain
    else:
        return None, None

print("Добро пожаловать в приложение для разбора email!")
email = input("Введите ваш email: ")
username, domain = pochtafinder(email)
if username and domain:
    print(f"Username: {username}")
    print(f"Domain: {domain}")
else:
    print("Введён некорректный email. Пожалуйста, попробуйте снова.")
