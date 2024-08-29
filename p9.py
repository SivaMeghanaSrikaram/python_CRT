#Ramesh’s basic salary is input through the keyboard. His dearness allowance is 40% of basic salary,
#and house rent allowance is 20% of basic salary. 
#Write a Python program to calculate his gross salary.
#Input:
#Enter the Basic Pay: Rs.10000
#Output:
#***** Salary Details *****
#Basic Salary:			Rs.10000.00
#Dearness Allowance:		Rs. 4000.00
#House Rent Allowance:	         Rs.2000.00
#Gross Pay is 			Rs.16000.00
sal=int(input("Enter the Basic Pay: "))
da=sal*(40/100)
hra=sal*0.2
gross=sal+da+hra
print("Basic Salary:       ",sal)
print("Dearness Allowance:      ",da)
print("House Rent Allowance:    ",hra)
print("Gross Pay is     ",gross)
