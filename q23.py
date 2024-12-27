lst = input("Enter a string: ")
space = 0
for i in lst:
    if i.isspace():           # i==" "
        space += 1
print("Number of spaces:", space)