class ParkingLotError(Exception):
    """Raise for not parking lot errors"""
    
    def __init__(self, mssg=None, *args):
        super().__init__(args)
        if mssg is None:
            mssg = "Currently this parking lot is not taking any request. visit after some time."
        self.mssg = mssg

    def __str__(self):
        return self.mssg
