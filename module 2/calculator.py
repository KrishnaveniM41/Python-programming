print("\CALCULATOR\n")
print("\nCHOOSE THE OPERATION\n")
print("\n1.ADD\n2.SUB\n3.DIV\n4.MUL")
cal=int(input("choose the operation:"))
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
print("******************************")
if(cal==1):
    print(a+b)
elif(cal==2):
    print(a-b)
elif(cal==3):
    print(a*b)
elif(cal==4):
    print(a/b)
else:
    print("Invalid")


