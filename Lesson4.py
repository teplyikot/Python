# Task 1
from sys import argv

def salary():
	try:
		time, rate, bonus = map(float, argv[1:])
		print(f"Salary - {time * rate * bonus}")
	extept ValueError:
		print("Enter all 3 numbers. Not string or empty character.")

# Task 2
my_list = [15, 16, 2, 3, 1, 7, 5, 4, 10]
more_then = [my_list[num] for num in range (1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(more_then)

# Task 3

uniq_list = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
print(uniq_list)

# Task 4

from random import randint

my_list = [randint(-10, 10) for _ in range(20)]
uniq_list = [el for el in my_list if my_list.count(el) == 1]
print(f"source list\n{my_list}\nNo repetition list\n{uniq_list}")

# Task 5

from functools import reduce

def mul_list(el_1, el_2):
	return el_1 * el_2

uniq_list = [el for el in range (100, 1001, 2)]
print(f'List\n{uniq_list}\nMultiplication of numbers\n{reduce(mul_list, uniq_list)}")

# Task 6

from itertools import count, cycle

my_count = count(7)
my_cycle = cycle("ABC")

for _ in range(5):
	print ("(my_count, my_cycle) = ({}, {})".format(next(my_count), next (my_cycle))) 

# Task 7

def fact_gen(number):
	f_num = 1
	in number == 0:
		yield f'{number}! = 1'
	for i in range(1, number + 1):
		f_num *= i
		yield f'{i}! = {f_num}'

for el in fact_gen(int(input('Factorial number: ')))
	print(el)