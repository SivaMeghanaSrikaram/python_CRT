#Write a Python program to read the total number of seconds from the user and convert it into the following format – Hours:Minutes:Secondsnput:
#Input seconds: 25300
#Output:
#H:M:S - 7:1:40
sec=int(input("seconds: "))
h=sec//3600
sec=sec%3600
m=sec//60
sec=sec%60
print(F"H:M:S - {h}:{m}:{sec}")
