class Vehicle:
    def __init__(self, speed):
        self.speed = speed
    def move(self):
        print(f"moving at {self.speed}kmph")

class Car(Vehicle):
    def __init__(self, speed, brand):
        super().__init__(speed) 
        self.brand = brand

class ElectricCar(Car):
    def __init__(self, speed, brand, batterycapacity):
        super().__init__(speed, brand) 
        self.batterycapacity = batterycapacity

ec = ElectricCar(speed = '120' , brand = 'tesla' , batterycapacity = '100%')
ec.move()
ec.brand()
ec.batterycapacity()



        