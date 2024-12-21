pal=lambda s:'palindrome' if(s==s[::-1]) else "not palindrome"

#print('palindrome') above when only pal(s) statement in down

s=input()
print(pal(s))
