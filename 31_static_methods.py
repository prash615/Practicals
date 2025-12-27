"""
Static method - method defined inside a class which is neither bound to the object nor to the class
To create a static method, we use staticmethod decorator
"""

class Student:

    college_name = "ABC College"
    departments = ["CE", "MECH", "CIVIL"]

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        print(f"Calling the Initializer {self}")

    def study(self, n_hours):
        print(self)
        print(f"the student studies for {n_hours} hours")

    def sports(self, sport_name):
        print(f"student plays {sport_name}")

    @staticmethod
    def greet():
        print("Welcome to the college")

    @classmethod
    def get_departments(cls):
        print(f"Departments in {cls.college_name} are:")
        for department in cls.departments:
            print(cls.departments)