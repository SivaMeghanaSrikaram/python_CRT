nov=300.0
non=400.0
dv=600.0
dn=800.0
exc=100.0
ext=100.0
waterb=20.0
ket=5.0
sd=75.0
takeaway=20.0
print("Pizza categories")
print("1.Normal")
print("2.Deluxe")
pc=int(input("Enter your Choice [1 or 2]:"))
print("Pizza Types")
print("1.Veg")
print("2.Non Veg")
pt=int(input("Enter your Choice [1 or 2]:"))
bill=0
if pc==1 and pt==1:
    bill=bill+300
elif pc==1 and pt==2:
    bill=bill+400
elif pc==2 and pt==1:
    bill=bill+600
elif pc==2 and pt==2:
    bill=bill+800
ec=int(input("Extra Cheese? [1.Yes or 2.NO]:"))
if ec==1:
    bill=bill+100
et=int(input("Extra Topping? [1.Yes or 2.NO]:"))
if et==1:
    bill=bill+100
wb=int(input("Do you want Water Bottles? [1.Yes or 2.NO]:"))
if wb==1:
    nwb=int(input("How many Water Bottles?"))
    bill=bill+(nwb*20)
k=int(input("Do you want Ketchup? [1.Yes or 2.NO]:"))
if k==1:
    packets=int(input("How many Packets? :"))
    bill=bill+(packets*5)
d=int(input("Do you want Soft Driknks? [1.Yes or 2.NO]:"))
if d==1:
    nd=int(input("How many soft drinks do you want?"))
    bill=bill+(nd*75)
ta=int(input("Is it a Take Away? [1.Yes or 2.NO]: "))
if ta==1:
    bill=bill+20.0
GST=bill*0.18
print()
print("------------------------------------")
print("***** Pizza Bill Generator *****")
if pc==1 and pt==1:
    print("Base Price         =",nov)
elif pc==1 and pt==2:
    print("Base Price         =",non)
elif pc==2 and pt==1:
    print("Base Price         =",dv)
elif pc==2 and pt==2:
    print("Base Price         =",dn)
if ec==1:
    print("Extra Cheese       =",exc)
if et==1:
    print("Extra Toppings     =",ext)
if wb==1:
    print("Water Bottle       =",nwb*waterb)
if k==1:
    print("Ketchup Packets    =",packets*ket)
if d==1:
    print("Soft Drinks        =",nd*sd)
if ta==1:
    print("Take Away          =",takeaway)
print("------------------------------------")
print("Total Cost         =",bill)
print("GST Charges        =",GST)
print("------------------------------------")
print("Net Amount Payable =",bill+GST)
