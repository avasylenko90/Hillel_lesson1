lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
new_lst = []
for i in lst:
    if i != 0:
        new_lst.append(i)
for i in lst:
    if i ==0:
        new_lst.append(0)

print(new_lst)

print("And lets do the same in another way")
lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
new_lst = []

for i in range(len(lst)):
    if lst[i] != 0:
        new_lst.append(lst[i])

for i in range(len(lst)):
    if lst[i] == 0:
        new_lst.append(lst[i])

print(new_lst)

print("And lets do the same in another way")
lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

i = 0
length = len(lst)

while i < length:
    if lst[i] == 0:
        lst.pop(i)
        lst.append(0)
        length -= 1
    else:
        i += 1

print(lst)