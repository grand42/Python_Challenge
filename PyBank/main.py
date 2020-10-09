# Modules
import os
import csv

# Set Path
csvpath = os.path.join("Resources","budget_data.csv")

# Define Lists
date = []
Profits_Losses = []

# Define Function
# def profits_and_losses(profits):
    
    #average = sum(profits)/len(profits)

    #total =sum(profits)
    
    #max_profit = max(profits)

    #max_loss = min(profits)

    #print(f"(Total: ${total})")
    #print(f"(Average Change: ${average})")




# Open CSV

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader)

    for row in csvreader:
        date.append(row[0])
        Profits_Losses.append(int(row[1]))

average = sum(Profits_Losses)/len(Profits_Losses) 
print(average)
 
