import os
import csv

csv_path = os.path.join("election_data.csv")

voter_id = []
candidate = []
max_vote = []

with open(csv_path, newline="") as raw_poll:
    csvreader = csv.reader(raw_poll, delimiter=",")
    csv_header = next(csvreader)

    total_khan = 0
    total_correy = 0
    total_li = 0
    total_otooley = 0

    for row in csvreader:
        voter_id.append(row[0])
        total_votes = len(voter_id)

        if row[2] == "Khan":
            total_khan = total_khan + 1
            percent_khan = round(float((total_khan / total_votes)*100),3)
            cand_name_khan = "Khan"
        elif row[2] == "Correy":
            total_correy = total_correy + 1
            percent_correy = round(float((total_correy / total_votes)*100),3)
            cand_name_correy = "Correy"
        elif row[2] == "Li":
            total_li = total_li + 1
            percent_li =  round(float((total_li / total_votes)*100),3)
            cand_name_li = "Li"
        elif row[2] == "O'Tooley":
            total_otooley = total_otooley + 1
            percent_otooley = round((float(total_otooley/total_votes)*100),3)
            cand_name_otooley = "O'Tooley"
            
    max_vote.append(total_khan)
    max_vote.append(total_correy)
    max_vote.append(total_li)
    max_vote.append(total_otooley)
    candidate.append(cand_name_khan)
    candidate.append(cand_name_correy)
    candidate.append(cand_name_li)
    candidate.append(cand_name_otooley)

summary = ("Election Results \n" +
            "---------------------------- \n" + 
            "Total Votes: " + str(total_votes) + "\n" +
            "---------------------------- \n" +
            cand_name_khan + ": " + str(percent_khan) + "% (" + str(total_khan) + ") \n" +
            cand_name_correy + ": " + str(percent_correy) + "% (" + str(total_correy) + ") \n" +
            cand_name_li + ": " + str(percent_li) + "% (" + str(total_li) + ") \n" +
            cand_name_otooley + ": " + str(percent_otooley) + "% (" + str(total_otooley) + ")")

print(summary)    
final_result = dict(zip(candidate, max_vote))
print("Winner: " + str(max(final_result, key=final_result.get)))    # Credit leo022 stack overflow

# write updated data to a text file
dataFile = open("final_poll_data.txt", "w+")
dataFile.write(summary)
dataFile.close


