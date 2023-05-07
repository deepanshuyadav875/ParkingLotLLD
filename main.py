from ParkingLot.service.parking_lot import ParkingLotService
from ParkingLot.model.vehicle import AnySizeVehicle


def perform_parking(parking_lot, vehicle_number):
    print("\033[97m \n_ PARKING REQUEST_\033[00m")
    vehicle = AnySizeVehicle(vehicle_number) # create a new vehicle with unique `vehicle_number`
    parked_msg = ParkingLotService.park_vehicle(parking_lot, vehicle) # park the above created vehicle in the lot
    print(parked_msg)
    vehicle.print_me() # view the vehicle current status
    return vehicle


def perform_unparking(parking_lot, vehicle):
    print("\033[97m \n_ UNPARKING REQUEST_\033[00m")
    print("Before unparking -> ")
    vehicle.print_me() # view the vehicle current status
    msg = ParkingLotService.unpark_vehicle(parking_lot, vehicle)
    print(msg)
    print("After unparking -> ")
    vehicle.print_me()
    return vehicle

def get_vehicle_spot_in_lot(parking_lot, vehicle_no):
    vehicle_pos = ParkingLotService.find_vehicle(lot, vehicle_no)
    print(f"\nspot position for vehicle {vehicle_no}: {vehicle_pos}")
    return vehicle_pos


if __name__ == '__main__':
    lvl_count = 2
    lvl_capacity = 20
    lot_name = 'Only Parking Lot in the city'

    # first creating a parking lot
    lot = ParkingLotService.create_parking_lot(
        parking_lot_name=lot_name,
        level_count=lvl_count,
        each_level_capacity=lvl_capacity
    )

    if lot:
        vehicles = []
        # park and unpark vehicles in a range
        for i in range(1, 56):
            print(f"\n######### New vehicle, entry_no:{i} #############\n")

            vehicle = perform_parking(lot, f'vehicle-{str(i)}')
            vehicles.append(vehicle)

            if i%5 == 0:
                # unpark the vehicle if it comes at the `entry_no` where `entry_no` is a multiple of 5(only for testig purpose)
                perform_unparking(lot, vehicle)

        for level in lot.levels:
            level.plot_me() # view every level's current view after parking / unparking of vehicles

        # get the current position of any vehicle in the parking lot by poviding unique vehicle no.
        vehicle_no = vehicles[0].vehicle_no
        get_vehicle_spot_in_lot(lot, vehicle_no)

        vehicle = vehicles[8]
        perform_unparking(lot, vehicle) # unpark request for a previously parked vehicle
        perform_unparking(lot, AnySizeVehicle('vehicle-x')) # unpark request for a vehicle that is not parked in the lot

        perform_parking(lot, 'vehicle-49') # park request for a vehicle which is already parked
        perform_parking(lot, 'vehicle-50') # park request for a new vehicle
        perform_parking(lot, 'vehicle-51') # park request for another vehicle when there is no space available
