import os
# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
#csvreader = csv.DictReader(open('Resources/budget_data.csv')) 
#define the variables
total_months = 0
net_amount = 0
greatestincrease_amount = 0
greatestincrease_month = 0
greatestdecrease_amount = 0
greatestdecrease_month = 0
previousrow_value = 0


# Reading using CSV module

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    row = next(csvreader)
    # count total numbers of months
    total_months += 1
    net_amount += int(row[1])
     # for loop to sum the months and net profit/losses amount
    for row in csvreader:
        #count total number of months and add then in the given data set
        total_months += 1
         #calculate net total for all the months in given data set
        net_amount += int(row[1])
        monthly_change = int(row[1]) - previousrow_value
        #find the greatest increase in the amount for a certain month
        if monthly_change > greatestincrease_amount:
            greatestincrease_amount = monthly_change
            greatestincrease_month = row[0]
        #find greatest decrease in the amount for a certain month
        if monthly_change < greatestdecrease_amount:
            greatestdecrease_amount = monthly_change
            greatestdecrease_month = row[0]
        previousrow_value = int(row[1])
    # print the value: results
    print("Financial Analysis")
    print("-----------------------------------")
    print(f"Total Months:  {total_months}")
    print(f"Net total amount: ${net_amount}")
    print(f"the greatest increase in Profits: {greatestincrease_month}  (${greatestincrease_amount})")
    print(f"the greatest decrease in Profits: {greatestdecrease_month}  (${greatestdecrease_amount})")

    #save the Financial Analysis results in txt file
    financialdata = csvpath.strip(".csv") + "FinancialAnalysis.txt"
    csvpath = os.path.join('Resources', 'financialdata')
    with open(csvpath, 'w') as text:
        text.write("Financial Analysis" + "\n")
        text.write("---------------------------------" + "\n")
        text.write(f"Total Months: {total_months}" + "\n")
        text.write(f"Total Revenue: ${net_amount}" + "\n")
        text.write(f"the greatest increase in Profits: {greatestincrease_month}  (${greatestincrease_amount})" + "\n")
        text.write(f"the greatest decrease in Profits: {greatestdecrease_month}  (${greatestdecrease_amount})" + "\n")
 
        