import csv

with open('IPA.csv', 'r') as f:
    reader = csv.reader(f)
    rows = [row for row in reader]

new_rows = []
for row in rows:
    new_first_column = row[0][:-1] # remove last character from first column
    new_row = [new_first_column] + row[1:]
    new_rows.append(new_row)

with open('new_file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(new_rows)