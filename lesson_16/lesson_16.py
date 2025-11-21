class Goods:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Goods [name = {self.name}, price = {self.price}]"


class Basket:
    """ У цій реалізації не можна пройти по елементам Кошика в циклі """

    def __init__(self, user):
        self.user = user
        self.goods_list = list()

    def add_good(self, good):
        self.goods_list.append(good)

    def __str__(self):
        result = f"User: {self.user}\n"
        for good in self.goods_list:
            result += str(good) + "\n"
        return result


basket = Basket("Alexander_Ts")

a = Goods("Apple", 35)
b = Goods("Milk", 50)

basket.add_good(a)
basket.add_good(b)
# Побачимо, що в кошику є товар
print(basket)
# User: Alexander_Ts
# Goods [name = Apple, price = 35]
# Goods [name = Milk, price = 50]

# Спроба передати об'єкт кошика в цикл, спричинить помилку
# TypeError: 'Basket' object is not iterable
for good in basket:
    print(good)