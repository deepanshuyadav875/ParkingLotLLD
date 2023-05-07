from abc import ABC, abstractmethod
from .vehicle_size import VehicleSize

class Vehicle(ABC):
    def __init__(self, vehicle_no):
        self.parking_spots = []
        self.vehicle_no = vehicle_no
        self.spots_needed = 0
        self.size = None


    def get_my_spot(self):
        return ''.join([str(spot.spot_number) for spot in self.parking_spots])


    def get_my_spot_level(self):
        return self.parking_spots[0].level.name if self.parking_spots else None


    def get_spots_needed(self):
        return self.spots_needed


    def get_size(self):
        return self.size


    def park_in_spot(self, spot):
        self.parking_spots.append(spot)


    def clear_spots(self):
        for spot in self.parking_spots:
            spot.remove_vehicle()

        self.parking_spots = []  


    @abstractmethod
    def can_fit_in_spot(self, spot):
        pass


    @abstractmethod
    def print_me(self):
        pass


class AnySizeVehicle(Vehicle):
    def __init__(self, vehicle_no):
        Vehicle.__init__(self, vehicle_no)
        self.spots_needed = 1
        self.size = VehicleSize.Single


    def can_fit_in_spot(self, spot):
        return spot.get_size() == self.size


    def print_me(self):
        spots = ''.join([f"spot_no: {str(spot.spot_number)}, L: {spot.level.name}" for spot in self.parking_spots])
        print(f"\033[94m{self.vehicle_no} at {spots} \033[00m")
