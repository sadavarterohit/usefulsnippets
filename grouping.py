import os
import shutil
folders = ["OPENLAND", "OTHERS", "URBAN", "VEGETATION", "WATER"]
dest= "ALL"  #foldername
os.mkdir(dest)

for folder in folders:
    for filename in os.listdir(folder):
        
        if(filename.endswith(".tif")):
            dst=os.path.join(folder,filename)
            shutil.copy(dst,dest)

            #USED TO RENAME, DON'T NEED HERE LEL.
            #newdst = os.path.join(dest,filename)
            #newname = os.path.join(dest, str(folder+filename))
            #os.rename(newdst, newname)


print("Success!")

            



