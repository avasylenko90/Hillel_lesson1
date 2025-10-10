my_lst=[]
if len(my_lst)==0:
    new_list = [[], []]

elif len(my_lst)%2==0:
    middle = len(my_lst)//2
    left_part = my_lst[:middle]
    right_part = my_lst[middle:]
    new_list = [left_part, right_part]
else:
    middle = (len(my_lst)+1)//2
    left_part = my_lst[:(middle)]
    right_part = my_lst[(middle):]
    new_list=[left_part]+[right_part]

print(new_list)