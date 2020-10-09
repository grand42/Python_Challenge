# Modules
import os
import csv

# Set Path
csvpath = os.path.join("..", "Resources","budget_data.csv")

# Define Lists
date = []
Profits_Losses = []

# Define Function
def profits_and_losses(budget_data):
    
    profits = int(budget_data[1])

    average = sum(profits)/len(profits)

    total =sum(profits)
    
    max_profit = max(profits)

    max_loss = min(profits)


# Open CSV

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(cvsreader)

    for row in csvreader:
        date.append(row[1])
        Profits_Losses.append(row[2])
