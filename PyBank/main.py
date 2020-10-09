# Modules
import os
import csv

# Set Path
csvpath = os.path.join("..", "Resources","budget_data.csv")

# Define Function
def wins_and_losses(budget_data)
date = str(budget_data)
profits = int(budget_data[1])
# Open CSV

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(cvsreader)

#