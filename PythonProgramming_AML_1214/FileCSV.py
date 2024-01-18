import csv
row1 = ['Krina', 20]
row2 = ['Deep', 25]
with open('names.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(row1)
    writer.writerow(row2)

with open('names.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
