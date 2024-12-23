my_string = "alpha"

multiline_string = """bravo
charlie"""
print(my_string)            #prints "alpha"
print(multiline_string)     #prints "bravo" then "charlie" 


print(my_string[0])         #prints "a"
print(my_string[3])         #prints "h"


print(my_string[0:3])       #prints "alp"
print(my_string[:2])        #prints "al"
print(my_string[2:])        #prints "pha"
print(my_string)            #prints "alpha"


for char in my_string:
    print(char)             #prints a l p h a letter by letter

print("pha" in my_string)   #prints "True"
print("z" not in my_string) #prints "True"