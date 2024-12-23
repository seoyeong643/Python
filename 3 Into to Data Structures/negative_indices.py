           # 0123456
my_string = "giraffe"
print(len(my_string))       # 7

print(my_string[-1])        # "e",  last character of "giraffe"
print(my_string[2:4])       # "ra", from index 2 to 4, non-inclusive of 4. 

print(my_string[-1:])       # "e"   same as [6:]
print(my_string[6:])

print(my_string[:-4])       # "gir" same as [:3]
print(my_string[:3])

print(my_string[-4:-1])     # "aff" same as [3:6]
print(my_string[3:6])