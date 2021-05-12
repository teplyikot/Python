# Task 1
list1 = [2, 25.3, 25+39j, 'test', True, {4, 45.4, 'twelve'}, {1: 24, 2: 'str', 3: True}]
for a in list1:
    print(type(a))

#Task 3 var 1
month1 = int(input("Введите номер месяца: "))
seasons = ['Зима', 'Весна', 'Лето', 'Осень']
if 3<=month1<=5:
    print("Время года: ", seasons[1])
elif 6<=month1<=8:
    print("Время года: ", seasons[2])
elif 9<=month1<=11:
    print("Время года: ", seasons[3])
else:
    print("Время года: ", seasons[0])

#Task 3 var 2
month1 = int(input("Введите номер месяца: "))
seasons = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
if 3<=month1<=5:
    print("Время года: ", seasons.get(2))
elif 6<=month1<=8:
    print("Время года: ", seasons.get(3))
elif 9<=month1<=11:
    print("Время года: ", seasons.get(4))
else:
    print("Время года: ", seasons.get(1))

#Task 4
stroka = str(input("Введите строку: "))
spis = stroka.split(" ")
for a in spis:
    print(spis.index(a)+1, a[:10])

# Task 5
rating = [7, 5, 3, 3, 2]
rate = int(input("Введите новый элемент рейтинга: "))
a = 0
for b in rating:
    if rate <= b:
	a += 1
rating.insert(a, rate)
print(rating)	

