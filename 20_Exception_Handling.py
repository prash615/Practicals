try:
    with open("file1.txt", "rt") as gf:
        data = gf.readline()

except FileNotFoundError as file_err:
    print("File not exist")
    print(file_err)
else:
    print(data)
