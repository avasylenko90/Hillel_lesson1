def fruitset(**kwargs):
    for fruit, price in kwargs.items():
        print(f"{fruit} costs {price}")

fruitset(aplles=10, banana=20, cherry=40, orange=50)