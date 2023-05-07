from .vehicle import VehicleSize
from .spot import ParkingSpot

class Level:
    def __init__(self, floor_no, floor_lable, no_of_spots, first_spot_no):
        self.floor_no = floor_no
        self.name = floor_lable
        self.no_of_spots = no_of_spots
        self.available_spots = no_of_spots
        self.spot_starting_at = first_spot_no
        self.spots = []

        self.__build_level()


    def __build_level(self):
        start = self.spot_starting_at
        end = start + self.no_of_spots
        for spot_no in range(start, end):
            self.spots.append(ParkingSpot(self, spot_no, VehicleSize.Single))


    def plot_me(self):
        print(f"\nspots at {self.name}")
        for spot in self.spots:
            print(f"\033[96m {spot}\033[00m")


    def spot_freed(self):
        self.available_spots += 1


    def get_available_spots(self):
        return self.available_spots


    def park_vehicle(self, vehicle):
        if self.get_available_spots() <= 0:
            return False

        spot_num = self.find_available_spots(vehicle)

        return False if spot_num < 0 else self.park_starting_at_spot(spot_num, vehicle)


    def find_available_spots(self, vehicle):
        """
        Strategy for finding the vacant spot for a new vehicle parking
        checks squentially from starting spot position to end positon
        if finds first spot where no vehicle is parked, returns that spot
        if all the spots are filled in this level, returns -1
        """
        for spot_no in range(len(self.spots)):
            spot = self.spots[spot_no]
            if spot.can_fit_vehicle(vehicle):
                return spot_no

        return -1


    def park_starting_at_spot(self, spot_num, vehicle):
        success = self.spots[spot_num].park(vehicle)
        if success:
            self.available_spots -= vehicle.get_spots_needed()
        return success
