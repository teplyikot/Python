# Task 1
first_name = input("Type your first name: ")
last_name = input("Type your last name: ")
age = int(input("Type your age: "))
weight = float(input("Type your weight: "))
print(f"Hello, {first_name} {last_name}. You are {age} year(s) old, and your weight is {weight} kg(s).")

# Task 2
time = int(input("Type time in seconds: "))
hours = (time // 3600) % 24
minutes = (time // 60) % 60
seconds = time % 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")

# Task 3
num = input("Type a number: ")
n1 = int(num)
n2 = int(num + num)
n3 = int(num + num + num)
print(n1 + n2 + n3)

# Task 4
n = int(input("Type a number: "))
last_char = n % 10
nummax = 0
while n > 0:
    if nummax < last_char:
        nummax = last_char
        n //= 10
        last_char = n % 10
    else:
        n //= 10
        last_char = n % 10
print(nummax)

# Task 5
vir = int(input("Укажите выручку, руб.: "))
izd = int(input("Укажите издержки, руб.: "))
prib = vir - izd
if prib > 0:
    print("Ваша рентабельность: ", prib)
    rent = prib / vir
    print("Ваша прибыль: ", rent)
    prib2 = int(input("Укажите число сотрудников: "))
    print("Прибыль на сотрудника: ", prib2)
else:
    print("Вы работаете в убыток: ", prib)

# Task 6
rez1 = int(input("Стартовый результат, км: "))
rez2 = int(input("Желаемый результат, км: "))
days = 1
while rez1 <= rez2:
    rez1 = rez1 * 1.1
    days +=1
print("Количество дней для достижения результата: ", days)