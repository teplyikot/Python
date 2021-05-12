# Task 1
def del_func(del1, del2): 
	return del1 / del2
del1 = int(input("Введите делимое: "))
del2 = int(input("Введите делитель: "))
while del2 == 0:
    print("Не верно! На ноль делить нельзя!")
    del2 = int(input("Введите делитель: "))
else:
    print(del_func(del1, del2))

# Task 2
def usrdt_func(var1, var2, var3, var4, var5, var6):
    return var1 + var2 + var3 + var4 + var5 + var6
print(list(usrdt_func(input("Введите имя: "), input("Введите фамилию: "), input("Введите год рождения: "),
                     input("Введите город проживания: "), input("Введите email: "), input("Введите телефон: "))))

# Task 3
def sum_func(sum1, sum2, sum3):
sum1 = int(input("Введите первую число: "))
sum2 = int(input("Введите второе число: "))
sum3 = int(input("Введите третье число: "))

# Task 3
sum1 = int(input("Введите первую число: "))
sum2 = int(input("Введите второе число: "))
sum3 = int(input("Введите третье число: "))
def my_func(sum1, sum2, sum3):
    return sum1 + sum2, sum1 + sum3, sum2 + sum3
print(max(my_func(sum1, sum2, sum3)))

# Task 4
num1 = float(input("Введите положительное число для возведения в степень: "))
num2 = int(input("Введите степень (отрицательное число): "))
def my_func(num1, num2):
    return num1 ** num2
while num1 <= 0 or num2 >= 0:
    print("Один из аргументов неверен")
    num1 = float(input("Введите положительное число для возведения в степень: "))
    num2 = int(input("Введите степень (отрицательное число): "))
else:
    print(my_func(num1, num2))

# Task 6
def int_func(text):
    return text.title()
text = str(input("Введите слово: "))
if text.islower() == False:
    print("Слово должно быть из маленьких букв, введите повторно: ")
    text = str(input("Введите слово: "))
else:
    print(int_func(text))