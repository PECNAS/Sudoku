def sudoku_check(first, second, third, fourth):
	print(f"{first}\n{second}\n{third}\n{fourth}")


if __name__ == "__main__":
	sudoku_check("14.3", "3..1", ".13.", "...4")

'''

1 4 2 3
3 2 4 1
4 1 3 2
2 3 1 4

1. В каждой строке каждое число от 1 до <размер судоку> встречается один раз
2. В каждом столбце каждое число от 1 до <размер судоку> встречается один раз
3. В каждом блоке каждое число от 1 до <размер судоку> встречается один раз
А также валидное судоку должно иметь только одно решение, не больше, не меньше!

'''