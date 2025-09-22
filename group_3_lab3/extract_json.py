import json
import csv

# denote which keys will be extracted from the json file
keys_to_extract = ['organizationid', 'GradeLevel', 'Test', 'Orglevel', 'organizationname', 'SchoolYear']
#keys_to_extract = ['data' == [[8,9,10,11,12,13]]] # this was in an effort to try and get line 32 to work, decided to just comment out

# load json file
with open('./data/raw/20222023.json', 'r', encoding = 'utf-8') as json_file:
    jsonData = json.load(json_file)

# write to csv file
with open('./data/processed/2023.csv', 'w', newline = '', encoding = 'utf-8') as csv_file:
    # create csv file writer
    writer = csv.DictWriter(csv_file, fieldnames = keys_to_extract)
    
    # write header to csv file
    writer.writeheader()
    
    for item in jsonData:
        row = {key: item.get(key, '') for key in keys_to_extract}
        
        writer.writerow(row)