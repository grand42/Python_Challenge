# Modules
import os
import csv

# Set Path
csvpath = os.path.join("Resources","budget_data.csv")

# Define Lists
Date = []
Profits_Losses = []
Changes=[]

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


# Find Changes
for i in range(1,length):
    x=Profits_Losses[i]-Profits_Losses[i-1]
    Changes.append(x)

#Calculate Average Change and round to two decimals
average = 0.00
average = sum(Changes)/len(Changes)
average = str(round(average, 2))

# Find Max Profit
Max = max(Changes)

# Find Max Loss
Min = min(Changes)
 
# Find Date with Max Profit
date_of_max = Date[Changes.index(Max)+1]

# Find Date with Max Loss
date_of_min = Date[Changes.index(Min)+1]

# Print Results

print("Financial Analysis")
print("----------------------")
print(f"Total Months: {length}")
print(f"Total: ${total}")
print("Average Change: $"+ average)
print(f"Greatest Increase in Profits: {date_of_max} (${Max})")
print(f"Greatest Decrease in Profits: {date_of_min} (${Min})")