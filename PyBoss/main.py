import os
import csv
import datetime
import states

# The Name column should be split into separate First Name and Last Name columns.
def first(full):
    split = full.split()
    first = split[0]
    return first

def last(full):
    split = full.split()
    last = split[1]
    return last

# The DOB data should be re-written into MM/DD/YYYY format.
def changeDate(inputDate):
    DateFormat = "%Y-%m-%d"
    date = datetime.datetime.strptime(inputDate, DateFormat)
    outPutDateFormat = "%m/%d/%Y"
    outputdate = datetime.date.strftime(date,outPutDateFormat)
    return outputdate

# The SSN data should be re-written such that the first five numbers are hidden from view.
def block(social):
    numbers = [num for num in social]
    del numbers[0:6]
    numbers[0]="***-**-"
    blocked = ""
    for number in numbers:
        blocked += str(number)
    return blocked

# The State data should be re-written as simple two-letter abbreviations.
def changeState(inputState):
    output = states.us_state_abbrev[inputState]
    return output

filepath = os.path.join("employee_data.csv")
employee = []

#create dictionary of employee data calling functions as we iterate to update values for reference use
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        First = first(row["Name"])
        Last = last(row["Name"])
        Birth = changeDate(row["DOB"])
        Blocked = block(row["SSN"])
        State = changeState(row["State"])
        employee.append(
            {
                "Emp ID": row["Emp ID"],
                "First Name": First,
                "Last Name": Last,
                "DOB": Birth,
                "SSN" : Blocked,
                "State" : State
            }
        )

_, filename = os.path.split(filepath)

# Write updated data to csv file
csvpath = os.path.join("output", filename)
with open(csvpath, "w+") as csvfile:
    fieldnames = ["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(employee)