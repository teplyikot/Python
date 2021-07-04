# Task 1

with open('text_1.txt', 'w', encoding='utf-8') as f:
	while True:
		line = input('Input new string or empty string to done: ')
		if not line:
			break
		# f.write(f"{line}\n")
		print(line, file=f)

# Task 2

with open ("text_2.txt", "r", encoding='utf-8') as f_obj:
	userful = [f'{line}. {' '.join(count.split())} - {len(count.split())} clos' for line, count in enumerate(f_obj, 1)]
	print(*userful, f"Всего строк - {len(userful)}.", sep="\n")	

# Task 3

with open('text_3.txt', 'r', encoding='utf-8') as f:
	employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
	print(f'Average salary = {round(sum(employees_dict.values()) / len(employees_dict), 3)}\n'
		f'Employees with salary lessthan 20k {[e[0] for e in employees_dit.items() if e[1] < 20000]}')

# Task 4

rus_dic = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("text_44.txt", "w", encoding='utf-8') as new_file:
	with open("text_4.txt", encoding='utf-8') as my_file:
		new_file.writelines([line.replace(line.split()[0], rus_dic.get(line.split()[0])) for line in my_file])

# Task 5

from random import randint

with open("text.txt". "w", encoding='utf-8') as my_file
	my_list = [randint(1, 100) for _ in range(100)]
	my_file.write(" ".join(map(str, my_list)))

print(f"Sum of elements - {sum(my_list)}")

# Task 6

mydict = {}
with open("tet_6.txt", encoding="utf-8") as fobj:
	for line in fobj:
		name, stats = line.split(':')
		name_sum = sum(map(int, "".join([i for i in stats if i == ' ' or '9' >= i >= '0']).split()))
		mydict[name] = name_sum
print(f"{mydict}")

# Task 7

import json

with open("my_ex7.json", "w", enconding="utf-8") as write_f:
	with open("text_7.txt", encoding="utf-8") as f_obj:
		profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f_obj}
		result = [profit, {"average_profit": round(sum([int(1) for i in profit.values( if int(i) > 0]) / len([int(i) for i in profit.values() if int(i) >0]))}]
	json.dump(result, write_f, ensure_ascii=False, indent=4)