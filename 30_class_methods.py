"""
Class methods are methods defined inside the class that are bound to the class
To create a class method, we use a decorator -> classmethod

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

    @classmethod
    def greet(cls):
        print(cls)
        print("Welcome to the college")

    @classmethod
    def get_departments(cls):
        print(f"Departments in {cls.college_name} are:")
        for department in cls.departments:
            print(cls.departments)

student1 = Student("Prash", 1001)
student1.study(4)
student1.greet()
student1.get_departments()