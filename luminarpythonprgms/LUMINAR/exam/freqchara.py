pattern="ABABABCAAA"

dict={}

for char in pattern:
    if(char not in dict):

        dict[char]=1

    else:

        dict[char]+=1

print(dict)


