even=[]
odd=[]
ls=[]

for i in range(50,100):

    ls.append(i)


for i in ls:
    if(i%2==0):

        even.append(i)

    else:

        odd.append(i)


print(odd)
print(even)


