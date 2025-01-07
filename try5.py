try:
   fileptr=open("cse2.txt","r")
   fileptr.write("hi we are in rise")
    
except:
    print("wrong operation")
    
else:
    print("mode of the file is read")

finally:
    print("file closed")
    print("Error")
