a=[1,2,3,4,5]
sum=0
for i in a:
    sum +=a[i]
print(sum)

a = eval(input("Enter a list of numbers (e.g., [1, 2, 3]): "))
if isinstance(a, (list, tuple)): 
    sum = 0
    for i in a:
        sum += i
    print("Sum:", sum)
else:
    print("Error: Please enter a list or tuple of numbers.")