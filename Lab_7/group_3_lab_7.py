# McKinley did task 3
import requests as rq
import pandas as pd
from bs4 import BeautifulSoup


def task_3():
    # setting up lists to make the df later
    dataset_name = []
    source = []
    description = []
    csv_link = []
    rdf_link = []
    json_link = []
    xml_link = []
    zip_link = []
    html_link = []
    page_count = []

    # parsing pages
    for page in range(1, 6):
        url = f"https://catalog.data.gov/dataset/?q=&sort=views_recent+desc&page={page}"
        webpage = rq.get(url)
        parsed_page = BeautifulSoup(webpage.text, "html.parser")

        # finding all individual datasets for each page
        individual_datasets = parsed_page.find_all("div", {"class": "dataset-content"})

        for dataset in individual_datasets:
            # getting the name of the dataset, many start and end with a newline character, so I'm removing that
            name_of_dataset_outer = dataset.find("h3", class_="dataset-heading")
            name_of_dataset = name_of_dataset_outer.find("a").text
            dataset_name.append(name_of_dataset.replace("\n", ""))

            # getting the source of the dataset, ends with an unnecessary hyphen, so I'm removing that
            srce = dataset.find("p", class_="dataset-organization").text
            source.append(srce.replace("—", ""))

            # the actual words of the description are inside a div inside a div with class "notes"
            description_outer = dataset.find("div", class_="notes")
            description.append(description_outer.find("div").text)

            # checking that there is one or more link and then seeing what type of link it is; if there is no link, then
            # appending an empty string for all link lists so the lists are the same length
            if len(dataset.find_all("ul", class_="dataset-resources unstyled")) >= 1:
                links = dataset.find("ul", class_="dataset-resources unstyled")

                # checking that there is one or more csv link and appending that, if not appending an empty string so all
                # lists are the same length, similar process for all the other links
                if len(links.find_all("a", attrs={"data-format": "csv"})) >= 1:
                    csv_link.append(links.find("a", attrs={"data-format": "csv"}).attrs.get("href"))
                else:
                    csv_link.append("")

                if len(links.find_all("a", attrs={"data-format": "rdf"})) >= 1:
                    rdf_link.append(links.find("a", attrs={"data-format": "rdf"}).attrs.get("href"))
                else:
                    rdf_link.append("")

                if len(links.find_all("a", attrs={"data-format": "json"})) >= 1:
                    json_link.append(links.find("a", attrs={"data-format": "json"}).attrs.get("href"))
                else:
                    json_link.append("")

                if len(links.find_all("a", attrs={"data-format": "xml"})) >= 1:
                    xml_link.append(links.find("a", attrs={"data-format": "xml"}).attrs.get("href"))
                else:
                    xml_link.append("")

                if len(links.find_all("a", attrs={"data-format": "zip"})) >= 1:
                    zip_link.append(links.find("a", attrs={"data-format": "zip"}).attrs.get("href"))
                else:
                    zip_link.append("")

                if len(links.find_all("a", attrs={"data-format": "html"})) >= 1:
                    html_link.append(links.find("a", attrs={"data-format": "html"}).attrs.get("href"))
                else:
                    html_link.append("")
            else:
                csv_link.append("")
                rdf_link.append("")
                json_link.append("")
                xml_link.append("")
                zip_link.append("")
                html_link.append("")
            # making the page count list
            page_count.append(page)
    # making the data into a dictionary, where the values are lists
    data = {"dataset_name": dataset_name, "source": source, "description": description, "csv_link": csv_link,
            "rdf_link": rdf_link, "json_link": json_link, "xml_link": xml_link, "zip_link": zip_link,
            "html_link": html_link, "page_count": page_count}
    # making the dictionary into a dataframe, and then into a csv file
    df = pd.DataFrame(data)
    df.to_csv("./group_3_task3.csv")
    rows, cols = df.shape
    print(f"The number of rows is: {rows}, and the number of columns is: {cols}")
