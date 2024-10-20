class Vehicle():
    def __init__(self, Name, MaxSpeed, Mileage):
        self.Name = Name
        self.MaxSpeed = MaxSpeed
        self.Mileage = Mileage
    
    def ride(self):
        print("Lets begin with a wonderful journey")

class Buss(Vehicle):
    def __init__(self, Name, MaxSpeed, Mileage, Type):
        self.Type = Type

        Vehicle.__init__(self, Name, MaxSpeed, Mileage)

obj = Buss("Toyota", 50, 25, "V.I.P")
obj.ride()
print(obj.Name, obj.MaxSpeed, obj.Mileage, obj.Type)
