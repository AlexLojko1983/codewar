def create_phone_number(n):
    numbers = '1234567890'
    str_n = ''.join([i for i in str(n) if i in numbers])
    return f'({str_n[:3]}) {str_n[3:6]}-{str_n[6:]}'


list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(create_phone_number(list_1))

'''
def create_phone_number(n):
	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
'''