lst=[1,2,3,4]
new_lst=[]
for i in lst:
    if i==2:
        i="a"
    elif i==3:
        i=2
    new_lst.append(i)
print(new_lst)