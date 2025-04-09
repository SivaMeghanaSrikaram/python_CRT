a=int(input())
b=int(input())
c=int(input())
if(a>=40 and b>=40 and c>=40):
    if(a>=65 and b>=65) or (a>=65 and c>=65) or b>=65 and c>=65:
        print("Seat is confirmed")
    else:
        print("No")
else:
    print("not eligible")
