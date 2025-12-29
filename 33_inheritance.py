class Vehicle:
    compony = "Prash Motors"

    def __init__(self, n_wheels, n_seats, mileage):
        self.n_wheels = n_wheels
        self.n_seats = n_seats
        self.mileage = mileage

    def get_details(self):
        return f"This vehicle has {self.n_wheels} wheels, {self.n_seats} seats and a mileage of {self.mileage}"

v1 = Vehicle(4, 7, 50)
print(v1.get_details())

class Car(Vehicle):
    model = "BMW M3"

    def __init__(self, car_type, drive_type, wheels, seats, mileage):
        print("Init of Car")
        self.car_type = car_type
        self.drive_type = drive_type
        super().__init__(4, 7, 50)

c1 = Car("SUV", "MANUAL", 4, 4, 25)
print(c1.model)
print(c1.compony)
print(f"Model = {c1.model}")
print(f"Compony = {c1.compony}")
