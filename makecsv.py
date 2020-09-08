import os
import csv

folders = ["OPENLAND", "OTHERS", "URBAN", "VEGETATION", "WATER"]
use=""
i=0
with open('data.csv' , mode='w') as f:
    ff=csv.writer(f, delimiter =',')
    for filename in os.listdir("ALL"):
        for folder in folders:
            if filename.startswith(folder):
                use=folder
                break
            else:
                i+=1
        if(filename.endswith(".tif")):
            ff.writerow([filename, i])
        i=0

print("Success!")
    

    
