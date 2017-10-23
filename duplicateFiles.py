import os
import shutil

#set source and destination folders for duplicates
src = 'C:\\Users\\dbwilson\\Documents\\_RevitLocals\\DynamoAutomation\\'
dst = src
#collect files in directory
f = os.listdir(src)
#list all files in directory to duplicate
for i in f:
    print(i)
#select file in directory to duplicate
name = os.path.splitext(f[0])[0]
ext = os.path.splitext(f[0])[1]

#verify file to be duplicated
print(name)
print(ext)

#number of duplicates
count = 40


# use base filename and append a number to it.
#uncomment to run -- dangerous!
# for i in range(count):
#     shutil.copy(src + f[0], dst + name + "-" + str(i) + ext)