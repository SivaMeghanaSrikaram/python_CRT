import sys
sys.setrecursionlimit(50)

def cse2():
    global i
    print(i)
    i+=1
    cse2()


i=1
cse2()
