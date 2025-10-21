import string
user_input = input("Enter 2 letter via '-' : ")
user_input2 = user_input.split("-")
x = string.ascii_letters.index(user_input2[0])
y = string.ascii_letters.index(user_input2[1])
z = string.ascii_letters[x : y + 1]
print(z)