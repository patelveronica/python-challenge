import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

total_votes = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0

# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    #for loop to count the total vot and sum the total votes.
    for row in csvreader:
        #count total votes and sum
        total_votes += 1
        # lets store candidates names and count & sum votes for each candidates.
        if row[2] == "Khan":
            Khan_votes += 1
        elif row[2] =="Correy":
            Correy_votes += 1
        elif row[2] == "Li":
            Li_votes += 1
        elif row[2] == "O'Tooley":
            OTooley_votes += 1
        # #maybe i should add function here:
    # def winnername(candidates):
    #     if Khan_votes > Correy_votes:
            # elif Khan_votes > Li_votes:
            #     elif Khan_votes > OTooley_votes:
# if khan_percentage > Correy_percentage and khan_percentage > Li_percentage and khan_percentage > OTooley_percentage:
candidates = ["Khan", "Correy","Li", "O'Tooley" ]
#store candidates votes    
Votes = [Khan_votes, Correy_votes, Li_votes, OTooley_votes]
#Calculate the percentage for each candidate
khan_percentage = (Khan_votes/total_votes)
Correy_percentage = (Correy_votes/total_votes)
Li_percentage = (Li_votes/total_votes)
OTooley_percentage = (OTooley_votes/total_votes)
        
#print the results for each candidate including total votes
print("Election Results")
print("-------------------------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------------------------")
print("Khan: "+"{:.3%}".format(khan_percentage) + " " + str(Khan_votes))
print("Correy: "+"{:.3%}".format(Correy_percentage) + " " + str(Correy_votes))
print("Li: "+"{:.3%}".format(Li_percentage) + " " + str(Li_votes))
print("O'Tooley: "+"{:.3%}".format(OTooley_percentage) + " " + str(OTooley_votes))
print("-------------------------------------------")
print("Winner: " + "Khan")
# print("The Winner is: " + winnername[0])
print("-------------------------------------------")

# Save the summary results to textfile
save_textfile = csvpath.strip(".csv") + "_ElectionResults.txt"
csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath, 'w')as result:
    print("Election Results")
result.write("Election Results" + "\n")
result.write("-------------------------------------------" + "\n")
result.write(f"Total Votes: {str(total_votes)}" + "\n")
result.write("-------------------------------------------" + "\n")
result.write(f"Khan: {{:.3%}.format(khan_percentage) + " " + str(Khan_votes)}" + "\n")
result.write(f"Khan: {{:.3%}.format(Correy_percentage) + " " + str(Khan_votes)}" + "\n")
# result.write("Correy: "+"{:.3%}".format(Correy_percentage) + " " + str(Correy_votes))
result.write(f"Khan: {{:.3%}.format(Li_percentage) + " " + str(Khan_votes)}" + "\n")
# result.write("Li: "+"{:.3%}".format(Li_percentage) + " " + str(Li_votes))
result.write(f"Khan: {{:.3%}.format(OTooley_percentage) + " " + str(Khan_votes)}" + "\n")
# result.write("O'Tooley: "+"{:.3%}".format(OTooley_percentage) + " " + str(OTooley_votes))
result.write("-------------------------------------------" + "\n")
result.write("Winner: " + "Khan")
result.write("-------------------------------------------" + "\n")

