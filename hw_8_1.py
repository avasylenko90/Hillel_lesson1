def add_one(some_digits):
     list = []
     interim = int(some_digits)
     list.append(interim)
     new_digit = (list[0] + 1)
     final_list = [int(x) for x in str(new_digit)]
     print(final_list)


some_digits = input("please enter any number of random digits:")
add_one(some_digits)
