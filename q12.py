a=[1,2,3,4,5]
odd_list=[]
even_list=[]
for i in a:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("Even list:",even_list)
print("Odd list:",odd_list)
