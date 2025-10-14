my_list = [1, 3, 5]
if my_list:
        new_list = my_list[::2]
        total = sum(new_list)
        final_list = total* my_list[-1]
        print(final_list)
else:
        print("0")


