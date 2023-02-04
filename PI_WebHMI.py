import requests
import json
import os
import time
import sys

resp = requests.post("https://ov38.dmz.com:9191/v1/security/token", data={"username":"Administrator","password":"Welcome@1234"}, verify="ov38.dmz.crt")
Headers = {}
Headers["Authorization"] = "Bearer " + resp.json()["token"]
#print(resp.text)
SID="0x80010F43"
PI_WebHMI =  "https://ov38.dmz.com:9191/v1/hmi/points/value?sids="+SID+"&filter=ALL"
print(PI_WebHMI) 
response = requests.get(PI_WebHMI, headers=Headers, verify="ov38.dmz.crt")
PI_response = response.text
path = r"C:\Users\Admin\AppData\Local\Programs\Python\Python37\IntegrationTests\app\Web HMI Automation\Point Information Web HMI"
with open(path+"html.txt", "w+") as file:
    file.write("\n")
    file.write(response.text)
with open(path+"html.txt", "r") as file:
        lines = file.readlines()[1:]
        keys1 = []
for line in lines:
    PI_data = json.loads(line)
    #print(PI_data)
    keys1 = PI_data["Points"][SID]["AV"]
    #print(len(PI_data["Points"]))
    print(keys1)


"""
headers = {}
tokenTime = 0

BASE_URL= 'https://ov38.dmz.com:9191'
USER = "Administrator"
PASSWORD = "Welcome@1234"
OUTPUT = "data.csv"

########################################################################################
def getToken():

    global tokenTime 
    global headers

    r = requests.post(BASE_URL + '/v1/security/token',

    #verify is needed to verify certificate for https. Remove for http
    data={"username":USER,"password":PASSWORD}, verify="C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python37\\IntegrationTests\\app\\ov38.dmz.crt")
    headers["Authorization"] = "Bearer " + r.json()["token"]

    tokenTime = time.time()


def getPIData(point):

    urlStr = (BASE_URL + '/v1/web/dashboard?name=pointinfo')
    #verify is needed to verify certificate for https. Remove for http
    r = requests.get(urlStr, headers=headers, verify="C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python37\\IntegrationTests\\app\\ov38.dmz.crt")
    print(r.text)

"""