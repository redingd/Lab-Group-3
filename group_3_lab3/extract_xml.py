import xml.etree.ElementTree as ET
import csv


filename = "./data/raw/20222023.xml"
tree = ET.parse(filename)
root = tree.getroot()

# getting data by element with a nested loop to only get the text of some elements
rows = []
i = 0
while i < 14170:
    j = 0
    row = []
    while j < 6:
        row.insert(j, root[0][i][j].text)
        j += 1
    rows.insert(i, row)
    i += 1

# made the header; could have also made the header with a loop
header = ['organizationid', 'gradelevel', 'test', 'orglevel', 'organizationame', 'schoolyear']

with open("./data/processed/2022.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerows(rows)
# I don't need to close csvfile because I used with open
