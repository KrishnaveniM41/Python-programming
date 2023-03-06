decimal=input("Enter the decimal number: ")
length=len(decimal)+1
binary=0
reminder=0

for digit in decimal:
    reminder=int(digit)%2
    
print("Binary no: ",reminder)