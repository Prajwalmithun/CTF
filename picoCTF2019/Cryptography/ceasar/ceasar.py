#! /bin/python3


#cipher = "abggbbonqbsnceboyrz"

# picoCTF{ynkooejcpdanqxeykjrnpavoth} This is should be decrypted

cipher = "ynkooejcpdanqxeykjrnpavoth"
for i in range(26):
	print("Shift ",i)
	res = ''
	for x in cipher:
		res += chr((ord(x)+i)%26+97) #for lowercase
		#res += chr((ord(x)+i)%26+65) for uppercase
	print(res + '\n')

