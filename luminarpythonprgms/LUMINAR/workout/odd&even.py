odd=[]
even=[]
lst=[]

for i in range(30,100):

    lst.append(i)

for i in lst:

    if(i%2==0):

        even.append(i)

    else:
        odd.append(i)

print("odd=",odd)
print("even=",even)
