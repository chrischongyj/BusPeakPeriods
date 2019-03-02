import requests

headers = { 'AccountKey': 'FP9dZIa6Tm6EsGeQWGRGOQ==', 
            'accept': 'application/json',
            'BusStopCode': '43289'}

target = 'http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2'

request = requests.get(target, params = headers)

print(request.text)