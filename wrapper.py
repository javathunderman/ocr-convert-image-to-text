import os,sys
import re
from itertools import chain
from glob import glob
os.system("python3 main.py --input_dir programs/ --output_dir compiled/")
folder = "compiled/"
for filename in os.listdir(folder):
       infilename = os.path.join(folder,filename)
       if not os.path.isfile(infilename): continue
       oldbase = os.path.splitext(filename)
       print(filename)
       fileThing = open("compiled/"+filename, 'r')
       lines = [line.lower() for line in fileThing]
       with open("compiled/"+filename, 'w') as out:
           out.writelines(sorted(lines))
       newname = infilename.replace('.txt', '.py')
       output = os.rename(infilename, newname)


for filename in os.listdir(folder):
        try:
           os.system("python3 compiled/" + filename)
        except:
           print("oof")
