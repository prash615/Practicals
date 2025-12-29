class Vehicle:
    compony = "Prash Motors"

    def __init__(self, n_wheels, n_seats, mileage):
        self.n_wheels = n_wheels
        self.n_seats = n_seats
        self.mileage = mileage

    def get_details(self):
        return f"This vehicle has {self.n_wheels} wheels, {self.n_seats} seats and a mileage of {self.mileage}"


class Car(Vehicle):
    model = "BMW M3"

    def __init__(self, car_type, drive_type, wheels, seats, mileage):
        print("Init of Car")
        self.car_type = car_type
        self.drive_type = drive_type
        super().__init__(wheels, seats, mileage)

    def display_info(self):
        print(f"Car type {self.car_type} drive type {self.drive_type}")

class ElectricCar(Car):
    def __init__(self, car_type, drive_type, wheels, seats, mileage, battery_capacity, distance_range):
        print("Init of ElectricCar")
        self.battery_capacity = battery_capacity
        self.distance_range = distance_range
        super().__init__(car_type, drive_type, wheels, seats, mileage)

    def charge(self):
        print(f"Charging the to {self.battery_capacity}")

ec1 = ElectricCar("Sedan", "Manual", 4, 5, 35, 100, 400)
print(ec1)
