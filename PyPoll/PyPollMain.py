#-----------------Import file

import csv
import os

election_data_path = os.path.join("PyPoll","Resources","election_data.csv")



#-----------------Open/Read file 

with open(election_data_path,"r") as election_data:
    csvreader = csv.reader(election_data,delimiter=",")
    csv_header=next(csvreader)

#-----------------Define variables

    votes = []
    candidates_list = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
    
    

    total_votes = 0
    total_votes_cand_1 = 0
    total_votes_cand_2 = 0
    total_votes_cand_3 = 0
    total_votes_cand=0
 

#-----------------For Loop to calculate the # of votes by candiate

    row = 0
    for row in csvreader:

        total_votes += 1        
        candidate = str(row[2])

        if  candidate==candidates_list[0]:
            total_votes_cand_1 += 1
                          
        
        if  candidate==candidates_list[1]:
            total_votes_cand_2 += 1
             

        if  candidate==candidates_list[2]:
            total_votes_cand_3 += 1
            

#-----------------Calculate % and find the Winner

perc_cand1 = round((total_votes_cand_1/total_votes)*100,3)
perc_cand2 = round((total_votes_cand_2/total_votes)*100,3)
perc_cand3 = round((total_votes_cand_3/total_votes)*100,3)

if perc_cand1 > perc_cand2 and perc_cand3:
    win = candidates_list[0]

if perc_cand2 > perc_cand1 and perc_cand3:
    win = candidates_list[1]

if perc_cand3 > perc_cand1 and perc_cand2:
    win = candidates_list[2]

winner = win


#-----------------Print

print("Election Results")
print("---------------------------------------")
print(f"Total Votes: {total_votes}")        
print("---------------------------------------")
print(f"{candidates_list[0]}: {perc_cand1}% ({total_votes_cand_1})")
print(f"{candidates_list[1]}: {perc_cand2}% ({total_votes_cand_2})")
print(f"{candidates_list[2]}: {perc_cand3}% ({total_votes_cand_3})")
print("---------------------------------------")
print(f"Winner: {winner}")
print("---------------------------------------")


#-----------------Outout

output_file = os.path.join("PyPoll","Analysis","PyPoll_results.txt")

with open(output_file, "w") as datafile:
    print("Election Results", file=datafile)
    print("---------------------------------------", file=datafile)
    print(f"Total Votes: {total_votes}", file=datafile)        
    print("---------------------------------------", file=datafile)
    print(f"{candidates_list[0]}: {perc_cand1}% ({total_votes_cand_1})", file=datafile)
    print(f"{candidates_list[1]}: {perc_cand2}% ({total_votes_cand_2})", file=datafile)
    print(f"{candidates_list[2]}: {perc_cand3}% ({total_votes_cand_3})", file=datafile)
    print("---------------------------------------", file=datafile)
    print(f"Winner: {winner}", file=datafile)
    print("---------------------------------------", file=datafile)

   