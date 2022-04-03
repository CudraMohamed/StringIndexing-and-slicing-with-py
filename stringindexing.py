#STRING INDEXING
#Index allows us to access individual or a range of xters in a string
#Each character in a string is assigned an index position

# 0 1 2 3 4 5 6 7 8
# A k i r a C h i x
#-9-8-7-6-5-4-3-2-1

#Positive indexing starts at 0
school=("AkiraChix")
print(school[2])
print(school[8])

# String negative starts with -1 form the left
print(school[-8])
print(school[-1])


#Given the string p= "Hello Python world"
#Conduct the following exercises
#Using positive indexing to print the first chracter of each word in the string

#0    1   2   3   4     5    6    7    8    9  10   11   12  13   14    15   16   17
#H    e   l   l   o          P    y    t    h   o   n         W    o    r    l    d
#-18 -17 -16 -15  -14  -13  -12  -11  -10   -9  -8  -7   -6   -5   -4   -3   -2    -1

p="Hello Python World"
print(p[0])
print(p[6])
print(p[13])

#Use the negative indexing to print the last character of each word in the string
print(p[-14])
print(p[-7])
print(p[-1])