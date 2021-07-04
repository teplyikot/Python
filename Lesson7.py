# Task 1

class Matrix:
	def __init__(self, data):
		self.data = data

	def __str__(self):
		return '\n'.join('\t'.join([f"{itm:03}" for itm in line]) for line in self.data)

	def __add__(self, other):
		try:
			m = [[int(self.data[line][itm]) + int(other.data[line][itm]) for itm in range(len(self.data[line]))] for line in range(len(self.data))]
			return Matrix(m)
		except IndexError:
			return f'ќшибка размерностей матриц'

m_1 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
m_2 = [['5', '7', '23'], ['9', '23', '-54'], ['12', '3', '16']]

mtrx_1 = Matrix(m_1)
mtrx_2 = Matrix(m_2)
new_m = mtrx_1 + mtrx_2

# Task 2

from abc import ABC, abstractmethod

class Clothes(ABC):
	result = 0

	def __init__(self, param):
		self.param = param

	@property
	@abstractmethod
	def consumption(self):
		pass

	def __add__(self, other):
		Clothes.result += self.consumption + other.consumption
		return Costume(0)

	def __str__(self):
		res = Clothes.result
		Clothes.result = 0
		return f"{res}"

class Coat(Clothes):
	@property
	def consumption(self):
		return round(self.param / 6.5) + 0.5

class Costume(Clothes):
	@property
	def consumption(self):
		return round((2 * self.param + 0.3) / 100)

coat = Coat(42)
costume = Costume(170)
print(coat + costume + coat)

# Task 3

class Cell
	def __init__(self, nums):
		self.nums = nums

	def make_order(self, rows):
		return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

	def __str__(self):
		return f"{self.nums}"

	def __add__(self, other):
		print("Sum of cell is:")
		return Cell(self.nums + other.nums)

	def __sub__(self, other):
		print("Subtraction of cell is:")
		return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
			else "ячеек в первой клетке меньше второй, вычитание невозможно!"

	def __mul__(self, other):
		print("Multiply of cell is:")
		return Cell(self.nums * other.nums)

	def __floordiv__(self, other):
		print("Truediv of cell is:")
		return Cell(self.nums // other.nums)

cell_1 = Cell(15)
cell_2 = Cell(24)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_2.make_order(7))