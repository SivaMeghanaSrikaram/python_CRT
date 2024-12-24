
def rlh(x,y):
    if(x<=y):
        print(x)
        x+=1
        rlh(x,y)  #recursive call


a=int(input())
b=int(input())
rlh(a,b);



'''
while(a<=b):
    print(a)
    a+=1
'''
