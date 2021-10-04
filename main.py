import os
import fnmatch

total_size=0
for path,dirs,files in os.walk('F:/C'):
    for file in files:
        if fnmatch.fnmatch(file,"*.pdf"):
            fullname = os.path.join(path,file)
            fp=os.path.join(path,file)
            if not os.path.islink(fp):
                total_size+=os.path.getsize(fp)
            print(fullname)
            print(total_size)

