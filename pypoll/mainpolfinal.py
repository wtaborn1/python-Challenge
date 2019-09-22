# Pypol Import CSV
import csv
import os
csvpath = os.path.join("election_data.csv")
#Read file
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    total_votes=0
    canidates = []
    khan_total = 0
    correy_total = 0
    li_total = 0
    otooley_total = 0
#Counting votes for each canidate    

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

    
    #Calculate the total vote
    total_votes =  khan_total+correy_total+li_total+otooley_total
    print("Total Votes,",total_votes)
    #percentage of votes
    khan_percentage = (khan_total/total_votes)*100
    corey_percentage = (correy_total/total_votes)*100
    li_percentage = (li_total/total_votes)*100
    otooley_percentage = (otooley_total/total_votes)*100
print("Khan:{0:.3f}% ({1})".format(khan_percentage,khan_total))
print("Li:{0:.3f}% ({1})".format(li_percentage,li_total))
print("Correy:{0:.3f}% ({1})".format(corey_percentage,correy_total))
print("O'tooley:{0:.3f}% ({1})".format(otooley_percentage,otooley_total))


#The Winner
winning_vote = max(khan_total,li_total,correy_total,otooley_percentage)

if winning_vote == khan_total:
        winning_canidates = "Khan"
elif winning_vote == li_total:
        winning_canidates = "Li"
elif winning_vote == correy_total:
        winning_canidates = "Correy"
elif winning_canidates == otooley_total:
        winning_canidates = "O'tooley"
print("Highest vote total",winning_canidates)


#print to file
with open ("Voter_Results.txt","w") as voter_file:
    voter_file.write("Total Votes:{0}\n".format(total_votes))
    voter_file.write("Khan:{0:.3f}% ({1})\n".format(khan_percentage,khan_total))
    voter_file.write("Li:{0:.3f}% ({1})\n".format(li_percentage,li_total))
    voter_file.write("Correy:{0:.3f}% ({1})\n".format(corey_percentage,correy_total))
    voter_file.write("O'tooley:{0:.3f}% ({1})\n".format(otooley_percentage,otooley_total))
    voter_file.write("Highest vote total",winning_canidates)





