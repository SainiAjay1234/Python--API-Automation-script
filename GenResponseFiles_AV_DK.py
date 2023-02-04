import requests
import time

resp = requests.post("https://ov38.com:9191/v1/security/token", data={"username":"Administrator","password":"Welcome@1234"}, verify="DataHubOV38.crt")
Headers = {}
Headers["Authorization"] = "Bearer " + resp.json()["token"]

f = open(r"C:\Users\Administrator\AppData\Local\Programs\Python\Python37\IntegrationTests\app\multiple_points\MultipleUpdatesProgram\PointsFile_24.txt","r")
lines = f.readlines()

mypath = r"C:\Users\Administrator\AppData\Local\Programs\Python\Python37\IntegrationTests\app\multiple_points\MultipleUpdatesProgram\ResponseFiles"

query_points = [point.replace('\n','')+":AV" for point in lines]

for i in range(0, 1200):
    for point in query_points:
        url = "https://ov38.com:9191/v1/live/points?names=" + point
        response = requests.get(url, headers=Headers, verify="DataHubOV38.crt")
        with open(mypath+"\\response_"+ point[0:(len(point)-3)] + ".txt", "a+") as file:
            file.write("\n")
            file.write(response.text)
            
    time.sleep(1)






