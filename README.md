# Python-Challenge:  PyBank and PyPoll

This challenge contains two data analysis projects, PyBank and PyPoll.

## PyBank

### Background

PyBank analysed the financial records of a company.  The financial data was contained in a csv file titled [budget_data](PyBank/Resources/budget_data.csv).

'''
# Open CSV

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader)

    for row in csvreader:
        Date.append(row[0])
        Profits_Losses.append(int(row[1]))	
'''

### Analysis

##### Calculate the total number of months included in the data set.
'''
#calculate total months
length = len(Profits_Losses)
'''

* Calculate the total amount of profits over the entire data set.
* Calculate the average monthly changes of profits over the entire data set.
* The greatest monthly increase in profits over the entire data set and the month this occurred.
* The greatest decrease in profits over the entire data st and the month this occurred.
* Save the desired outputs in a txt file.

### Analysis






## PyPoll

The second project, PyPoll, analysed polling data for a state election.  The poll data was contained in a csv file.  The goals of the analysis include:

	* Output the total number of votes cast.
	* Output a list of candidates who recieved votes.
	* Calculate the total number of votes recieved by each candidate.
	* Calculate the percentage of votes won by each candidate.
	* Output the winner of the election based on the popular vote.
	* Save the desired outputs in a txt file. 