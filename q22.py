start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
sum_even = 0
for i in range(start, end + 1):
    if i % 2==0:
        sum_even += i
print("Sum of even numbers:", sum_even)