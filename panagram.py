'''panagaram--->in a string all the alphabets must be present'''
import string
s=input()
u=string.ascii_uppercase
l=string.ascii_lowercase
if all(i in s or j in s for i,j in zip(u,l)):
    print("pangram")
else:
    print("not a pangram")
