n=int(input())
s=0
while(s==0 or s>=10):
    s=0
    while(n!=0):
        r=n%10
        n=n//10
        s=s+r
    n=s
print(s)


'''def addDigits(self, num):
        if(num==0):
            return 0
        else:
            num=(num-1)%9+1
            return num'''
