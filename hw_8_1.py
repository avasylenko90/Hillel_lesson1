def add_one(some_digits):
    new_digit = int("".join(str(x) for x in some_digits))
    updated_digit = new_digit.__add__(1)
    updated_list = [int(x) for x in str(updated_digit)]
    print(updated_list)


some_digits = [9]
add_one(some_digits)

