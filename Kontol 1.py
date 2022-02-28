import random
num = input("Enter 7 digit number: ")
count = 0
sum_ = 0
for i in range(7):
    sum_ += int(num[i])
    if int(num[i]) % 2 == 0:
        count += 1
prod = int(num[0]) * int(num[2]) * int(num[5])

if count > 3:
    print(sum_)
else:
    print(prod)
print("____________________________________\n")

import random

n = int(input("Введите число: "))
numbers = [n // 1000000, (n // 100000) % 10, (n // 10000) % 10, (n // 1000) % 10, (n // 100) % 10, (n // 10) % 10,
           n % 10]
chet = 0
nechet = 0

for number in numbers:
    if number % 2 == 0:
        chet += 1
    else:
        nechet += 1

if chet > nechet:
    print(sum(numbers))
else:
    print(numbers[0] * numbers[2] * numbers[5])
