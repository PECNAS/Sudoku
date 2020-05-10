import argparse

parser   = argparse.ArgumentParser() #создаём образ парсера
parser.add_argument('-c', '--color', action="store_true") # добавляем необязательный аргумент
parser.add_argument('-vz', '--visualize', action="store_true") # добавляем необязательный аргумент
args     = parser.parse_args()

if args.color:
	print("Color")
if args.visualize:
	print("visualize")