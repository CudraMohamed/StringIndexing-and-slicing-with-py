#STRING SLICING
#Accessing a range of character not just one through there index positions
#You can command negative and positive indexing

#Index from left to right even in negative numberhed by supplying 2 index positions separated by a colon e.g
#School [1:4] #the last index position is not included in the output
#School [1:]returns from the commanded position to the end
school="AkiraChix"
print(school[1:4])

#returns characcters from the commanded position to the second last position...
# emits the last position
print(school[-4:-1])

