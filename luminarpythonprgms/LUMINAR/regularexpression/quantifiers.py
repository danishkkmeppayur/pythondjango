from re import *

#pattern="a+"

#pattern="a*"

#pattern="a?"

pattern="a{3,4}"

matcher=finditer(pattern,'abaabaaaabfhgfytuy')

for match in matcher:

    print(match.start())
    print(match.group())

