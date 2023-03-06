num=int(input("Enter the number: "))
for i in range(2,(num//2)+1):
    if num%i==0:
        break
if i<(num//2):
    print("not prime")
else:
    print("prime")