# x => for creating file

fh = open("file1.txt", "rt")
content = fh.read(15)
line1 = fh.readline()
print(content)
print(line1)