import functools

lst=[10,20,30,31,32]

total=functools.reduce(lambda num1,num2:num1+num2,lst)

maxval=functools.reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
minval=functools.reduce(lambda num1,num2:num1 if num1<num2 else num2,lst)

print(total)
print(maxval)
print(minval)

