vowels = "aeiouAEIOU"
string = input("Enter a string: ")
no_vowels = ""
for i in string:
    if i not in vowels:
        no_vowels += i
print(no_vowels)