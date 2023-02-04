# multiple points at different instances 
import json
from os import listdir
from os.path import isfile, join

mypath = r"C:\Users\Administrator\AppData\Local\Programs\Python\Python37\IntegrationTests\app\multiple_points\MultipleUpdatesProgram\ResponseFiles"
mypath1 = r"C:\Users\Administrator\AppData\Local\Programs\Python\Python37\IntegrationTests\app\multiple_points\MultipleUpdatesProgram\output"
mypath2 = r"C:\Users\Administrator\AppData\Local\Programs\Python\Python37\IntegrationTests\app\multiple_points\MultipleUpdatesProgram\SummaryReport"

#myfiles is a list for all 24 text files
myfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# print(myfiles)

#Running the loop for analysis for every text file one by one
for i in range(len(myfiles)):
    f = open(mypath+ "\\" + myfiles[i], 'r')
    lines = f.readlines()[1:]
    list_AV = []
    max_list=[]
    diff_list = [] 
    count1 = 0
    count2 = 0 
    count3 = 0 
    for line in lines:
        data_dict = json.loads(line)
        AV_VALUE =  data_dict["values"][0]["fields"]["AV"]
        list_AV.append(AV_VALUE)
        
    print(list_AV)
    for j in range(len(list_AV)-1):
        diff = abs(list_AV[j+1] - list_AV[j])
        diff_list.append(diff)
        print(diff_list)
        
        if(diff == 1):
            count1 = count1 + 1
        elif(diff == 0):
            count2 = count2 + 1
        elif(diff > 2):
            count3 = count3 + 1   
        
        #generating output files corresponding to each response file (24 input files so 24 output files will be created) 
        with open(mypath1+"\\out_"+myfiles[i], "a+") as file:
            file.write("\n")
            file.write("the previous value: " + str(list_AV[j]))
            file.write("\n")
            file.write("the current value: "+ str(list_AV[j+1]))
            file.write("\n")
            file.write("the difference is: " + str(diff))
            file.write("\n******************************")
                
                    
                    
    # generating the summary file for results 
    with open(mypath2+"\\MainResult.txt", "a+") as file:
        file.write("***********************TEST RESULTS**********************************")
        file.write("\n") 
        file.write("\nAnalysis for Point: " + str(myfiles[i][:-4]))
        file.write("\n") 
        file.write("max values of difference: {} ".format(max(diff_list)))
        file.write("\n")  
        file.write("\nthe difference list is:"  + str(diff_list))
        file.write("\n") 
        file.write("\nNo of times difference is more then the allowed limit:  {count3}".format(count3=count3))
        file.write("\n") 
        for val in diff_list:
            if(val > 2):
                file.write("\nTest case failed! difference value: " + str(val) + " (more than the allowed limit..)")
                file.write("\n")  

