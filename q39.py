sum_even = 0
sum_odd = 0
for i in range(1,101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print(f"Sum of evens: {sum_even}, Sum of odds: {sum_odd}")