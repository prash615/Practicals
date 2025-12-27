# initializer method __init__()


class Student:

    def __init__(self, name, roll, dept):
        self.name = name
        self.roll = roll
        self.dept = dept

    def study(self, n_hours):
        print(f"the student studies for {n_hours} hours")

    def sports(self, sport_name):
        print(f"student plays {sport_name}")

student1 = Student("prash", 100, "CE")
student1.study(5)
student1.sports("Cricket")
print(student1.name, student1.roll, student1.dept)
print(student1.__dict__)

student2 = Student("Rohan", 1001, "MECH")
student2.study(4)
student2.sports("Tennis")
print(student2.name, student2.roll, student2.dept)
print(student2.__dict__)