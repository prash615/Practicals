import pickle

students = {
            'student1' : {'roll': 101, 'name': 'John', 'percent': 78.5},
            'student2' : {'roll': 101, 'name': 'John', 'percent': 78.5},
            'student3' : {'roll': 101, 'name': 'John', 'percent': 78.5},
            'student4' : {'roll': 101, 'name': 'John', 'percent': 78.5}
            }
print(students)
print(type(students))
print()

# Serialization
with open("students.bin", "bw") as fh:
    for student in students:
        pickle.dump(students[student], fh)

# Deserialization
with open("students.bin", "br") as fh:
    while True:
        try:
           data = pickle.load(fh)
           print(data, type(data))
        except EOFError:
            print("done")
            break

