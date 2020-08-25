f=open("numbers", "r")

lst=[]

for num in f:

    lst.append(num.rstrip("\n"))

print(lst)