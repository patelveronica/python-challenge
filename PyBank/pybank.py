import os
# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
#define the variables
total_months = 0
net_amount = 0
greatestincrease_amount = 0
greatestincrease_month = 0
greatestdecrease_amount = 0
greatestdecrease_month = 0
avgchange = 0

# Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    row = next(csvreader)
    # print(f"CSV Header: {csvreader}")
   # calculate total numbers of months, net amount of profit/losses
    total_months += 1
    net_amount += int(row[1])
    avgchange = 0

    for row in csvreader:
        #calculate total number of months in the given data set
        total_months += 1
        #calculate net total for all the months in given data set
        net_amount += int(row[1])
        #calculate greatest increase in the amount and month
        if int(row[1]) > greatestincrease_amount:
            greatestincrease_amount = int(row[1])
            greatestincrease_month = row[0]
        #calculate greatest decrease in the amount and month
        if int(row[1]) < greatestdecrease_amount:
            greatestdecrease_amount = int(row[1])
            greatestdecrease_month = row[0]





        print(f" Total Months:  {total_months}")
        print(f"Net total amount: {net_amount}")
        print(f"the greatest increase amount: {greatestincrease_amount}")
        print(f"the greatest increase month: {greatestincrease_month}")
        print(f"the greatest decrease amount: {greatestdecrease_amount}")
        print(f"the greatest decrease month: {greatestdecrease_month}")
