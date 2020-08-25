from re import *

pattern="[abc]" #either a , b or c

#or u can use "[a-z]"tat it use all alphbt from a to z
#or "[a-zA-Z]" for all upper and lower case alphabets
#"\s" check for spaces
#"\d" check for digit  or "[0-9]"
#"\w" for all words


matcher=finditer(pattern,"afdghbbaa")

for match in matcher:

    print(match.start())
    print(match.group())
