from collections import defaultdict
from .singleton import SingletonMeta
from .level import Level
from ..exceptions import ParkingLotError
from ..utils import get_level_name
from .. import constants


class ParkingLot(metaclass=SingletonMeta):
    """
    Singleton Class `ParkingLot`
    Multiple instance creation is not allowed for a Parking Lot
    Only a single `ParkingLot` is allowed in this service
    """
    def __init__(self, name, no_of_levels:int, level_capacity:int):
        """
        name: name of parking lot
        no_of_levels: no. of levels(floors) parking lot contains
        level_capacity: no. of spots each level contains
        """
        assert no_of_levels > 0, constants.ERROR_MSG_LEVEL_COUNT_LESS_THAN_ZERO
        assert level_capacity > 0, constants.ERROR_MSG_LEVEL_CAPACITY_LESS_THAN_ZERO

        self.levels = []
        self.name = name
        self.no_of_lvl = no_of_levels
        self.lvl_capacity = level_capacity
        self.vehicle_map = defaultdict(dict)

        self.__build_lot()


    def __build_lot(self):
        first_spot_no = 1
        for level_no in range(1, self.no_of_lvl + 1):
            self.levels.append(Level(level_no, get_level_name(level_no), self.lvl_capacity, first_spot_no))
            first_spot_no = level_no*self.lvl_capacity + 1


    def park_vehicle(self, vehicle):
        """
        Park the vehicle in a spot (or multiple spots)
        Return false if failed
        After parking successfully add the vehicle in vehicle map
        """
        if vehicle.vehicle_no in self.vehicle_map:
            raise ParkingLotError(constants.ERROR_MSG_DUPLICATE_VEHICLE_PARKING_REQUEST.format(vehicle.vehicle_no))

        for level in self.levels:
            if level.park_vehicle(vehicle):
                vehicle_spots = vehicle.get_my_spot()
                vehicle_level = vehicle.get_my_spot_level()
                self.vehicle_map[vehicle.vehicle_no] = {'level':vehicle_level, 'spot':vehicle_spots}
                return True
        return False


    def unpark_vehicle(self, vehicle):
        """
        Unpark the vehicle and free the spot(s)
        After unparking remove the vehicle from vehicle map
        """
        if vehicle.vehicle_no not in self.vehicle_map:
            raise ParkingLotError(constants.ERROR_MSG_VEHICLE_NOT_PRESENT_IN_LOT.format(vehicle.vehicle_no))

        vehicle.clear_spots()
        if vehicle.vehicle_no in self.vehicle_map:
            del self.vehicle_map[vehicle.vehicle_no]


    def get_vehicle_spot(self, vehicle_no):
        """
        take the vehicle number and provide the vehicle spot and level
        """
        if vehicle_no not in self.vehicle_map:
            raise ParkingLotError(constants.ERROR_MSG_VEHICLE_NOT_PRESENT_IN_LOT.format(vehicle_no))

        return self.vehicle_map[vehicle_no]
