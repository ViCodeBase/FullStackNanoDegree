import os
file_List = os.listdir("/Users/Vicky/FullStackNanoDegree/ProgrammingWithPython/prank")
dir_path = os.getcwd()
print dir_path
os.chdir("/Users/Vicky/FullStackNanoDegree/ProgrammingWithPython/prank")
for file in file_List:
    print "Renaming file - " + file + " to - " + file.translate(None,"01234556789")
    os.rename(file, file.translate(None,"01234556789"))