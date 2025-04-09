'''write a prog to verify given string is palindrome or not.'''
a=input()
if(a==a[::-1]):
    print("Yes")
else:
    print("No")
