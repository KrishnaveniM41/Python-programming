binaryNumber=input("Enter the binary number: ")
exponent=len(binaryNumber)-1
decimal=0

for digit in binaryNumber:
    decimal += int(digit)*2**exponent
    exponent -= 1

print("Deciment equivalent is: ",decimal)



#decimal to binary

decimal=int(input("Enter the decimal number: "))
reminder=0
binary=0

for digit in decimal:
    binary=digit//2
    reminder=digit%2
    
print("Binary no: ",reminder)


#binary to octal
octal=input("Enter the octal number :")
binaryNumber=""
for digit in octal:
    number=int(digit)
