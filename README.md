# Python-Challenge:  PyBank and PyPoll

This challenge contains two data analysis projects, PyBank and PyPoll.

## PyBank

### Background

PyBank analysed the financial records of a company.  The financial data was contained in a csv file titled [budget_data](PyBank/Resources/budget_data.csv).

	with open(csvpath) as csvfile:
    		csvreader = csv.reader(csvfile, delimiter=",")
    		header=next(csvreader)

    		for row in csvreader:
        		Date.append(row[0])
        		Profits_Losses.append(int(row[1]))	

### Analysis

##### Calculate the total number of months included in the data set.

	length = len(Profits_Losses)

##### Calculate the total amount of profits over the entire data set.
	
	total = sum(Profits_Losses)

##### Calculate the average monthly changes of profits over the entire data set.

* Loop through the array and calculates the difference between the current and previous months.
	Changes = []
	for i in range(1,length):
    		x=Profits_Losses[i]-Profits_Losses[i-1]
    		Changes.append(x)

* Calculate the average of the changes and round to two decimals.

	average = 0.00
	average = sum(Changes)/len(Changes)
	average = str(round(average, 2))


##### Calculate the greatest monthly increase in profits over the entire data set and the month this occurred.
	Max = max(Changes)
	date_of_max = Date[Changes.index(Max)+1]
	
##### Calculate the greatest decrease in profits over the entire data set and the month this occurred.
	Min = min(Changes)
	date_of_min = Date[Changes.index(Min)+1]
##### Save the desired outputs in a txt file.
	
	with open("Analysis/Bank_Analysis.txt", "w") as f:
    		print("Financial Analysis", file=f) 
    		print("----------------------", file=f)
    		print(f"Total Months: {length}", file=f)
    		print(f"Total: ${total}",file=f)
    		print("Average Change: $"+ average,file=f)
   		print(f"Greatest Increase in Profits: {date_of_max} (${Max})",file=f)
    		print(f"Greatest Decrease in Profits: {date_of_min} (${Min})",file=f) 






## PyPoll

The second project, PyPoll, analysed polling data for a state election.  The poll data was contained in a csv file.  The goals of the analysis include:

	* Output the total number of votes cast.
	* Output a list of candidates who recieved votes.
	* Calculate the total number of votes recieved by each candidate.
	* Calculate the percentage of votes won by each candidate.
	* Output the winner of the election based on the popular vote.
	* Save the desired outputs in a txt file. 