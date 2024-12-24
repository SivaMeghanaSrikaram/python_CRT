l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
new=[]
for i in range(len(l1)):
        for j in range(len(l2)):
            if(l1[i]*2==l2[j]):
                new.append(l1[i])


print(new)
      
        
    
