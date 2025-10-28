def example_function(*args):
def example_function(*kwargs):
    for arg in args:
        print(arg)

# Виклик функції з різною кількістю позиційних аргументів
example_function(1, 2, 3, 4, 5)