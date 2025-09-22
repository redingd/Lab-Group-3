David wrote the CSV to CSV and JSON to CSV extractors. McKinley found the datasets, wrote the XML to CSV extractors, wrote the merged CSV, and wrote part of the report.

At one point in her life, my mother taught English to students in Hawaii, and I have a couple friends who have English as a second language, so I was curious what it was like on the administrative side of teaching English to children. 
I liked that the datasets were not terribly big, and had very similar columns, but still had different values from each other.

The columns I decided to keep were the organizationid, gradelevel, test, orglevel, organizationname, and schoolyear columns.  I kept these columns because they are columns the files all have in common and are in the same order.

I merged the files by doing what you would normally do to read a CSV file 3 times, but with one writer to make one file. I didn't think there should be headers within the new CSV file, just one header at the top, so I removed the headers that would have been unnecessary with next(reader). There is probably a much more efficient way to combine all of these files, likely involving more loops than I used, but this was the simplest way I could think of to combine them.

To run the scripts, you will need a structure very similar to the one pictured in the lab description document for this lab. There will be a data folder, that will eventually contain three other folders: one that holds the raw data, one that holds the processed data, and one that holds the final CSV data. All of the scripts used for extraction and the script used to merge all the processed CSV files are outside of this folder, but are not contained in their own folder. The scripts for extraction will need to be run before the script to merge all the files.


Name, Source, Format, Number of records, Fields

Report Card English Learner Assessment Data 2022-23 School Year, https://catalog.data.gov/dataset/report-card-english-learner-assessment-data-2022-23-school-year ,XML, 14171, 15                      
                  
Report Card English Learner Assessment Data 2023-24 School Year, https://catalog.data.gov/dataset/report-card-english-learner-assessment-data-2023-24-school-year ,JSON, 14258, 15                    
                  

Report Card English Learner Assessment Data 2024-25 School Year, https://catalog.data.gov/dataset/report-card-english-learner-assessment-data-2024-25-school-year ,CSV, 17912, 15
                  



