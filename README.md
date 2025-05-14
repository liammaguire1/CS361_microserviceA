# Communication Contract

## How to programatically REQUEST data
To request data from the microservice, use the Python requests library or another similar method for making REST API requests.
In the context of a Flask application, this will likely involve making the request within one of the routes for one's application.
Crucially, this request must include the VIN as a string parameter. An example request is included below:

requests.get('http://127.0.0.1:3001/lookup_vehicle/2T1AE00E9PC017543')

## How to programatically RECEIVE data
To receive data from the microservice, simply format the result of the REST API request. I recommend using .json() to format the result.
An example is included below:

vehicle_info = requests.get('http://127.0.0.1:3001/lookup_vehicle/2T1AE00E9PC017543').json()

## UML Diagram
(./"Microservice A UML.vpd")
