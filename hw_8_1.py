def add_one(random_list):
     list = []
     interim = int(random_list)
     list.append(interim)
     new_list = (list[0]+1)
     print(new_list)


random_list = input("please enter any number of random digits:")
add_one(random_list)
