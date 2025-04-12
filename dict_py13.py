'''dictionary records are taking in runtime'''

d1={}
n=int(input())
for i in range(n):
    k=input()
    v=input()
    d1.update({k,v})
print(d1)

#program to print the frequencies of the elements present in the list

import collections
n=int(input())
x=list(map(int,input().split(' ',n-1)))
d=collections.Counter(x)
print(d)

''' o/p: 12
         1 2 3 4 5 1 2 3 4 5 1 1
        Counter({1: 4, 2: 2, 3: 2, 4: 2, 5: 2})'''

import collections
n=int(input())
x=list(map(int,input().split(' ',n-1)))
d=collections.Counter(x)
print(d)
hf=d.most_common()[0][0]
print(hf)
