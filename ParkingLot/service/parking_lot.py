from ..model.parking_lot import ParkingLot
from ..model.vehicle import Vehicle
from ..utils import print_error
from .. import constants


class ParkingLotService:
    def create_parking_lot(*, parking_lot_name:str, level_count:int, each_level_capacity:int):
        """
        API for creation of parking lot 
        """
        try:
            return ParkingLot(parking_lot_name, level_count, each_level_capacity)
        except Exception as e:
            print_error(e)


    def park_vehicle(parking_lot:ParkingLot, vehicle:Vehicle):
        """
        API for parking of vehicle 
        """
        try:
            if parking_lot.park_vehicle(vehicle):
                return constants.SUCCESS_MSG_VEHICLE_PARKED
            return constants.FAILURE_MSG_NO_SPACE_FOR_PARKING
        except Exception as e:
            print_error(e)


    def unpark_vehicle(parking_lot:ParkingLot, vehicle:Vehicle):
        """
        API for unparking of vehicle 
        """
        try:
            parking_lot.unpark_vehicle(vehicle)
            return constants.SUCCESS_MSG_VEHICLE_UNPARKED
        except Exception as e:
            print_error(e)


    def find_vehicle(parking_lot:ParkingLot, vehicle_no:str):
        """
        API for getting the spot of vehicle 
        """
        try:
            return parking_lot.get_vehicle_spot(vehicle_no)
        except Exception as e:
            print_error(e)
