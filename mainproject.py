import requests
import json

header = { 'AccountKey': 'FP9dZIa6Tm6EsGeQWGRGOQ==', 
            'accept': 'application/json'}

param = {'BusStopCode': '43679'}

target = 'http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2'

request = requests.get(target, params = param, headers = header)

x = json.loads(request.text)

print(json.dumps(x, indent = 2))

for buses in x['Services']:
    print("Service Number " + buses['ServiceNo'],
    "Next Bus 1 = " + buses['NextBus']['Load'],
    "Next Bus 2 = " + buses['NextBus2']['Load'],
    "Next Bus 3 = " + buses['NextBus3']['Load'])



