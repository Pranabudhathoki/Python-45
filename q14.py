a = [1, 2, 3, "d", 4, 5, "a"]
integers = []
strings = []
for i in a:
    if isinstance(i, int):
        integers.append(i)
    elif isinstance(i, str):
        strings.append(i)
print("Integers:", integers)
print("Strings:", strings)