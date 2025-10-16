x = input("Please create the password: ")
y = list(x)
if y[0].isdigit():
    print("Password can't start with digit")
for i in y:
    if i.isupper():
        print("Password can't start with uppercase")

