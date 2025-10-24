import math

my_str = input("Please enter any integer")
my_int = [int(x) for x in my_str]
mult_result = math.prod(my_int)

while mult_result > 9:
    my_new_int = [int(x) for x in str(mult_result)]
    mult_result = math.prod(my_new_int)
print(mult_result)