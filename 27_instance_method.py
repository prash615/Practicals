class Student:

    def study(self, n_hours):
        print(f"the student studies for {n_hours} hours")

    def sports(self, sport_name):
        print(f"student plays {sport_name}")


student1 = Student()
print(f"the object of{student1}")
student1.study(4)
student1.sports("Cricket")

print("========================")

student2 = Student()
student2.study(5)
student2.sports("Tennis")