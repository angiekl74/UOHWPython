import os
import csv

csv_path = os.path.join("election_data.csv")

candidates = {}

with open(csv_path, newline="") as raw_poll:
    csvreader = csv.reader(raw_poll, delimiter=",")
    csv_header = next(csvreader)

    total_votes = 0

    for row in csvreader:
        
        total_votes += 1

        try:
        # if candidates[row[2]]:
            candidates[row[2]] +=1
        except:
            candidates[row[2]] = 1

    print(candidates)        
    candidate_names = list(candidates.keys())
    print(candidate_names)
    candidate_votes = list(candidates.values())
    print(candidate_votes)
    
summary = ("Election Results \n" +
            "---------------------------- \n" + 
            "Total Votes: " + str(total_votes) + "\n" +
            "---------------------------- \n")
for x in candidate_names:
    summary += f"{x}: {round(candidates[x]/total_votes * 100, 3)}% ({candidates[x]}) \n" 

    # instead of doing below, do above instead  in a loop:
    # candidate_names[0] + ": " + str(percent_correy) + "% (" + str(total_correy) + ") \n" +
     
summary2 += ("Winner: " + str(max(candidates, key=candidates.get)))	# still my solution, 
											   not Justin’s 
print(summary)
