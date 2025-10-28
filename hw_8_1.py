def add_one(random_list):
    return random_list

random_list = input("please enter any number of random digits:")
random_list = [int(x) for x in random_list]
result = add_one(random_list)
