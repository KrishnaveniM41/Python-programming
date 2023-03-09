print([1,24,76])

for i in [5,4,3,2,1]:
    print(i)
print("Blastoff!")


friends=['Joseph','Glenn','Sally']
for friend in friends:
        print('Happy new year! :',friend)
print('Done')

#Looking inside Lists
print(friends[1]) #printing values by indexing

#Lists are mutable
fruit="banana"
fruit[0]="f"  #str are not mutable

#long is list
greet ='Hello bob'
print(len(greet))

x=[1,2,'Joe',99]
print(len(x))

#concatenation of list
a=[1,2,3,4]
b=[5,6,7]
c=a+b
print(c)

#List can be sliced
t=[9,41,6,5,36]
print(t[1:3])  #slicing 2nd to 3rd]
print(t[:4])#slicing first position to 4th pos]


#list methods

x=list()
print(type(x))
print(dir(x))

L.append(element) #Adds element to thw end of L
L.extend(aList)   #Adds the element of aList to the end
insert(index, element) 

myList=list()
print(type(myList))
myList.append(10)
print(myList)
myList.append(20)
print(myList)
myList.pop(0)
print(myList)
mySecondList=[50,60,70]
myList.extend(mySecondList)
print(myList)

#Is something in list
some=[1,3,9,5,6,5]
print(9 in some)
print(9 not in some)

#sort
some=['Joseph','Glenn','Aryan']
some.sort()
print(some)