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

print("And now lets do the second task from the lesson 2")
print("Could you please enter any positive number which consists of 5 digits from 0 to 9")
answer = int(input())
z = divmod(answer,10)[1]
y = divmod(answer, 10)[0]%10
x = divmod(answer,100)[0]%10
w = divmod(answer,1000)[0]%10
v= divmod(answer,10000)[0]%10
print(z,y,x,w,v,sep="")

print("Great job! And now lets do the same but using another operator")
print("Could you please enter any positive number which consists of 5 digits from 0 to 9")
answer = int(input())
z = answer % 10
y = (answer//10)%10
x = (answer//100)%10
w = (answer//1000)%10
v = (answer//10000)%10
print(z,y,x,w,v,sep="")
