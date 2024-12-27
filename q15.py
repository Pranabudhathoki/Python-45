a=input("Enter a sentence as yoou wish: ")
digit=0
letter=0
space=0
for i in a:
    if i.isalpha():
        letter+=1
    elif i.isdigit():
        digit+=1
    elif i.isspace():
        space+=1
print(f"Letters: {letter}")
print(f"Digits: {digit}")
print(f"Spaces: {space}")
