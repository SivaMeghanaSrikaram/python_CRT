from zipfile import *
p=ZipFile("cse.zip",'w',ZIP_DEFLATED)
p.write('s3batch.txt')
p.close
