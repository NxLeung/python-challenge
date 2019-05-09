# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting so the records are simple.)


# Your task is to create a Python script that analyzes the records to calculate each of the following:


# The total number of months included in the dataset


# The net total amount of "Profit/Losses" over the entire period


# The average of the changes in "Profit/Losses" over the entire period


# The greatest increase in profits (date and amount) over the entire period


# The greatest decrease in losses (date and amount) over the entire period




# As an example, your analysis should look similar to the one below:
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)


# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv

filepath = os.path.join("budget_data.csv")

bankdata = []

#create dictionary of bankdata for reference use
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Month = row["Date"]
        Net = row["Profit/Losses"]
        bankdata.append(
            {
                "Month": row["Date"],
                "Net": row["Profit/Losses"],
            }
        )

#assigning first value to calculate net change
first = int(bankdata[0]['Net'])
net = 0
average = 0
greatest = 0
lowest = 0
delta = 0
last = 0

#iterate through each row to calculate values
for row in bankdata:
    #using a variable to perform calculations in current iteration
    current = int(row['Net'])
    
    #running total of net change
    net = net + current 

    #Evaluate the monthly delta and keep a running total of the greatest and lowest amount and corresponding month
    delta = current - int(last)
    if delta > greatest:
        greatest = delta
        greatestMonth = row['Month']
    elif delta < lowest:
        lowest = delta
        lowestMonth = row['Month']
    
    #establishing variable for next iteration
    last = row['Net']

# calculating average change
totalDelta = int(last) - int(first)
average = totalDelta / (len(bankdata)-1)

# Output to terminal with formating
print (f"Total Months: {len(bankdata)} ")
print (f"Total: ${net} ")
print (f"Average Change: ${average:,.2f}".replace('$-', '-$'))
print (f"Greatest Increase in Profits: {greatestMonth} (${greatest}) ".replace('$-', '-$'))
print (f"Greatest Decrease in Profits: {lowestMonth} (${lowest}) ".replace('$-', '-$'))

# Output to file
file = open("PyBankAnalysis.txt","w+")
file.write(f"Total Months: {len(bankdata)} \n")
file.write(f"Total: ${net} \n")
file.write(f"Average Change: ${average:,.2f}\n".replace('$-', '-$'))
file.write(f"Greatest Increase in Profits: {greatestMonth} (${greatest}) \n".replace('$-', '-$'))
file.write(f"Greatest Decrease in Profits: {lowestMonth} (${lowest}) \n".replace('$-', '-$'))
file.close() 