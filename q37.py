even_count = 0
odd_count = 0
for num in range(1,50):
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Even: {even_count}, Odd: {odd_count}")