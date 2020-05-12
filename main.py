import argparse

parser = argparse.ArgumentParser() #создаём образ парсера
parser.add_argument('-c', '--color', action="store_true") # добавляем необязательный аргумент
parser.add_argument('-vz', '--visualize', action="store_true") # добавляем необязательный аргумент

parser.add_argument(type=str, dest="sudoku first row\n") # добавляем обязательный аргумент в виде чисел для судоку
parser.add_argument(type=str, dest="sudoku second row\n") # добавляем обязательный аргумент в виде чисел для судоку
parser.add_argument(type=str, dest="sudoku third row\n") # добавляем обязательный аргумент в виде чисел для судоку
parser.add_argument(type=str, dest="sudoku fourth row\n") # добавляем обязательный аргумент в виде чисел для судоку

try:
	args = parser.parse_args()
	if args.color:
		print("Color")
	if args.visualize:
		print("visualize")
except:
	print("Не введены аргументы, или введены неверно!\nвызовите программу с аргументом --get_help для помощи")