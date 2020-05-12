def find_next_cell_to_fill(grid, i, j): # ищем следующую ячеку для заполнения
		for x in range(i, 4): # проходимся по горизонтали
			for y in range(j, 4): # проходимся по вертикали
				if grid[x][y] == ".": # если пустая 
					return x,y 
		#(Процесс заполнения)
		for x in range(0,4): # проходимся по горизонтали
			for y in range(0,4): # проходимся по вертикали
				if grid[x][y] == ".": # eсли равен .
					return x,y
		return -1,-1 # возвращаем -1 -1, когда всё заполнили

def is_valid(grid, i, j, e):
	rowOk = all([e != grid[i][x] for x in range(4)]) # вернёт True если ни одно число в генерируемом списке не равно 0
	if rowOk: # если True
		columnOk = all([e != grid[x][j] for x in range(4)]) # вернёт True если ни одно число в генерируемом списке не равно 0
		if columnOk: # если True
			# начинаем искать верхний левый координат, ориентируясь на i и j
			secTopX, secTopY = 2 * (i // 2), 2 * (j // 2) # используется этажное деление
			for x in range(secTopX, secTopX + 2): # с помощью двух циклов проверяем квадрат 3 на 3 клетки(первый цикл)
				for y in range(secTopY, secTopY + 2): # второй цикл
					if grid[x][y] == e:
						return False
			return True
	return False

def sudoku_check(grid):
	for x in grid:
		past = []
		for y in x:
			if y in past:
				print("[+]Bad sudoku!", y)
			else:
				print("[+]Good, nice Good", y)
				past.append(y)
		print()


def solve_sudoku(grid, i=0, j=0): # рекурсия
		i,j = find_next_cell_to_fill(grid, i, j) # передаём 0 и 0 (первые ячейки)
		if i == -1: # если функция поиска ячейки вернула -1
			return True
		for e in range(1,5): # заполняем числами от 1 до 4(указано 5, но цикл 5 не берёт(Я запомнил это уже давно))
			if is_valid(grid, i, j, e): # вызываем функцию 
				grid[i][j] = e
				if solve_sudoku(grid, i, j): # рекурсия
					return True

				grid[i][j] = 0 # обнуляем ячейку
		return False

if __name__ == "__main__":
	data = [[1, 4, ".", 3], [3, ".", ".", 1], [".", 1, 3, "."], [".", ".", ".", 4]]
	solve_sudoku(data)
	sudoku_check(data)
	for row in data:
		print(row)
'''
1 4 2 3
3 2 4 1
4 1 3 2
2 3 1 4

'''