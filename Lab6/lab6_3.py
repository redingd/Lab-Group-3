# Submit a Single Python Script: The script should include both functions for Parts 1 and 2.
# Menu Interface: Create a simple menu in the script that allows users to:
# Select either Part 1 (Data Merging) or Part 2 (Data Cleaning).
# Run the selected function.

# All #_SAT_Dataset.csv files are for part 1, the rest are for part 2

# for part 2, there are two csv files needed which are both in a zip file linked in the assignment instructions on canvas
# One of the files (rotten_tomatoes_critic_reviews.csv) is too large to import into GitHub, so only one of them (rotten_tomatoes_movies.csv) is currently in the folder for this lab
# Whoever submits the assignment will need to make sure that they include the other csv file that is 220 MB

import csv
import pandas as pd

part_num = int(input("Enter 1 for part 1 and 2 for part 2"))

def part_1():
    filename1 = "./Best_Colleges_SAT_Dataset.csv"
    filename2 = "./Prep_Scholar_SAT_Dataset.csv"
    filename3 = "./Princeton_Review_SAT_Dataset.csv"

    # read the files, put them into a nested list
    file1 = open(filename1)
    f1 = csv.reader(file1)
    list1 = []
    for row in f1:
        list1.append(row)
    # create a dataframe out of the list
    pd1 = pd.DataFrame(list1)
    # make the column names the first row of the csv file
    pd1.columns = list1[0]
    # drop the now duplicated first actual row of the df
    pd1.drop([0], inplace=True)

    # similar process for other 2 input files
    file2 = open(filename2)
    f2 = csv.reader(file2)
    list2 = []
    for row in f2:
        list2.append(row)
    pd2 = pd.DataFrame(list2)
    pd2.columns = list2[0]
    pd2.drop([0], inplace=True)

    file3 = open(filename3)
    f3 = csv.reader(file3)
    list3 = []
    for row in f3:
        list3.append(row)
    pd3 = pd.DataFrame(list3)
    pd3.columns = list3[0]
    pd3.drop([0], inplace=True)

    # outer join of first 2 dataframes to make a new one
    merged_1_and_2 = pd.merge(pd1, pd2, on='State', how="outer")
    # outer join of first 2 df and 3rd one
    merged_all = pd.merge(merged_1_and_2, pd3, on="State", how="outer")
    merged_all.to_csv("./merged_sat_stats.csv")
    file1.close()
    file2.close()
    file3.close()


def part_2():
    # creating pandas dataframes out of csv files
    movies_df = pd.read_csv("./rotten_tomatoes_movies.csv")
    reviews_df = pd.read_csv("./rotten_tomatoes_critic_reviews.csv")

    # print number of features and observations before data cleaning
    movie_counter = 0
    review_counter = 0
    for row in movies_df.iterrows():
        movie_counter += 1
    for row in reviews_df.iterrows():
        review_counter += 1
    print("Number of Features (before cleaning): " + str(movie_counter - 1)) # subtract 1 to account for header
    print("Number of Observations (before cleaning): " + str(review_counter - 1))

    # removing duplicates from reviews because it has them (movies does not have them)
    reviews_df.drop_duplicates(inplace=True)

    # dropping columns with a high number of empty values
    movies_df.drop(columns=["critics_consensus"], inplace=True)
    reviews_df.drop(columns=["review_score"], inplace=True)

    # 12717 to drop an unset row (round midnight)
    list_rows_movies_to_drop = [12717]

    # looping through rows to get amounts of null values in them: if more than 30% of values are null, the row is removed
    for index, row in movies_df.iterrows():
        a = movies_df.loc[index].isnull().sum()
        if a >= 7:
            list_rows_movies_to_drop.append(index)
    movies_df.drop(list_rows_movies_to_drop, inplace=True)

    # 10701 to drop an unset row (unborn, reviewed by tom meek)
    list_rows_reviews_to_drop = [10701]

    # looping through rows to get amounts of null values in them: if more than 30% of values are null, the row is removed
    for index, row in reviews_df.iterrows():
        b = reviews_df.loc[index].isnull().sum()
        if b >= 2:
            list_rows_reviews_to_drop.append(index)
    reviews_df.drop(list_rows_reviews_to_drop, inplace=True)

    # print number of features and observations after data cleaning
    # first, reset counters
    movie_counter = 0
    review_counter = 0
    for row in movies_df.iterrows():
        movie_counter += 1
    for row in reviews_df.iterrows():
        review_counter += 1
    print("Number of Features (after cleaning): " + str(movie_counter - 1)) # subtract 1 to account for header
    print("Number of Observations (after cleaning): " + str(review_counter - 1))

    # merge the files, put into new csv file
    merged_files = pd.merge(movies_df, reviews_df, on='rotten_tomatoes_link', how="outer")
    merged_files.to_csv("./lab6_group3_cleaned.csv")


def choose_part(num):
    if num == 1:
        part_1()
    elif num == 2:
        part_2()
    else:
        print("Invalid input")

choose_part(part_num)




