from zipfile import *
p=ZipFile("cse.zip",'r',ZIP_STORED)
a=p.namelist()
for x in a:
    print(x)
p.close()
