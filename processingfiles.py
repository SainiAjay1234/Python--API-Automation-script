import os
import sys
import json
from os import listdir
from os.path import isfile, join

mypath_1 = r"C:\Users\Administrator\AppData\Local\Programs\Python\Python37\IntegrationTests\app\multiple_points\MultipleUpdatesProgram\ResponseFiles"
mypath_2 = r"C:\Users\Administrator\AppData\Local\Programs\Python\Python37\IntegrationTests\app\multiple_points\MultipleUpdatesProgram\ProcessedResponseFiles"
mypath_3 = r"C:\Users\Administrator\AppData\Local\Programs\Python\Python37\IntegrationTests\app\multiple_points\MultipleUpdatesProgram\errorfiles"

# bad_words = ['errors', 'invalid', 'err']

# #myfiles is a list for all 24 text files
# myfiles = [f for f in listdir(mypath_1) if isfile(join(mypath_1, f))]
# print(myfiles)
# print(type(myfiles))
# for i in range(len(myfiles)):
#         with open(mypath_1+ "\\" + myfiles[i], 'r') as file:
#             output=""
#             for line in file:
#                 if not line.isspace():
#                     output+=line
#         f= open(mypath_1+ "\\" + myfiles[i], "w")
#         f.write(output)
#         with open(mypath_1+ "\\" + myfiles[i], "r") as oldfile, open(mypath_2+ "\\processed_" + myfiles[i], 'w') as newfile, open(mypath_3+"\\error_"+ myfiles[i], "w") as errfile:
#             for line in oldfile:
#                 #print (line)
#                 if not any(bad_words in line for bad_words in bad_words):
#                     newfile.write(line)
#                     #print (line)
#                 elif any(bad_words in line for bad_words in bad_words):
#                     errfile.write(line)

def remove_empty(path):
    print(list(os.walk(path)))
    for (dirpath, folder_names, files) in os.walk(path):
        for filename in files:
            file_location = dirpath + '/' + filename  #file location is location of the file
            if os.path.isfile(file_location):
                if os.path.getsize(file_location) == 0:#Checking if the file is empty or not
                    os.remove(file_location)  #If the file is empty then it is deleted using remove method


   
remove_empty(mypath_2)  # Calling the function    
remove_empty(mypath_3)