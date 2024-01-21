# Parking Lot
### Requirements
- Python3
### Project Overview
1: main.py file is starting point of this module,
- It has some default test cases written
- In order to test sample cases (success or failure), run this file usign command python3 main.py

2: Inside the service dir, ParkingLotSerivce class provides the 4 API Methods
- create_parking_lot
- park_vehicle
- unpark_vehicle
- find_vehicle

find the method's descriptions in order to use the same

3: Inside the model dir, 4 main model classes are present
- ParkingLot(Singleton Class, as only one Parking Lot is allowed in this service)
- Level
- Spot
- Vehicle(Abstract Class), AnySizeVehicle(child class of Vehicle, it just handles with all size of vehicles)
