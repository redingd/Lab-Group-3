import csv
# 2022 was the XML file, 2023 was the JSON file, and 2024 was the CSV file
inputs = ["./data/processed/2022.csv", "./data/processed/2023.csv", "./data/processed/2024.csv"]
# header could have also been made with a loop
header = ['organizationid', 'gradelevel', 'test', 'orglevel', 'organizationame', 'schoolyear', 'source']

# doing what would normally happen once to read and write a csv file 3 times for the 3 different files being combined to
# get the source column right
with (open(inputs[0], 'r', newline='') as file0,
      open(inputs[1], 'r', newline='') as file1,
      open(inputs[2], 'r', newline='') as file2,
      open("./data/final/merge.csv", 'w', newline='') as output_file):
    reader0 = csv.reader(file0)
    reader1 = csv.reader(file1)
    reader2 = csv.reader(file2)
    writer = csv.writer(output_file)

    # I don't want the header being printed multiple times from the individual csv files all having a header, so this
    # should ignore the first row of each file, which is the header
    writer.writerow(header)
    ignore_header0 = next(reader0)
    ignore_header1 = next(reader1)
    ignore_header2 = next(reader2)

    # actually writing the merged csv file
    for row in reader0:
        line = row + ['2022.csv']
        writer.writerow(line)
    for row in reader1:
        line = row + ['2023.csv']
        writer.writerow(line)
    for row in reader2:
        line = row + ['2024.csv']
        writer.writerow(line)
# this doesn't need to be closed because I used with open
