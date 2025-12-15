# filter (fun, sequence)

seq = [1, 2, 3, 4, 5, 6, 7]
filtered_output = filter (lambda x: True if x % 2 != 0 else False, seq)
print(f"filtered output is : {list(filtered_output)}")

mapped_output = map(lambda x: x ** 2, seq)
print(f"mapped output is : {tuple(mapped_output)}")