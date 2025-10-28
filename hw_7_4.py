def common_elements():
    r1 = set(range(0, 100, 3))
    r2 = set(range(0, 100, 5))
    r3 = r1.intersection(r2)
    return r3

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

my_set = {1, 2, 3, 4}
my_frozen1 = frozenset(my_set)
print(my_frozen1)