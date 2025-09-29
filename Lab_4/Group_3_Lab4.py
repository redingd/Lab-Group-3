"""
CONTRIBUTION STATEMENT
Mckinley wrote the excel file reader and did the data cleaning and organization.
David wrote the csv file writer and row counter, and reorganized the code into functions.
"""


# Per the assignment instructions, we are to only turn in this file, NOT the xlsx sheet

# The columns from the xlsx sheet to be used are: B, E, K, M, O, Q, S, U, W, Y, AA

import openpyxl as xl
import csv

# The conversion process is split acorss three functions, meant to read data from the excel file, clean it, and then write it to the csv file
def Read_Excel_File(Excel_file): # returns an array containing all data read from the excel file
    wkbk = xl.load_workbook(xml_file, read_only = True, data_only = True)
    a = wkbk.worksheets[1]
    data = []
    # MIN_ROW AND MIN_COL ARE 1 INDEXED, NOT 0 INDEXED!
    # only took the ranges of the Excel file I thought I would need
    for row in a.iter_rows(min_row=15, max_row=211, min_col=1, max_col=27, values_only=True):
        row_data = []
        for value in row:
            row_data.append(value)
        data.append(row_data)
    return data

data_for_csv = []
def Clean_Data(data):
    # made a nested list for the csv file to be written from, after cleaning the data. i is the row, j is the column
    # check j to see what column it came from, to see what the category name has to be, then make a nested list out of it
    # to make it easy to make a csv file out of it
    i = 0
    while i < (len(data)):
        j = 0
        while j < (len(data[i])):
            if j == 4 or j == 10 or j == 12 or j == 14 or j == 16 or j == 18 or j == 20 or j == 22 or j == 24 or j == 26:
                if data[i][j] == 0 or data[i][j] == "-" or data[i][j] == "None" or data[i][j] == "–" or data[i][j] == "–" or data[i][j] == "– ":
                    pass
                else:
                    row_data_csv = []
                    if j == 4:
                        row_data_csv.extend([data[i][1], "Child labour (%) 2005-2012", data[i][j]])
                        data_for_csv.append(row_data_csv)
                    if j == 10:
                        row_data_csv.extend([data[i][1],"Child marriage (%) 2005-2012_married by 15" , data[i][j]])
                        data_for_csv.append(row_data_csv)
                    if j == 12:
                        row_data_csv.extend([data[i][1], "Child marriage (%) 2005-2012_married by 18", data[i][j]])
                        data_for_csv.append(row_data_csv)
                    if j == 14:
                        row_data_csv.extend([data[i][1], "Birth registration (%) 2005-2012", data[i][j]])
                        data_for_csv.append(row_data_csv)
                    if j == 16:
                        row_data_csv.extend([data[i][1],
                                          "Female genital mutilation/cutting (%) 2002-2012_prevalence_women",
                                          data[i][j]])
                        data_for_csv.append(row_data_csv)
                    if j == 18:
                        row_data_csv.extend([data[i][1], "Female genital mutilation/cutting (%) 2002-2012_prevalence_girls",
                                             data[i][j]])
                        data_for_csv.append(row_data_csv)
                    if j == 20:
                        row_data_csv.extend([data[i][1], "Female genital mutilation/cutting (%) 2002-2012_attitudes",
                                             data[i][j]])
                        data_for_csv.append(row_data_csv)
                    if j == 22:
                        row_data_csv.extend([data[i][1], "Justification of wife beating (%) 2005-2012_male", data[i][j]])
                        data_for_csv.append(row_data_csv)
                    if j == 24:
                        row_data_csv.extend([data[i][1], "Justification of wife beating (%) 2005-2012_female", data[i][j]])
                        data_for_csv.append(row_data_csv)
                    if j == 26:
                        row_data_csv.extend([data[i][1], "Violent discipline (%) 2005-2012", data[i][j]])
                        data_for_csv.append(row_data_csv)
            j += 1
        i += 1
    return data_for_csv

def Write_CSV_File(data_for_csv, csv_file):
    # Write header
    header = ['Country Name', 'Category Name','Category Total']

    # Write header and data to new CSV file
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(data_for_csv)

    # print number of rows in the new CSV file
    with open(csv_file, 'r', newline = '') as file:
        reader = csv.reader(file)
        row_count = -1 # set at -1 to exclude header
        for row in reader:
            row_count += 1
        print(f"Number of rows in '{csv_file}': {row_count}")


# Call functions to convert the SML file to CSV

excelFileName = './Lab4Data.xlsx'
csvFileName = './redingd1.csv' # instructions said to name the new file your_nku_username.csv
rawData = Read_Excel_File(excelFileName)
cleanData = Clean_Data(rawData)
Write_CSV_File(cleanData, csvFileName)
