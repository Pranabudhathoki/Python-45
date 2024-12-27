start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
sum_odd = 0
for i in range(start, end + 1):
    if i % 2 != 0:
        sum_odd += i
print("Sum of odd numbers:", sum_odd)