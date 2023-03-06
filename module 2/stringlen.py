##to find length of a string
print(len("Fire fist ace"))   
##subscript operator
n="chicken"
print(n[3])

name="Bincy is a baka"
print(name[11])
print(len(name))
print(name[-1])  #last alphabet
print(name[-2])  #second last alphabet

data="Bincy is scientifically proven as a vazha"
for index in range(len(data)):
    print(index,data[index])
    


##slicing for stringd
##str_object[start_pos:end_pos:steps]
s="bincy is not tall"
first_five_chars=s[:5]
print(first_five_chars)

third_to_fifth_chars=s[2:5]
print(third_to_fifth_chars)
#to reverse a string
reverse_str=s[::-1]   
print(reverse_str)

s="bincy is a bishhh"
s1=s[-1:1:-2]
print(s1)

#checking for substrings
filelist=["myfile.txt","myprogram.exe","yourfile.txt"]
for filename in filelist:
    if ".txt" in filename:
        print(filename)

data="myprogram"
print(data[2])
print(data[-1])
print(len(data))
print(data[0:8])

