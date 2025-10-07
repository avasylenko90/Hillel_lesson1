print("Hello dude, we are doing the task from the lesson 2")
print("Could you please enter any number which consists of 4 digits from 0 to 9")
answer = int(input())
x = answer//1000
y = (answer//100)%10
z = (answer//10)%10
w = answer%10
print(x)
print(y)
print(z)
print(w)

print("Great job! And now lets do the same but using another operator")
print("Could you please enter any number which consists of 4 digits from 0 to 9")
answer = int(input())
print(divmod(answer,1000)[0])
print(divmod(answer, 100)[0] %10)
print(divmod(answer, 10)[0]%10)
print(divmod(answer,10)[1])



