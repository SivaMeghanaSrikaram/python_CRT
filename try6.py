try:
   a=int(input())
   b=int(input())
   c=a/b
   print(c)

except:
    print("given wrong input 2 chances left give correct i/p")
    ch=2
    while(ch):        
        a=int(input())
        b=int(input())
        if(a==0 or b==0):
            ch-=1
            if(ch==0):
                print("chances are over")
                break
            print(f"{ch} chances left give correct i/p")
            continue
        else:
            c=a/b
            print(c)
            break
