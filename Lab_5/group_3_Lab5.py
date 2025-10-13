import pdfplumber
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
    for line in nested_list_raw_data:
        i = 0
        while i < len(line):
            if (line[i] == "-" or line[i] == "x" or line[i] == "y" or line[i] == "v" or line[i] == "x,y" or line[i] == "v,x,y" or line[i] == "**"):
                line.pop(i)
                
                temp_row_data = []
                if (i == 2):
                    temp_row_data.extend(line[1], "Child labour (%) 2005-2012", line [i])
                    nested_list_cleaned_data.append(temp_row_data)
                if (i == 5):
                    temp_row_data.extend(line[1], "Child marriage (%) 2005-2012_married by 15", line [i])
                    nested_list_cleaned_data.append(temp_row_data)
                if (i == 6):
                    temp_row_data.extend(line[1], "Child marriage (%) 2005-2012_married by 18", line [i])
                    nested_list_cleaned_data.append(temp_row_data)
                if (i == 7):
                    temp_row_data.extend(line[1], "Birth registration (%) 2005-2012", line [i])
                    nested_list_cleaned_data.append(temp_row_data)
                if (i == 8):
                    temp_row_data.extend(line[1], "Female genital mutilation/cutting (%) 2002-2012_prevalence_women", line [i])
                    nested_list_cleaned_data.append(temp_row_data)
                if (i == 9):
                    temp_row_data.extend(line[1], "Female genital mutilation/cutting (%) 2002-2012_prevalence_girls", line [i])
                    nested_list_cleaned_data.append(temp_row_data)
                if (i == 10):
                    temp_row_data.extend(line[1], "Female genital mutilation/cutting (%) 2002-2012_attitudes", line [i])
                    nested_list_cleaned_data.append(temp_row_data)
                if (i == 11):
                    temp_row_data.extend(line[1], "Justification of wife beating (%) 2005-2012_male", line [i])
                    nested_list_cleaned_data.append(temp_row_data)
                if (i == 12):
                    temp_row_data.extend(line[1], "Justification of wife beating (%) 2005-2012_female", line [i])
                    nested_list_cleaned_data.append(temp_row_data)
                if (i == 13):
                    temp_row_data.extend(line[1], "Violent Discipline (%) 2005-2012", line [i])
                    nested_list_cleaned_data.append(temp_row_data)


with open("..\Group_3_Lab5\group_3_Lab5.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(nested_list_cleaned_data)
