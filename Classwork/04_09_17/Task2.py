# Дан входной файл с арабскими числами. Перевести каждое число в римскую систему счисления

symbol_on_positions = [['I', 'V', 'X'], ['X', 'L', 'C'], ['C', 'D', 'M']]
templates = ['', '0', '00', '000', '01', '1', '10', '100', '1000', '02']

with open('numbers.txt', 'r', encoding='UTF-8') as file_object:
	for number in file_object:
		number = number.rstrip('\n')
		results = ''
		length = len(number)
		for i in range (length-1, -1, -1):
			templ = templates[int (number[i])]
			result = ''
			for x in range (len(templ)):
				result += symbol_on_positions[length-i-1][int (templ[x])]
			results = result + results
		print(results)


