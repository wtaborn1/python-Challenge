# Pypol
import csv
import os
csvpath = os.path.join("election_data.csv")
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    total_votes=0
    canidates = []
    khan_total = 0
    correy_total = 0
    li_total = 0
    otooley_total = 0
    

    for row in csvreader:
        total_votes = total_votes+1
        if row [2] not in canidates:
            canidates.append(row[2])
        if row [2] == "Khan":
            khan_total=khan_total+1
        if row [2] == "Correy":
            correy_total = correy_total+1
        if row [2] == "Li":
            li_total = li_total+1
        if row [2] == "O'Tooley":
            otooley_total = otooley_total+1

    print ("khan",khan_total)
    print("tot", total_votes)
    print("names",canidates)
    print("li",li_total)
    print("correy",correy_total)
    print("ottotot",otooley_total)
        
