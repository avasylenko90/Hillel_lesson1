import keyword

x = input("Please create the name of variable: ")
y = list(x)
if y[0].isdigit():
    print("False. The name of variable can't start with the digit")
for i in y:
    if i.isupper():
        print("False. The name of variable can't contain uppercase letters")
        break
    if i in """!" " "#$%&'()*+,-./:;<=>?@[\]^`{|}~""":
        print("False. The name of variable can't contain punctuation but for _")
        break
for i in range(len(y) - 1):
    if y[i] == "_" and y[i + 1] == "_":
        print("False. The name of variable can't contain more than 1 _")
        break
if x in keyword.kwlist:
    print("False. The name of variable can't contain Python keywords")


import keyword
import string

x = input("Lets try now another way. Please create the name of variable: ")
y = list(x)
if y[0].isdigit():
    print("False. The name of variable can't start with the digit")
for i in y:
    if i.isupper():
        print("False. The name of variable can't contain uppercase letters")
        break
    if (i in string.punctuation and i != "_") or i == " ":
        print("False. The name of variable can't contain punctuation but for _")
        break
    if x in keyword.kwlist:
        print("False. The name of variable can't contain Python keywords")
        break
for i in range(len(y) - 1):
    if y[i] == "_" and y[i + 1] == "_":
        print("False. The name of variable can't contain more than 1 _")
        break
