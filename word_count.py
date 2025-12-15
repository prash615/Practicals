countries = ["India", "Aus", "Iran", "Poland", "Ireland"]

counter = 0
output = []

for country in countries:
    if country.startswith("I"):
        counter = counter + 1
        output.append(country)


print(counter)
print(output)
