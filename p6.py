#Write a Python program to convert specified days into years, weeks and days.
#Note: Ignore leap year.

#Input:
#Write a Python program to convert specified days into years, weeks and days.
#Enter the number of Days: 1329
#Output:
#Years: 3
#Weeks: 33
#Days: 3
days=int(input("Enter the number of Days:"))
y=days//365
days=days%365
print("Years:",y)
w=days//7
days=days%7
print("Weeks:",w)
print("Days:",days)
