def convert(num, base):
	result = ''
	while num > 0:
		result = str(num % base) + result
		num = num // base
	print(result)

try: 
	a = int(input('Введите число: '))
	b = int(input('Введите целевую систему счисления: '))
	if a > 0 and b == 2 or b == 8:
		convert(a, b)
	else:
		print('Ошибка входных данных.')

except ValueError :
	print('Ошибка входных данных.')
