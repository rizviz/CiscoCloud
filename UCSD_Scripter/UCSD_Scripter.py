import csv
import requests
import ast

f = open("test.csv", "r")
csv = csv.reader(f, dialect='excel')
csv.next() # skips the header

with open(".secret.txt") as file:
    somewhatSecret = file.read()
    somewhatSecret = ast.literal_eval(somewhatSecret)
    # Note: With statements are a context manager.
    # As such, they do not affect scope.
    # Hence, somewhatSecret is available outside the
    # With statement

headers = {
    'authorization': "Basic YWRtaW46YWRtaW4=",
    'x-cloupia-request-key': somewhatSecret['apikey'],
    'cache-control': "no-cache",
    'postman-token': "0d544a7c-8a76-195f-eb69-404857ad217e"
    }

url = "http://10.0.254.5/app/api/rest"
querystring = {"formatType":"json","opName":"userAPIGetMyLoginProfile","opData":"{}"}
response = requests.request("GET", url, headers=headers, params=querystring)

for row in csv:
    catalogName = row[0]
    vdcName = row[1]
    userID = row[2]
    durationHours = row[3]
    beginTime = row[4]
    quantity = row[5]
    memoryMB = row[6]
    diskGB = row[7]
    cores = row[8]
    estimatedCost = row[9]
    comments = row[10]
    additionalInfo = row[11]
    chargeFrequency = row[12]

    qsDict = {"param0":{"catalogName":catalogName,"vdcName":vdcName,"userID":userID,"durationHours":durationHours,"beginTime":beginTime,"quantity":quantity,"memoryMB":memoryMB,"diskGB":diskGB,"cores":cores,"estimatedCost":estimatedCost,"comments":comments,"additionalInfo":additionalInfo,"chargeFrequency":chargeFrequency}}

    querystring = '/app/api/rest?formatType=json&opName=userAPIProvisionRequest&opData=' + str(qsDict)

    r = requests.request("GET", url, headers=headers, params=querystring)
    print r.text

f.close()

print "Script completed successfully."

