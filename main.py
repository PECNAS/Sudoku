import argparse
from sudoku_plan import sudoku

parser = argparse.ArgumentParser() #создаём образ парсера
parser.add_argument('-c', '--color', action="store_true") # добавляем необязательный аргумент
parser.add_argument('-vz', '--visualize', action="store_true") # добавляем необязательный аргумент

parser.add_argument(type=str, dest="sudoku_first_row") # добавляем обязательный аргумент в виде чисел для судоку
parser.add_argument(type=str, dest="sudoku_second_row") # добавляем обязательный аргумент в виде чисел для судоку
parser.add_argument(type=str, dest="sudoku_third_row") # добавляем обязательный аргумент в виде чисел для судоку
parser.add_argument(type=str, dest="sudoku_fourth_row") # добавляем обязательный аргумент в виде чисел для судоку

try:
	args = parser.parse_args()
	if args.color:
		print("Color")
	if args.visualize:
		print("visualize")
	first_row = args.sudoku_first_row
	second_row = args.sudoku_second_row
	third_row = args.sudoku_third_row
	fourth_row = args.sudoku_fourth_row
except:
	print("Не введены аргументы, или введены неверно!\nвызовите программу с аргументом --get_help для помощи")

sudoku_grid = []
sudoku_grid.append(list(first_row))
sudoku_grid.append(list(second_row))
sudoku_grid.append(list(third_row))
sudoku_grid.append(list(fourth_row))

for x in sudoku_grid:
	for y in range(len(x)):
		if x[y].isdigit():
			x[y] = int(x[y])
			
sudoku.sudoku_start(sudoku_grid)