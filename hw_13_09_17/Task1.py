#Конвертер из десятичной записи в запись в виде римских цифр (использовать функцию)

symbol_on_positions = [['I', 'V', 'X'], ['X', 'L', 'C'], ['C', 'D', 'M']]
templates = ['', '0', '00', '000', '01', '1', '10', '100', '1000', '02']

def into_roman_system(number):
	result = ''
	length = len(number)
	for i in range(0, length):
		templ = templates[int(number[i])]
		length=length-1
		for x in range(len(templ)):
			result += symbol_on_positions[length][int(templ[x])]
	return result

n = str (input())
print(into_roman_system(n))
