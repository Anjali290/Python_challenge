
#----Importa Data
import csv
import os
from datetime import datetime


budget_data_path = os.path.join("PyBank","Resources","budget_data.csv")


#---- Open  & Read Data
with open(budget_data_path,"r") as budget_data:
  
    csvreader = csv.reader(budget_data, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    
#---- Create Variables

    data = []
    total_amount = 0
    total_months = 0
    changes = []
    changes_dates = []
    delta = 0
    first_row = next(csvreader)  
    total_months += 1
    total_amount += int(first_row[1])
    previous_value = int(first_row[1])

 
#----For Loop to calculate months and amount  

    for row in csvreader:
        
        total_months += 1
        total_amount += int(row[1])
        current_value = int(row[1])
        
        delta=current_value-previous_value
        
       
        previous_value = current_value
        changes.append(delta)
        changes_dates.append(row[0])
        


#---- summarize final results       
change_monthly_avg = round(sum(changes)/len(changes),2)
max_changes = max(changes) 
min_changes = min(changes) 

max_changes_index = changes.index(max_changes)
min_changes_index = changes.index(min_changes)


max_dates=changes_dates[max_changes_index]
min_dates=changes_dates[min_changes_index]


#----Print Results
print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {total_months}")
print(f"Total Amount: ${total_amount}")
print(f"Average Change: ${change_monthly_avg}")
print(f"Greatest Increase in Profits:  {max_dates}  (${max_changes})")
print(f"Greatest Decrease in Profits: {min_dates} (${min_changes})")



#----Output file in txt
output_file = os.path.join("PyBank","Analysis","PyBank_results.txt")

with open(output_file, "w") as datafile:
    print("Financial Analysis", file=datafile)
    print("--------------------------------", file=datafile)
    print(f"Total Months: {total_months}", file=datafile)
    print(f"Total Amount: ${total_amount}", file=datafile)
    print(f"Average Change: ${change_monthly_avg}", file=datafile)
    print(f"Greatest Increase in Profits: {max_dates} (${max_changes})", file=datafile)
    print(f"Greatest Decrease in Profits: {min_dates} (${min_changes})", file=datafile)

