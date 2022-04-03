#STRING SLICING
#Accessing a range of character not just one through there index positions
#You can command negative and positive indexing
#In indexing and slicing spacing is also sounted as a character

#Index from left to right even in negative numberhed by supplying 2 index positions separated by a colon e.g
#School [1:4] #the last index position is not included in the output
#School [1:]returns from the commanded position to the end
school="AkiraChix"
print(school[1:4])

#returns characcters from the commanded position to the second last position...
# emits the last position
print(school[-4:-1])

#Given the string p= "Hello Python world"
#Conduct the following exercises

#0    1   2   3   4     5    6    7    8    9  10   11   12  13   14    15   16   17
#H    e   l   l   o          P    y    t    h   o   n         W    o    r    l    d
#-18 -17 -16 -15  -14  -13  -12  -11  -10   -9  -8  -7   -6   -5   -4   -3   -2    -1

p="Hello Python World"
#Use positive number slicing to print
#Python
#Hell
#World
print(p[6:12])
print(p[0:4])
print(p[13:])

#Use the negative number slicing to print
#Python World
#Hello python

print(p[-12:])
print(p[-18:-6])

#replacing letters
#replace any occurence of o with a
print(p.replace("o","a"))

#convert the string to uppercase
print(p.upper())

#convert the string to lowercase
print(p.lower())

#find the number of occurence of character "o"
print(p.count("o"))