string = '                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                '

one = ' '
two = '  '
new_string = ''

for x in string:
	if x == one:
		new_string += '1'

	else:
		new_string += '0'

print(new_string)
