# Pybank project
# Modules
import os
import csv
t_count = 0
net_total = 0
profit_loss= []
profit_changes =[]
# Set path for file
csvpath = os.path.join("budget_data.csv")
print("Financial Analysis")
print("---------------------")
# open csv
with open(csvpath, mode='r', encoding='utf') as csvfile:
    # read csv
    csvreader = csv.reader(csvfile, delimiter=',')
    # storing header row
    csv_header = next(csvreader)
    # loop through looking for values
    for row in csvreader:
        t_count += 1
        if row[1] != "Profit/Losses":
            net_total += (int(row[1]))
            profit_loss .append(int(row[1]))
    # print the results
    print("Total Months: ", t_count )
    print("Total: $",net_total)
    # set the variable i
    i = 0
    for i in range(1,len(profit_loss)):
        profit_changes.append(profit_loss[i] - profit_loss[i-1])
    change = round(sum(profit_changes) / len(profit_changes), 2)
    # print results
    print("Average change: $", change)
    print("Greatest increase in profits: $", max(profit_changes))
    print("Greatest Decrease in profits: $", min(profit_changes))
# creating a text file
with open('py_bank.txt', 'w') as f:
    Finacial_analysis=(
        f"\n\nFinancial Analysis\n"
        f"---------------------\n"
        f"Total Months: {t_count}\n"
        f"Total: ${net_total}\n"
        f"Average Change: ${change}\n"
        f"Greatest increase in profits:${max(profit_changes)}\n"
        f"Greatest decrease in profits:${min(profit_changes)}"
    )
    # writing into the file
    f.write(Finacial_analysis)

