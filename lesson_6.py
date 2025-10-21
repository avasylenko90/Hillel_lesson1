import random
import string

user_input = input("Enter password length: ")
input_int = int(user_input)

new_str = string.ascii_letters + string.digits + string.punctuation

password = ""
for _ in range(input_int):
    password += random.choice(new_str)

print(password)
