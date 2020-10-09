# Modules
import os
import csv

# Set Path
csvpath = os.path.join("Resources","budget_data.csv")

# Define Lists
Date = []
Profits_Losses = []

# Open CSV

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader)

    for row in csvreader:
        Date.append(row[0])
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
 
# Find Date with Max Profit
date_of_max = Date[Profits_Losses.index(Max)]

# Find Date with Max Loss
date_of_min = Date[Profits_Losses.index(Min)]

# Print Results

print("Financial Analysis")
print("----------------------")
print(f"Total Months: {length}")
print(f"Total: ${total}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {date_of_max} (${Max})")
print(f"Greatest Decrease in Profits: {date_of_min} (${Min})")