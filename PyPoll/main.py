# In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)


# You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:


# The total number of votes cast


# A complete list of candidates who received votes


# The percentage of votes each candidate won


# The total number of votes each candidate won


# The winner of the election based on popular vote.




# As an example, your analysis should look similar to the one below:
# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------


# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv

filepath = os.path.join("election_data.csv")

khanCount = 0
correyCount = 0
liCount = 0
otoolCount = 0

#create dictionary of bankdata for reference use
with open(filepath) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    for row in reader:
        if row[2] == "Khan":
            khanCount += 1
        elif row[2] == "Correy":
            correyCount += 1
        elif row[2] == "Li":
            liCount += 1
        elif row[2] == "O'Tooley":
            otoolCount += 1

candidate = ["Khan", "Correy", "Li", "O'Tooley"]
votecount = [khanCount, correyCount, liCount, otoolCount]
totalCount = khanCount+correyCount+liCount+otoolCount
percent = [khanCount/totalCount*100, correyCount/totalCount*100, liCount/totalCount*100, otoolCount/totalCount*100]
winner = votecount.index(max(votecount))
outcome = zip(candidate, percent, votecount)


# Output to terminal with formating
print (f"Election Results")
print (f"-----------------------------")
print (f"Total Votes: {totalCount}")
print (f"-----------------------------")
for i in range(len(candidate)):
    print (f"{candidate[i]}: {percent[i]:,.3f}% ({votecount[i]})")
print (f"-----------------------------")
print (f"Winner: {candidate[winner]}")
print (f"-----------------------------")


# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------


# Output to file
file = open("PyPollAnalysis.txt","w+")
# file.write(f"Total Months: {len(bankdata)} \n")
# file.write(f"Total: ${net} \n")
# file.write(f"Average Change: ${average:,.2f}\n".replace('$-', '-$'))
# file.write(f"Greatest Increase in Profits: {greatestMonth} (${greatest}) \n".replace('$-', '-$'))
# file.write(f"Greatest Decrease in Profits: {lowestMonth} (${lowest}) \n".replace('$-', '-$'))
# file.close() 

file.write (f"Election Results\n")
file.write (f"-----------------------------\n")
file.write (f"Total Votes: {totalCount}\n")
file.write (f"-----------------------------\n")
for i in range(len(candidate)):
    file.write (f"{candidate[i]}: {percent[i]:,.3f}% ({votecount[i]})\n")
file.write (f"-----------------------------\n")
file.write (f"Winner: {candidate[winner]}\n")
file.write (f"-----------------------------\n")
file.close()