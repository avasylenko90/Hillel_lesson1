print("Please one by one enter integers and math action identifying what to do with them: ")
a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = input("enter arithmetic operator (+, -, *, /): ")
if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    if b != 0:
        print(a/b)
    else:
        print("❌ Error: division by zero!")

print("Please one by one enter floating digits and math action identifying what to do with them: ")
a = float(input("enter first number: "))
b = float(input("enter second number: "))
c = input("enter arithmetic operator (+, -, *, /): ")
if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    if b != 0:
        print(a/b)
    else:
        print("❌ Error: division by zero!")
print ("the end")