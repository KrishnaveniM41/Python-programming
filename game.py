import random
low=int(input("Enter the lower range: "))
high=int(input("Enter the higher range :"))
myNumber=random.randint(low, high)
print(myNumber)
while(1):
    count = 1
    count += 1
    userNumber=int(input("Enter a number with in the limit: "))
    if userNumber > myNumber:
        print("TOO BIG")
    elif userNumber < myNumber:
        print("TOO SMALL")
    else:
        print("CONGO!!! YOU GOT IT!!!")
    break;       
    