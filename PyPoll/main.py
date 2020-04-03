#Import the needed functions
import os
import csv

#This next part does a lot of different things so i'll break it down line by line, but it was made possible by the fine people at stack overflow
with open("resource/election_data.csv") as csvfile: #Opens the file and loads it into a variable
    reader = csv.DictReader(csvfile)#This is a class of csv that allows the newly created variable to be mapped into a dictionary
    data = {}#Creates an empty dictionary variable
    for row in reader: #this is going to read through each line of the reader variable
        for header, value in row.items(): #This essentially keeps the foor loop on a specific column
            try:#The try/except is so we don't get a keyerror from the header matching a row
                data[header].append(value)#This is making a list of the values under the keyword of the header
            except KeyError:
                data[header] = [value]

#Next I need to have a list of the votes for candidates
vote = data['Candidate']
#Answer 1 is the length of the list
total_votes = len(vote)

#Next I want to make a list that has all the unique names of the above list as well as a list to support the cote count
candidate_name = []
voter_count = []
for name in vote:
    if name not in candidate_name:
        candidate_name.append(name)
        voter_count.append(0)

#Using the list of unique names I can use it as a "search" to make sure I am incremeting the right vote count
place = 0
for name in vote:
    place = candidate_name.index(name)
    voter_count[place] += 1

#Now That I have to the total votes in a list, I can make a third list that have the vote percentage
per_of_vote = []
for i in range(len(voter_count)):
    #per_of_vote.append(round((voter_count[i]/total_votes) * 100,3))
    per_of_vote.append((voter_count[i]/total_votes) * 100)

#Now I need to us a for loop and if conditional to find the winner
winner_name = ""
winner_count = 0
for i in range(len(voter_count)):
    if voter_count[i] > winner_count:
        winner_count = voter_count[i]
        winner_name = candidate_name[i]

#This next section will be used to print the information to console
print("Election Results")
print("---------------------")
print("Total Votes: " + str(total_votes))
print("---------------------")
for i in range(len(candidate_name)):
    print(f"{candidate_name[i]}: {per_of_vote[i]:.3f}% ({voter_count[i]})")
print("---------------------")
print(f"Winner: {winner_name}")
print("---------------------")

#Next I need to write up the report
f = open("analysis/report.txt","w+")
f.write("Election Results\n" +
        "---------------------\n" +
        "Total Votes: " + str(total_votes) + "\n" +
        "---------------------\n")
for i in range(len(candidate_name)):
    f.write(f"{candidate_name[i]}: {per_of_vote[i]:.3f}% ({voter_count[i]})\n")
f.write("---------------------\n"
        f"Winner: {winner_name}\n"
        "---------------------")
f.close()

#print(candidate_name)
#print(voter_count)
#print(per_of_vote)
#print(winner_name)
