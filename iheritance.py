# opp 

class Car :
    def __init__(self):
        self.wheel = 4
        self.seat = 5

    def drive(self):
        print("Driving a car ")

class SportCar(Car):
    def __init__(self):
        super().__init__()

        self.engine = "400 HP"
        self.seats = 3
    def drive(Car):
        print("Drive a sport car ...")



mySportCar = SportCar()
mySportCar.drive()



# 
