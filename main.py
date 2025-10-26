import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special=True):

    characters = string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("Должен быть выбран хотя бы один тип символов")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Случайный пароль:", generate_password())
print("Пароль из 8 символов:", generate_password(8))
print("Простой пароль (только буквы):", generate_password(use_numbers=False, use_special=False))