#A cashier has currency notes of denominations 100’s, 50’s, 20’s, 10’s, 5’s, 2’s and 1’s.
#If the amount to be withdrawn is input through the keyboard in hundreds,
#find the total number of currency notes of each denomination the cashier will have to give to the withdrawer.
#Input:
#Enter the amount: 565
#Output:
#There are:
#5 Note(s) of 100
#1 Note(s) of 50
#0 Note(s) of 20
#1 Note(s) of 10
#1 Note(s) of 5
#0 Note(s) of 2
#0 Note(s) of 1
m=int(input("Enter the amount:"))
hu=m//100
m=m%100
fi=m//50
m=m%50
tw=m//20
m=m%20
ten=m//10
m=m%10
f=m//5
m=m%5
t=m//2
m=m%2
one=m//1
print("There are:")
print(f"{hu} Note(s) of 100")
print(f"{fi} Note(s) of 50")
print(f"{tw} Note(s) of 20")
print(f"{ten} Note(s) of 10")
print(f"{f} Note(s) of 5")
print(f"{t} Note(s) of 2")
print(f"{one} Note(s) of 1")
