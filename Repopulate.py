
import requests
import os
import time
import json
import sys

resp = requests.post("https://ov38.dmz.com:9191/v1/security/token", data={"username":"Administrator","password":"Welcome@1234"}, verify="ov38.dmz.crt")
Headers = {}
Headers["Authorization"] = "Bearer " + resp.json()["token"]

path = r"C:\Users\Administrator\AppData\Local\Programs\Python\Python37\IntegrationTests\app\multiple_points\Ajay\MultipleSidUpdate"

url_SPDResponse =  "http://192.168.116.205:9001/v1/points/spd" 
response = requests.get(url_SPDResponse, headers=Headers, verify="ov38.dmz.crt")
signal = response.text
print(type(signal))
with open(path+ "Repopulate.json", "w") as file:
        file.write("\n")
        file.write(signal)
        file.write("\n")
with open(path+ 'Repopulate.json') as file:
        data = json.load(file)
        f = open(path+ "Repopulate.json", 'r')
        lines = f.readlines()[1:]
        json_sid1 = [] 
        json_pnt1 = []
        for line in lines:
            data_dict = json.loads(line)
            IsComp = data_dict["IsComplete"]
            i = 1
            data={}
            data_dict={}
            print(IsComp)
"""
            while IsComp == False:
                    a = 4
                    print(a)
                    with open(path+ "Repopulate"+str(i)+".json", "w") as file:
                            file.write("\n")
                            file.write(signal)
                            file.write("\n")
                    with open(path+ 'Repopulate'+str(i)+'.json') as file:
                            key=str(i)
                            data[key] = json.load(file)
                            f = open(path+ "Repopulate"+str(i)+".json", 'r')
                            lines = f.readlines()[1:]
                            json_sid = []
                            json_pnt = []
                            for line in lines:
                                    data_dict[key] = json.loads(line)
                                    IsComp = data_dict[key]["IsComplete"]
                                    #print(IsComp)
                                    key1 = len(data_dict[key]["points"])
                                    points_sid =  data_dict[key]["points"][key1-1]["SID"]
                                    points_pn = data_dict[key]["points"][key1-1]["PN"]
                                    #print(points_sid)
                                    #print(points_pn)
                                    json_sid.append(points_sid)
                                    json_pnt.append(points_pn)
                                    #print(json_sid)
                                    #print(json_pnt)
                                    url_SPDResponse =  "http://192.168.116.205:9001/v1/points/spd" +"?"+ "start=" + str(points_sid)
                                    #print(url_SPDResponse)
                    i += 1
"""












""""
i = 1
data={}
data_dict={}
while i <= 59:
        #print(i)
        with open(path+ "Repopulate"+str(i)+".json", "w") as file:
                file.write("\n")
                file.write(signal)
                file.write("\n")
        with open(path+ 'Repopulate'+str(i)+'.json') as file:
                key=str(i)
                data[key] = json.load(file)
                f = open(path+ "Repopulate"+str(i)+".json", 'r')
                lines = f.readlines()[1:]
                json_sid = []
                json_pnt = []
                for line in lines:
                        data_dict[key] = json.loads(line)
                        IsComp = data_dict[key]["IsComplete"]
                        key1 = len(data_dict[key]["points"])
                        #print(key1)
                        points_sid =  data_dict[key]["points"][key1-1]["SID"]
                        points_pn = data_dict[key]["points"][key1-1]["PN"]
                        #print(points_sid)
                        #print(points_pn)
                        json_sid.append(points_sid)
                        json_pnt.append(points_pn)
                        #print(json_sid)
                        #print(json_pnt)
                        json_sid.append(points_sid)
                        json_pnt.append(points_pn)
                        url_SPDResponse =  "http://192.168.116.205:9001/v1/points/spd" +"?"+ "start=" + str(points_sid)
                        #print(url_SPDResponse)
                        response = requests.get(url_SPDResponse, headers=Headers, verify="ov38.dmz.crt")
                        signal = response.text
                        #print(len(data_dict[key]["points"]))
                        #print(IsComp)
                        #print(IsComp)
                        #if(IsComp == "true"):break                       
                        #else:
                        """
"""                       
                                #var = 4
                                #print(var)
                                #print(len(data_dict[key]["points"]))
                                key1 = len(data_dict[key]["points"])
                                #print(key1)
                                points_sid =  data_dict[key]["points"][key1-1]["SID"]
                                points_pn = data_dict[key]["points"][key1-1]["PN"]
                                #print(points_sid)
                                #print(points_pn)
                                json_sid.append(points_sid)
                                json_pnt.append(points_pn)
                                #print(json_sid)
                                #print(json_pnt)
                                url_SPDResponse =  "http://192.168.116.205:9001/v1/points/spd" +"?"+ "start=" + str(points_sid)
                                print(url_SPDResponse)
                                response = requests.get(url_SPDResponse, headers=Headers, verify="ov38.dmz.crt")
                                signal = response.text
                                #print(type(signal))
                                """
                        #i += 1
"""      
#print(data_dict)
#print(data)


"""









        #i +=1
                #print(data[i])



        #i += 1
        #url_SPDResponse = url_SPDResponse  +"?"+ "start=" + str(points_sid)

                
        

"""
with open(path+ "Repopulate.json", "w") as file:
        file.write("\n")
        file.write(signal)
        file.write("\n")
with open(path+ 'Repopulate.json') as file:
        data = json.load(file)
        #print(json.dumps(data, indent=4, sort_keys= False))
        f = open(path+ "Repopulate.json", 'r')
        lines = f.readlines()[1:]
        json_sid = [] 
        json_pnt = []
        for line in lines:
            data_dict = json.loads(line)
            IsComp = data_dict["IsComplete"]
            #print(IsComp)
            if(IsComp == "True"):
                    break
            else:
                    print(len(data_dict["points"]))
                    points_sid =  data_dict["points"][1999]["SID"]
                    points_pn = data_dict["points"][1999]["PN"]
                    print(points_sid)
                    print(points_pn)
                    json_sid.append(points_sid)
                    json_pnt.append(points_pn)
                    print(json_sid)
                    print(json_pnt)
                    url_SPDResponse = url_SPDResponse  +"?"+ "start=" + str(points_sid)
                    print(url_SPDResponse)
                    response = requests.get(url_SPDResponse, headers=Headers, verify="ov38.dmz.crt")
                    signal1 = response.text
                    with open(path+ "Repopulate1.json", "w") as file:
                            file.write("\n")
                            file.write(signal1)
                            file.write("\n")
                    with open(path+ 'Repopulate1.json') as file:
                            data1 = json.load(file)
                            f = open(path+ "Repopulate1.json", 'r')
                            lines = f.readlines()[1:]
                            for line in lines:
                                    data_dict1 = json.loads(line)
                                    IsComp1 = data_dict1["IsComplete"]
                                    if(IsComp1 == "True"):
                                            break
                                    else:
                                            print(len(data_dict1["points"]))
                                            points_sid1 =  data_dict1["points"][1999]["SID"]
                                            points_pn1 = data_dict1["points"][1999]["PN"]
                                            print(points_sid1)
                                            print(points_pn1)
"""













"""
response = requests.get(url_SPDResponse1, headers=Headers, verify="ov38.dmz.crt")
signal1 = response.text
#print(type(signal1))
with open(path+ "Repopulate.json", "a+") as file:
        file.write("\n")
        file.write(signal1)
        file.write("\n")
"""
"""
with open(path+ 'Repopulate.json') as file:
        data1 = json.load(file)
        #print(json.dumps(data, indent=4, sort_keys= False))
        f = open(path+ "Repopulate.json", 'r')
        lines = f.readlines()[1:]
        json_sid1 = [] 
        json_pnt1 = []
        for line in lines:
            data_dict = json.loads(line)
            points_sid1 =  data_dict["points"][0]["SID"]
            points_pn1 = data_dict["points"][0]["PN"]
            print(points_sid1)
            print(points_pn1)
            print(len(data_dict["points"]))
            json_sid.append(points_sid1)
            json_pnt.append(points_pn1)
        print(json_sid1)
        print(json_pnt1)
url_SPDResponse2 =  "http://192.168.116.205:9001/v1/points/spd" +"?"+ "start=" + str(points_sid1)
print(url_SPDResponse2)
"""

        #for sid in data:
            #if(IsComplete == "false"):
                #sid = data["points"]["SID"]
                #print(sid)

           
        #for Repo in data

#if(IsComplete == "false")
"""


#for dump in data:
    #print(dump['SID'])

    #print(json.dumps(data, indent=4, sort_keys= False))

    #print(data)
    #data1 = f.readlines()
   # print(data1)
"""

