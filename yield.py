def print_even(t_list):
    for i in t_list:
        if i%2==0:
            yield i #return the value to calling function i.e., stored in 'j' and control will come back

t_list= [1,4,5,6,7]
print(t_list)


a=1
print("Even no in list are: ", end=" ")
for j in print_even(t_list):
    print(j,a)
    a+=1        #to see the data executed step by step
