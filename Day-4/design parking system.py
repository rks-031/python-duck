class ParkingSystem:
    
    def __init__(self, big: int, medium: int, small: int):
        self.m = {}
        self.m[1] = big
        self.m[2] = medium
        self.m[3] = small

    def addCar(self, carType: int) -> bool:
        if self.m[carType] != 0:
            self.m[carType] -= 1
            return True
        else:
            return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)