from flask import Flask
import requests

app = Flask(__name__)

microservice_url = "http://127.0.0.1:3001/lookup_vehicle/"

vehicles = []
vins = ['2T1AE00E9PC017543', '1JCWX77M0G0015078', '1FDZU90V2TVA26792']

for vin in vins:
    vehicle_info = requests.get(microservice_url+vin).json()
    vehicles.append(vehicle_info)

print(vehicles)

if __name__ == '__main__':
    app.run(port=3000)