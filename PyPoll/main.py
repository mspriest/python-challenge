import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

#initialize lists
voter_ID=[]
candidate = []
unique_candidate=[]
candidate_votes=[]
percent = []

#open csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)
    print(f"{csv_header}")

    # Loop through rows
    for row in csvreader:
        voter_ID.append(row[0])
        candidate.append(row[2])

        #find unique candidates
        if row[2] not in unique_candidate:
            unique_candidate.append(row[2])

    #find total number of votes for each candidates
    for n in unique_candidate:
        total_votes=candidate.count(n)
        candidate_votes.append(total_votes)
        #check: print (total_votes)

        #find total votes by summing candidate votes
        vote_total = sum(candidate_votes)
        #check: print(vote_total)

        #find percent of vote for each candidate
        vote_percent = (round(total_votes/(len(voter_ID)) *100))
        percent.append(vote_percent)
        #check: print(vote_percent)

    #find winning candidate
    winning_vote_total = max(candidate_votes)
    winner = unique_candidate[candidate_votes.index(winning_vote_total)]
    #check: print(winner)

    #print analysis
    print("***Election Results***")
    print(f'Total Votes: {vote_total}')
    for i in range(len(unique_candidate)):
        print(unique_candidate[i] + ": " + str(percent[i]) +"% (" + str(candidate_votes[i])+ ")")
    print(f'Winner: {winner}')

    # print to text file
    with open("Election_Results.text", "w") as text_file:
        text_file.write(f"*** Election Results *** \n")
        text_file.write(f"Total Votes: {vote_total} \n")
        for i in range(len(set(unique_candidate))):
            text_file.write(unique_candidate[i] + ": " + str(percent[i]) +"% (" + str(candidate_votes[i]) + ")\n")
        text_file.write(f"Winner: {winner}\n")








