
def rhl(x,y):
    if(x>=y):
        print(x)
        x-=1
        rhl(x,y)  #recursive call


a=int(input())
b=int(input())
rhl(a,b);



'''
while(a>=b):
    print(a)
    a-=1
'''
