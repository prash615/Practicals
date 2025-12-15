import json

students = {
    'student1': {'roll': 101, 'name': 'John', 'percent': 80.5, 'sports': False},
    'student2': {'roll': 102, 'name': 'Carol', 'percent': 80.5, 'sports': False},
    'student3': {'roll': 103, 'name': 'Alice', 'percent': 50.5, 'sports': False}
}

print(students)
print(type(students))

#dump()

# with open("student_data.json", "w") as fh:
#     json.dump(students, fh, indent=4)
#
# #load()
#
# with open("student_data.json", "r") as fh:
#     data = json.load(fh)
#
# print(data)
# print(type(data))

# update()
# read the old data first

with open("student_data.json" , "r") as fh:
    data = json.load(fh)

# update operation
data.update(students)

#dump date into json

with open("student_data.json", "w") as fh:
    json.dump(data, fh, indent=4)