# Pypoll project
# importing modules
import os
import csv
# set variables
value = 0
count_1 = 0
count_2 = 0
count_3 = 0
# set csv path
csvpath = os.path.join("election_data.csv")
print("Election Results")
print("---------------------")
# open csv
with open(csvpath, encoding='utf') as csvfile:
    # read csv
    csvreader = csv.reader(csvfile, delimiter=',')
    # storing header row
    csv_header = next(csvreader)
    # looping through csvreader
    for row in csvreader:
        value += 1
        if row[2] == "Charles Casper Stockham":
            count_1 += 1
        if row[2] == "Diana DeGette":
            count_2 += 1
        if row[2] == "Raymon Anthony Doane":
            count_3 += 1
    # print results
    print("Total votes: ", value)
    print("---------------------")
    print ("Charles Casper Stockham:", round((count_1/value)*100,3),"%" ,"(",count_1,")")
    print("Diana DeGette:", round((count_2/value)*100,3),"%" ,"(",count_2,")")
    print("Raymon Anthony Doane:", round((count_3/value)*100,3),"%" ,"(",count_3,")")
    print("---------------------")
    dict= {"Charles Casper Stockham": count_1,
           "Diana DeGette": count_2,
           "Raymon Anthony Doane" : count_3
           }
    result = max(dict, key=dict.get)
    print("Winner:" ,result)
    print("---------------------")
    # creating a text file
    with open('py_poll.txt', 'w') as f:
        election_results = (
            f"\n\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {value}\n"
            f"-------------------------\n"
            f"Charles Casper Stockham: {round((count_1/value)*100,3)}% ({count_1})\n"
            f"Diana DeGette: {round((count_2 / value) * 100, 3)}% ({count_2})\n"
            f"Raymon Anthony Doane: {round((count_3 / value) * 100, 3)}% ({count_3})\n"
            f"-------------------------\n"
            f"Winner: {result}\n"
            f"-------------------------\n"
        )
        # writing outputs in text file
        f.write(election_results)
