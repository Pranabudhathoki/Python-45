a = [1, 2, 3, "d", 4, 5, "a"]
for i in a:
    if isinstance(i, int):
        print("Integer:", i)
    elif isinstance(i, str):
        print("String:", i)