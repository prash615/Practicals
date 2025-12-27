class Student:

    college_name = "ABC College"
    departments = ["CE", "MECH", "CIVIL"]

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        print(f"Calling the Initializer {self}")

    def study(self, n_hours):
        print(f"the student studies for {n_hours} hours")

    def sports(self, sport_name):
        print(f"student plays {sport_name}")

student1 = Student("Parsh", 1001)