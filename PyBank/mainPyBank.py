#import modules
import os
import csv

# create the path.  Do I need the os.path.join if its in the same hierarchy?
csv_path = os.path.join("budget_data.csv")

# create a list to store data
date_list = []
num_list = []
rev_change_list = []

# open csv file and use csv.reader method to read file
with open (csv_path, newline="") as raw_budget:
    csvreader = csv.reader(raw_budget, delimiter=",")
    csv_header = next(csvreader)    # skipped header


    for row in csvreader:
        date_list.append(row[0])    # added month/year date to list
       
        integer = int(row[1])       # changing the data type to integer
        num_list.append(integer)
        
    for row in range(1, len(num_list)):
        rev_change_list.append(num_list[row] - num_list[row-1])   
        avg_change = round(sum(rev_change_list)/len(rev_change_list), 2)
        # Need to credit Hetal stack overflow for code lines 29 and 30
        max_rev_change_date = str(date_list[rev_change_list.index(max(rev_change_list))+1])
        min_rev_change_date = str(date_list[rev_change_list.index(min(rev_change_list))+1])
    
    summary = ("Financial Analysis \n" +
                "------------------- \n" +
                "Total Months: " + str(len(date_list)) + "\n" +   # calculates total months
                "Total: $" + str(sum(num_list)) + "\n" +
                "Average Change: $" + str(avg_change) + "\n" +
                "Greatest Increase in Profits: " + str(max_rev_change_date) + "($" + str(max(rev_change_list)) + ") \n" +
                "Greatest Decrease in Profits: " + str(min_rev_change_date) + "($" + str(min(rev_change_list)) + ") \n")

    print(summary)

# write updated data to a text file
dataFile = open ("final_budget_data.txt", "w+")
dataFile.write(summary)
dataFile.close
   
