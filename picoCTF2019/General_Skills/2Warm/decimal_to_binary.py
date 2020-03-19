def decimal_to_binary(n):
    if n>1:
        decimal_to_binary(n//2)
    print(n % 2,end="")

dec = int(input('Enter the decimal number : '))
decimal_to_binary(dec)
print()
