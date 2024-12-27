bad_chars = [';', ':', '!', "*"]
string = "py;th*o:n!;py*t*h:o!n"
cleaned = ""
for i in string:
    if i not in bad_chars:
        cleaned += i
print(cleaned)