import string
user_input = input("Enter 2 letter via '-' : ")
split_input = user_input.split("-")
x = string.ascii_letters.index(split_input[0])
y = string.ascii_letters.index(split_input[1])
z = string.ascii_letters[x : y + 1]
print(z)