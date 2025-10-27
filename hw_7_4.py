def common_elements():
    r1 = set(range(0, 100, 3))
    r2 = set(range(0, 100, 5))
    r3 = r1.intersection(r2)
    return r3

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
