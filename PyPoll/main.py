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

# Find Total Votes
total = len(Voter_ID)

# Find unique candides
Candidate_List = []
for vote in Candidate:
    if vote not in Candidate_List:
        Candidate_List.append(vote)

def vote_percent(candidate_vote):
    x = Candidate.count(candidate_vote)
    Total = len(Voter_ID)
    percent = (x/Total) * 100
    print(candidate_vote + ": " + str(percent) + "% (" + str(x) + ")")


for candidate in Candidate_List:
    vote_percent(candidate)