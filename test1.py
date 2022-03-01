# №5
torts = {"Наполеон" : [['мука', 'вода', 'яйцо'], 4.5, 100],
         "Mедовик" : [['мука', 'мед', 'яйцо'], 5.5, 100],
         "Грильяж" : [['мука', 'орехи', 'яйцо'], 5.9, 100]}
for key, value in torts.items():
    print('key','-', value[0])
    cont = 0
for key, value in torts.items():
    print('key','-', value[1])
    cont = 0
for key, value in torts.items():
    print('key', '-', value[2])
    cont = 0
for key, value in torts.items():
    print('key', '-', value[0], '-',  value[1], '-',  value[2])
    cont = 0

while True:
    tort = input("Наименование?(n - nothing)")
    if tort == 'n' or tort not in torts.keys():
        break
    qty = int(input("Количество?"))
    if qty > torts[tort][2]:
        print("Нет в наличии.")
        continue
    cost += torts[tort][1] * qty
    torts[tort][2]-= qty
    print("Price:", cost)
print("До свидания!")

for key, value in torts.items():
    print(key, '-', value[1], '-', value[2])
