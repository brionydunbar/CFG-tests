import csv

# create field names
field_names = ["name", "age"]

# create dictionary of key pair values
data = [
    {"name": "Briony", "age": 30},
    {"name": "Emily", "age": 35},
    {"name": "Leo", "age": 32}
]

# create csv file and input data

with open("csvdemo.csv", "w+") as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames = field_names)

    spreadsheet.writeheader()
    spreadsheet.writerows(data) # adds the above data



# reading a spreadsheet
with open("/Users/brionydunbar/Documents/CFGdegree/CFG-tests/python_session5/trees.csv", "r") as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    for row in spreadsheet:
        print(dict(row))