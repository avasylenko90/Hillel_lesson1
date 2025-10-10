my_list = [1,2,3,4,5,6,7,8,9]
if len(my_list)>1:
    a = my_list.pop(-1)
    my_list.insert(0,a)
    print(my_list)
else:
    print(my_list)

