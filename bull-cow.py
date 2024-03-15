import random
promt = 'Это игра "Быки и коровы". Надо отгадать 4 числа [х, х, х, х]\n'
promt += 'Быки (число): числа, что совпали И на своем месте.\n'
promt += 'Коровы (число): числа, что совпали И не на своем месте.\n'
promt += 'P.S. ошибки не отлажены, пиши только 4-значное число.\n'
bull = 0

#Создаем 4 не повторяющихся числа
num_1 = random.randint(0, 9)
num_2 = random.randint(0, 9)
num_3 = random.randint(0, 9)
num_4 = random.randint(0, 9)
while num_2 == num_1:
	num_2 = random.randint(0, 9)
while num_3 == num_2 or num_3 == num_1:
	num_3 = random.randint(0, 9)
while num_4 == num_3 or num_4 == num_2 or num_4 == num_1:
	num_4 = random.randint(0, 9)

#Вот он, тот самый ЗАГАДАННЫЙ список!
wish = [num_1, num_2, num_3, num_4]
print(promt)

def guess(my_guess): #функция ввода чисел и перевода в список
	my_guess = int(input('Введи числа: '))
	if my_guess < 1000:
		new_guess = [int(x) for x in str(my_guess)]
		new_guess.reverse()
		new_guess.append(0)
		new_guess.reverse()
	elif my_guess < 10000:
		new_guess = [int(x) for x in str(my_guess)]
	else:
		print('Error')
	return new_guess

def error(bull, cow): #Функция подсчета коров и быков и вывод списка
	#Ищем быков!
	if a[0] == wish[0]:
		bull += 1
	if a[1] == wish[1]:
		bull += 1
	if a[2] == wish[2]:
		bull += 1
	if a[3] == wish[3]:
		bull += 1
	#Ищем коров!
	if a[0] == wish[1] or a[0] == wish[2] or a[0] == wish[3]:
		cow += 1
	if a[1] == wish[0] or a[1] == wish[2] or a[1] == wish[3]:
		cow += 1
	if a[2] == wish[0] or a[2] == wish[1] or a[2] == wish[3]:
		cow += 1
	if a[3] == wish[0] or a[3] == wish[1] or a[3] == wish[2]:
		cow += 1
	return [bull, cow]

while bull != 4:
	#Инициализация функции ввода чисел
	a = guess(5555)
	#Инициализация функции подсчета быков и коров
	b = error(0, 0)
	bull = b[0]

	#Преобразуем список задуманного для принта
	list_x = ''
	for i in a:
		list_x = list_x + str(i)

	#Создаем словарь историй
	history = {}
	history[list_x] = b
	for keys, value in history.items():
		print(keys, value)
if bull == 4:
	print(f'Поздравляю! Было задумано: {num_1}{num_2}{num_3}{num_4}')
