# Задание №1
# Создайте словарь person, в котором будут присутствовать ключи name, age, city.
# Выведите значение возраста из словаря person.

person = {"Name": "Ina", "age": 39, "city": "Minsk"}
print(person['age'])

# Задание №2
# Значениями словаря могут быть и списки.
# Создайте словарь с ключами BMW, Tesla и списками из 3х моделей в качестве значений.
# Выведите первое и последнее значения каждого из ключей.

models_data = {"BMW":["Model_1", "Model_2", "Model_3"],"Tesla":["Model S", "Model A", "Model B"]}
print(models_data["BMW"][0], models_data["BMW"][2])
print(models_data["Tesla"][0], models_data["Tesla"][2])

# Задание №3
# Исправьте ошибки в коде, чтобы получить требуемый вывод. (Вывод True)
# d1 = {"a": 100. "b": 200. "c": 300}
# d2 = {a: 300. b: 200, d: 400}
# print(d1["b"] == d2["b"])
d1 = {"a": 100,"b": 200, "c": 300}
d2 = {"a": 300, "b": 200, "d": 400}
print(d1["b"] == d2["b"])

# Задание №4
#Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран.

my_dictionary = {'data1': 375, 'data2': 567, 'data3': 37, 'data4': 21}
result = 1
for key in my_dictionary:
    result = result * my_dictionary[key]
print(result)

#Задание №5
# Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом,
# чтобы элементы первого списка были ключами, а элементы второго — соответственно
# значениями нашего словаря.

keys = ["red", "green", "blue"]
values = ["#FF0001", "#000300", "#0000FF"]
color_dictionary = dict(zip(keys, values))
print(color_dictionary)

# Задание №6
# Создайте словарь из строки 'pythonist' следующим образом: в качестве ключей возьмите буквы строки,
# а значениями пусть будут числа, соответствующие количеству вхождений данной буквы в строку.
str1 = 'pythonist'
my_digt = {i: str1.count(i) for i in str1}
print(my_digt)

# Домашнее задание
# У вас есть словарь, где ключ – название продукта. Значение – список, который содержит цену и кол-во товара.
# Выведите через ‘’–’’ название – цену – количество.
# С клавиатуры вводите название товара и его кол-во. n – выход из программы. Посчитать цену выбранных товаров
# и сколько товаров осталось в изначальном списке.

product = {'coffee': ['quantity': 1, 'price': 30], 'tea': ['quantity': 1, 'price': 25],
          'water': ['quantity': 1, 'price': 10], 'juice': ['quantity': 1, 'price': 35],
          'soda': ['quantity': 1, 'price': 15]}
print(product"-")
for item in goods:
    item_name = item
    item_code = goods[item]
    item_quantity, item_total_amount = 0, 0

    for i in store[item_code]:
        item_quantity += i['quantity']
        item_total_amount += i['price'] * i['quantity']

    print(item_name, item_quantity, 'шт, стоимость', item_total_amount, 'руб')

