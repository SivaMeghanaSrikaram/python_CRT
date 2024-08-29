#Write a Python program that reads a floating-point number and then display the right-most digit of the
#integral part of the number.
#Output:
#Enter a Floating-point Number: 1423.569
#Right-most Number is 3
d=float(input("Enter a Floating-point Number: "))
i=int(d)
r=i%10
print("Right-most Number is",r)
