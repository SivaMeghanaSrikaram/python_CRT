#Consider that you have purchased a Laptop – price get it from the user upon which a sales tax of 6% is applied. Write a Python program that calculates and displays the total purchase price of the Laptop.

c=int(input("Enter the price of the Laptop:"))
tc=c*(6/100)
c=c+tc
print("Total Cost Price of the Laptop is",c)
