import pdfplumber
import csv
pdf_filename = "Table9.pdf"

with pdfplumber.open(pdf_filename) as pdf:
    pages = pdf.pages
    # string to hold raw data from pdf, turns into nested list later
    raw_pdf_data = ""

    # adding data to string
    i = 0
    while i < 6:
        raw_pdf_data += (pages[i].extract_text())
        i += 1

    # turning string into one big list
    list_raw_data = raw_pdf_data.split("\n")

    # turning big list into nested list, where each row is mostly one line for actual data
    nested_list_raw_data = []
    for line in list_raw_data:
        temp_row = [line.split(" ")]
        nested_list_raw_data.extend(temp_row)
    
    
    nested_list_cleaned_data = []
    n = 0
    while n < len(nested_list_raw_data):
        # rows  in nested_list_clean_data with usable data: 11-50, 61-100, 112-151, 161-200, 212-251, 262-265
        # skip rows that only include headers, footers, parts of names with no values, and other random text
        if (n < 10) or (n > 49 and n < 60) or (n > 99 and n < 111) or (n > 150 and n < 162) or (n > 199 and n < 211) or (n > 250 and n < 261) or (n > 264) or n == 31 or n == 68 or n == 70 or n == 128 or n == 148 or n == 193 or n == 234 or n == 248:
            pass
        else:
            # first, handle country names. They can at times be multiple words long and therefore need to be condensed into one value in the list
            name = ""

            # three words in one line
            if n == 15 or n == 32 or n == 43 or n == 178 or n == 185 or n == 196 or n == 228 or n == 236 or n == 243:
                name += (nested_list_raw_data[n][0] + " " + nested_list_raw_data[n][1] + " " + nested_list_raw_data[n][2])
                nested_list_raw_data[n].pop(2)
                nested_list_raw_data[n].pop(1)

            # two words in one line
            elif n == 35 or n == 37 or n == 39 or n == 60 or n == 66 or n == 74 or n == 77 or n == 97 or n == 143 or n == 168 or n == 188 or n == 191 or n == 195 or n == 212 or n == 216 or n == 218 or n == 211 or n == 222 or n == 247 or n == 262:
                name += (nested_list_raw_data[n][0] + " " + nested_list_raw_data[n][1])
                nested_list_raw_data[n].pop(1)

            # four words in one line
            elif n == 114 or n == 190:
                name += (nested_list_raw_data[n][0] + " " + nested_list_raw_data[n][1] + " " + nested_list_raw_data[n][2] + " " + nested_list_raw_data[n][3])
                nested_list_raw_data[n].pop(3)
                nested_list_raw_data[n].pop(2)
                nested_list_raw_data[n].pop(1)

            # two lines
            elif n == 31 or n == 68 or n == 70 or n == 128 or n == 148 or n == 193 or n == 232 or n == 246 or n == 261:
                for item in nested_list_raw_data[n-1]: # should be able to handle any number of words in the first line
                    name += (item + " ")

                # some words may be removed from their row to make things work in lines 73-102
                if n == 31 or n == 148 or n == 193 or n == 246 or n == 261: # two words in second line
                    name += (nested_list_raw_data[n][0] + " " + nested_list_raw_data[n][1])
                    nested_list_raw_data[n].pop(1)
                elif n == 68 or n == 70 or n == 232: # three words in second line
                    name += (nested_list_raw_data[n][0] + " " + nested_list_raw_data[n][1] + " " + nested_list_raw_data[n][2])
                    nested_list_raw_data[n].pop(2)
                    nested_list_raw_data[n].pop(1)
                elif n == 128: # one word in second line; no need to remove elements
                    name += (nested_list_raw_data[n][0])

            # one word
            else:
                name += (nested_list_raw_data[n][0])

            i = 1 # skip column 1
            while i < len(nested_list_raw_data[n]):
                # next, take care of non-integers
                if (nested_list_raw_data[n][i] == "–" or nested_list_raw_data[n][i] == "x" or nested_list_raw_data[n][i] == "y" or nested_list_raw_data[n][i] == "v" or nested_list_raw_data[n][i] == "x,y" or nested_list_raw_data[n][i] == "v,x,y" or nested_list_raw_data[n][i] == "**"):
                    pass
                else:
                    temp_row_data = []
                    if (i == 1):
                        temp_row_data.extend([name, "Child labour (%) 2005-2012", nested_list_raw_data[n][i]])
                        nested_list_cleaned_data.append(temp_row_data)
                    elif (i == 4):
                        temp_row_data.extend([name, "Child marriage (%) 2005-2012_married by 15", nested_list_raw_data[n][i]])
                        nested_list_cleaned_data.append(temp_row_data)
                    elif (i == 5):
                        temp_row_data.extend([name, "Child marriage (%) 2005-2012_married by 18", nested_list_raw_data[n][i]])
                        nested_list_cleaned_data.append(temp_row_data)
                    elif (i == 6):
                        temp_row_data.extend([name, "Birth registration (%) 2005-2012", nested_list_raw_data[n][i]])
                        nested_list_cleaned_data.append(temp_row_data)
                    elif (i == 7):
                        temp_row_data.extend([name, "Female genital mutilation/cutting (%) 2002-2012_prevalence_women", nested_list_raw_data[n][i]])
                        nested_list_cleaned_data.append(temp_row_data)
                    elif (i == 8):
                        temp_row_data.extend([name, "Female genital mutilation/cutting (%) 2002-2012_prevalence_girls", nested_list_raw_data[n][i]])
                        nested_list_cleaned_data.append(temp_row_data)
                    elif (i == 9):
                        temp_row_data.extend([name, "Female genital mutilation/cutting (%) 2002-2012_attitudes", nested_list_raw_data[n][i]])
                        nested_list_cleaned_data.append(temp_row_data)
                    elif (i == 10):
                        temp_row_data.extend([name, "Justification of wife beating (%) 2005-2012_male", nested_list_raw_data[n][i]])
                        nested_list_cleaned_data.append(temp_row_data)
                    elif (i == 11):
                        temp_row_data.extend([name, "Justification of wife beating (%) 2005-2012_female", nested_list_raw_data[n][i]])
                        nested_list_cleaned_data.append(temp_row_data)
                    elif (i == 12):
                        temp_row_data.extend([name, "Violent Discipline (%) 2005-2012", nested_list_raw_data[n][i]])
                        nested_list_cleaned_data.append(temp_row_data)
                i += 1
        n += 1


with open("../Group_3_Lab5/group_3_Lab5.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    # line 117 is to see which rows are which index values in nested_list_raw_data
    #writer.writerows(nested_list_raw_data)
    writer.writerows(nested_list_cleaned_data)

# all of the below is for testing purposes
""" 
with open("../Group_3_Lab5/group_3_Lab5.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    count = 0
    for row in reader:
        print(count, " : ", row)
        count += 1
"""
