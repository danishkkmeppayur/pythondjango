import re

matcher=re.finditer("ab","ababababababbabababbabbababa")

count=0

for match in matcher:
    
    print(match.start())
    print(match.group())

    count+=1

print("count",count)