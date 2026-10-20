import csv

with open("data.csv", "r", newline="") as file: 
    reader = csv.DictReader(file)
    data = list(reader)


print("column name:", reader.fieldnames)
print("Number of records:", len(data))
print('\nRaw dataset:')

for row in data: 
    print(row)
