x = input("Please create the name of variable: ")
y = list(x)
if y[0].isdigit():
    print("The name of variable can't start with the digit")
for i in y:
    if i.isupper():
        print("The name of variable can't contain uppercase letters")
        break
    if i in """!"#$%&'()*+,-./:;<=>?@[\]^`{|}~""":
        print("The name of variable can't contain punctuation")
        break
