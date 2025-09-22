import csv

# denote which columns will be extracted from the input csv file, as listed in the header
columns_to_extract = ['organizationid', 'GradeLevel', 'Test', 'Orglevel', 'organizationname', 'SchoolYear']

# open input and output csv files
with (open('./data/raw/20222023.csv', 'r', newline = '', encoding = 'utf-8') as infile,
      open('./data/processed/2024.csv', 'w', newline = '', encoding = 'utf-8') as outfile):

    # create file reader and writer
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames = columns_to_extract)

    # write header to output file
    writer.writeheader()

    # print previously denoted columns (see line 4) from input file to output file
    for row in reader:
        filtered_row = {key: row[key] for key in columns_to_extract}

        writer.writerow(filtered_row)
