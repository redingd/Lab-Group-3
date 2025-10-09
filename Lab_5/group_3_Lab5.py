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
