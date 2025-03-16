import secrets
import string
#главная генерация 
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(secrets.choice(chars) for _ in range(length))
    
    return password

# Пример использования
print(generate_password(8943))
