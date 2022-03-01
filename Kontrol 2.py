# #№1
# list = [30, 'Hello', 30, 'n', 2.45]
# list_1 = []
# for i in list:
#     if list.count(i) == 1:
#         list_1.append(i)
# print(list_1)
#
# # №2
# list = [12, 22, 68, 124, 22, 68, 97]
# counter = 0
# for i in range(len(list)):
#     for j in range(i + 1, len(list)):
#         if list[i] == list[j]:
#             counter += 1
# print(counter)
#
# # №3
# C_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
# C_2 = (45, 21, 124, 76, 5, 23, 91, 234)
# sum_1 = sum(C_1)
# sum_2 = sum(C_2)
# if sum_1 > sum_2:
#     print("Сумма больше в кортеже - С_1")
# else:
#     print("Сумма больше в кортеже - С_2")
#
# max_C_1 = max(C_1)
# max_C_2 = max(C_2)
# mini_C1 = min(C_1)
# mini_C2 = min(C_2)
# print(f"C_1 max index {C_1.index(max_C_1)} , min index {C_1.index(mini_C1)}")
# print(f"C_2 max index {C_2.index(max_C_2)} , min index {C_2.index(mini_C2)}")
#
# # №4
#
# str = ' An apple a day keeps the doctor away'
# my_dict = {}
# for letter in str:
#     my_dict[letter] = my_dict.get(letter, 0) + 1
# print(my_dict)

# # №6
#
# a = [1,3,6,8,6]
# b = [2,4,6,8,6]
#
# print(len(set(a) & set(b)))