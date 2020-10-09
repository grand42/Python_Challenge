# Modules
import os
import csv

# Set Path
csvpath = os.path.join("Resources","budget_data.csv")

# Define Lists
date = []
Profits_Losses = []

# Open CSV

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader)

    for row in csvreader:
        date.append(row[0])
        Profits_Losses.append(int(row[1]))

#calculate total months
length = len(Profits_Losses)

# Calculate Total Profits
total = sum(Profits_Losses)

#Calculate Average Change
average = (Profits_Losses[(length-1)] - Profits_Losses[0])/length

# Find Max Profit

Max = max(Profits_Losses)

# Find Max Loss

Min = min(Profits_Losses)
 
