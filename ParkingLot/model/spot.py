class ParkingSpot:
    def __init__(self, lvl, spot_no, spot_size):
        self.level = lvl
        self.spot_number = spot_no
        self.spot_size = spot_size
        self.vehicle = None


    def __str__(self) -> str:
        return f"floor: {self.level.name}, spot_no: {self.spot_number}, size: {self.spot_size}, v: {self.vehicle.vehicle_no if self.vehicle else None}"


    def get_spot_number(self):
        return self.spot_number


    def get_size(self):
        return self.spot_size


    def get_my_level(self):
        return self.level.name


    def is_available(self):
        return self.vehicle is None


    def can_fit_vehicle(self, vehicle):
        return self.is_available() and vehicle.can_fit_in_spot(self)


    def park(self, vehicle):
        if not self.can_fit_vehicle(vehicle):
            return False

        self.vehicle = vehicle
        self.vehicle.park_in_spot(self)
        return True


    def remove_vehicle(self):
        """
        Remove vehicle from spot and notify level that a new spot is available
        """
        self.level.spot_freed()
        self.vehicle = None
