from flask import Flask
import requests

app = Flask(__name__)

@app.route("/lookup_vehicle/<vin>")
def lookup_vehicle(vin):
    vehicle_info = {}
    url = f'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVin/{vin}?format=json'
    vehicle = requests.get(url)
    
    if vehicle.status_code == 200:
        vehicle = vehicle.json()
        try:
            vehicle_info['make'] = vehicle['Results'][7]['Value'].lower().capitalize()
            vehicle_info['model'] = vehicle['Results'][9]['Value'].lower().capitalize()
            vehicle_info['year'] = int(vehicle['Results'][10]['Value'])
        except:
            print('Vehicle information not found')
        finally:    
            return vehicle_info
    else:
        print('Unsuccessful request')
        return vehicle_info

if __name__ == '__main__':
    app.run(port=3001)