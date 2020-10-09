# Modules
import os
import csv

# Set Path
csvpath = os.path.join("Resources","election_data.csv")

# Define Lists
Voter_ID = []
County = []
Candidate=[]

# Open CSV

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader)

    for row in csvreader:
        Voter_ID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])

# Print Header
print("Election Results")
print("--------------------")

# Find Total Votes
total = len(Voter_ID)
print(f"Total Votes: {total}")

print("--------------------")

# Find unique candides
Candidate_List = []
for vote in Candidate:
    if vote not in Candidate_List:
        Candidate_List.append(vote)

# Define function to find percentage of votes

def vote_percent(candidate_vote):
    x = Candidate.count(candidate_vote)
    Total = len(Voter_ID)
    percent = 0.00
    percent = (x/Total) * 100
    percent = str(round(percent, 3))
    print(candidate_vote + ": " + percent + "% (" + str(x) + ")")

# Create list for vote counts to find winner
winner = []


for candidate in Candidate_List:
    vote_percent(candidate)
    
    # Find Votes/Candidate
    winner.append(int(Candidate.count(candidate)))

#Find Winner
winner_index = winner.index(max(winner))
print("--------------------")
print(f"Winner: {Candidate_List[winner_index]}")
print("--------------------")