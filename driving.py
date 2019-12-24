country = input('請問你是那國人: ')
age = input('請輸入年齡: ')
age = int(age)
if country == '香港':
	if age >= 18:
		print('You Can Drive')
	else:
		print('You Cannot Drive')
