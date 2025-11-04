def find_unique_value(some_list):
    verification_list = [x for x in some_list if some_list.count(x) == 1]
    print("unique number ", verification_list)

some_list = [5, 5, 2, 2, 0.5, 0.5]
find_unique_value(some_list)