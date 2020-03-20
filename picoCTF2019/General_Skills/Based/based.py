# binary --> word
binary = input('Enter binary value : ')

word = ''.join(str(chr(int(x,2))) for x in binary.split())
print(word)


# octal --> word
octal = input('Enter octal value : ')

word = ''.join(str(chr(int(x,8))) for x in octal.split())
print(word)

# hex --> word
hexd = input('Enter hex value : ')

word = ''
inter = [hexd[i:i+2] for i in range(0,len(hexd),2)] 
word = ''.join(chr(int(x,16)) for x in inter)
print(word)