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
print(total)