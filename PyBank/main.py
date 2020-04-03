#Import the needed functions
import os
import csv

#This next part does a lot of different things so i'll break it down line by line, but it was made possible by the fine people at stack overflow
with open("resource/budget_data.csv") as csvfile: #Opens the file and loads it into a variable
    reader = csv.DictReader(csvfile)#This is a class of csv that allows the newly created variable to be mapped into a dictionary
    data = {}#Creates an empty dictionary variable
    for row in reader: #this is going to read through each line of the reader variable
        for header, value in row.items(): #This essentially keeps the foor loop on a specific column
            try:#The try/except is so we don't get a keyerror from the header matching a row
                data[header].append(value)#This is making a list of the values under the keyword of the header
            except KeyError:
                data[header] = [value]

#Next I want to have just a list of the values from the Profit/losses Column and a list for the dates
proloss = data['Profit/Losses']
dates = data['Date']

#Since we can assume there are continuous, non duplicate months, we can equate the number of months to the length of the list
#Answer 1
num_of_months = len(proloss)

#Now I need 2 variables, one to count the profits and loss, and then an offset list of the profits
total_proloss = 0
prolossoff = [0]
for value in proloss:#This loops though te total profit list
    #Answer 2
    total_proloss = total_proloss + int(value) #continuously adds the value to the variable to get the sum
    prolossoff.append(value)

#finally to make a list of values that have proloss
prolosschan = []
for i in range(len(proloss)):
    prolosschan.append(int(proloss[i])-int(prolossoff[i]))
prolosschan.pop(0)#Need to remove the first value

#These are variables i need for the final 3 answers
total_proloss_change = 0
total_change_average = 0
max_prof = prolosschan[0]
month_max = ""
min_prof = prolosschan[0]
month_min = ""
#One last loop to get the finally 3 answers
for i in range(len(prolosschan)):
    total_proloss_change = total_proloss_change + int(prolosschan[i])
    if prolosschan[i] > max_prof:
        #Answer 4
        max_prof = int(prolosschan[i])
        month_max = dates[i+1]
    elif prolosschan[i] < min_prof:
        #answer 5
        min_prof = int(prolosschan[i])
        month_min = dates[i+1]

#Answer 3
total_change_average = round(total_proloss_change/len(prolosschan),2)

#Now I tant to put every thing into variables that will be printed to the terminal and the report text
line_1 = "Financial Analysis\n"
line_2 = "------------------------------\n"
line_3 = "Total Months: " + str(num_of_months) + "\n"
line_4 = "Total: $" + str(total_proloss) + "\n"
line_5 = "Average Change: $" + str(total_change_average) + "\n"
#line_6 = "Greatest Increase in Profits: $" + str(max_prof) + "\n"
line_6 = "Greatest Increase in Profits: " + month_max + " ($"+ str(max_prof) + ")\n"
line_7 = "Greatest Decrease in Profits: " + month_min + " ($"+ str(min_prof) + ")\n"
#line_7 = "Greatest Decrease in Profits: $" + str(min_prof)

print(line_1 + line_2 + line_3 + line_4 + line_5 + line_6 + line_7)
#Now that I have all the variables i can save them to a report in the analysis put_folder
f = open("analysis/report.txt","w+")
f.write(line_1 + line_2 + line_3 + line_4 + line_5 + line_6 + line_7)
f.close()
