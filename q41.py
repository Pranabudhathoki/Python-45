num = int(input("Enter a number: "))
order = len(str(num))
sum_armstrong = 0
for i in str(num):
    sum_armstrong += int(i) ** order
if sum_armstrong == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")