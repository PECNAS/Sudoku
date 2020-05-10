class Sudoku():
	def __init__(self, first, second, third, fourth):
		self.first = first
		self.second = second
		self.third = third
		self.fourth = fourth
		self.row_elements = []
	def append_elements(self):
		self.row_elements.append(list(self.first))
		self.row_elements.append(list(self.second))
		self.row_elements.append(list(self.third))
		self.row_elements.append(list(self.fourth))
	def column_check(self, column_number): # проверяем элементы
		column = []
		for i in range(4): # проходимя по всем строкам
			try:
				if int(self.row_elements[i][column_number]) in (1, 2, 3, 4): # работаем с двумерными массивами
					column.append(self.row_elements[i][column_number])
				else:
					print("Bad data")
			except ValueError:
				print("Full point")
				column.append(".")

		print(column)




if __name__ == "__main__":
	sudoku = Sudoku("14.3", "3..1", ".13.", "...4")
	sudoku.append_elements()
	sudoku.column_check(3)





#	do something...

'''
"14.3" "3..1" ".13." "...4"
---------------------
1 4 . 3
3 . . 1
. 1 3 .
. . . 4
---------------------

1. В каждой строке каждое число от 1 до <размер судоку> встречается один раз
2. В каждом столбце каждое число от 1 до <размер судоку> встречается один раз
3. В каждом блоке каждое число от 1 до <размер судоку> встречается один раз
А также валидное судоку должно иметь только одно решение, не больше, не меньше!

'''