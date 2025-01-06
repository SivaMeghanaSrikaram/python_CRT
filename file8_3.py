x=open('s3batch.txt','rb') #if we want to change file object position no.of times then file is open in binary mode
x.seek(-10,2)
content=x.read()
print(content)
x.close()
