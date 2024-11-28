# Домашнее задание по теме "Режимы открытия файлов"

from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        products_str = file.read()
        file.close()
        return products_str

    def add(self, *products: Product):
        file = open(self.__file_name, 'r')
        products_list = self.get_products()
        for item in products:
            if not isinstance(item, Product):
                break
            elif item.name in products_list:
                print(f'Продукт {item.name} уже есть в магазине')
                continue
            else:
                file = open(self.__file_name, 'a')
                file.write(f"{str(item)}\n")
        file.close()

# file = open('products.txt', 'w')
# file.close()

s1 = Shop()
p1 = Product('Potato', 50.0, 'Vagetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Tomato', 5.5, 'Vegetables')
print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())

