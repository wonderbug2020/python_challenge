#Import the needed functions
import os
import csv
from datetime import datetime
from itertools import zip_longest

#This next part does a lot of different things so i'll break it down line by line, but it was made possible by the fine people at stack overflow
with open("resource/employee_data.csv") as csvfile: #Opens the file and loads it into a variable
    reader = csv.DictReader(csvfile)#This is a class of csv that allows the newly created variable to be mapped into a dictionary
    data = {}#Creates an empty dictionary variable
    for row in reader: #this is going to read through each line of the reader variable
        for header, value in row.items(): #This essentially keeps the foor loop on a specific column
            try:#The try/except is so we don't get a keyerror from the header matching a row
                data[header].append(value)#This is making a list of the values under the keyword of the header
            except KeyError:
                data[header] = [value]

#Now I am going to get the list from all the headers
Emp_ID = data['Emp ID']
Name = data['Name']
DOB = data['DOB']
SSN = data['SSN']
State = data['State']

#Next to create 2 lists, one for first and one for last Name
first_name = []
last_name = []
#Now I need to populate them with the split function from the original name list.
for full_name in Name:
    first_name.append(full_name.split()[0])
    last_name.append(full_name.split()[1])


#Then a new list for the new date format
new_date_format = []
#Now to change the date format and order using datetime
for date in DOB:
    new_date = datetime.strptime(date,"%Y-%m-%d").strftime("%m/%d/%Y")
    new_date_format.append(new_date)

#Next up is to take the SSN list and star out the first 5 numbers
secure_SSN = []
#The SSN list is a list of strings, so this is jus string manipulation
for number in SSN:
    secure_SSN.append(f"XXX_XX{number[6:11]}")

#The last modification is to abbriviate the states names, first i need a new list and also a helpful dictionary
abb_state = []
us_state_abbrev = {'Alabama': 'AL','Alaska': 'AK','Arizona': 'AZ','Arkansas': 'AR',
                   'California': 'CA','Colorado': 'CO','Connecticut': 'CT',
                   'Delaware': 'DE','Florida': 'FL','Georgia': 'GA','Hawaii': 'HI',
                   'Idaho': 'ID','Illinois': 'IL','Indiana': 'IN','Iowa': 'IA',
                   'Kansas': 'KS','Kentucky': 'KY','Louisiana': 'LA','Maine': 'ME',
                   'Maryland': 'MD','Massachusetts': 'MA','Michigan': 'MI',
                   'Minnesota': 'MN','Mississippi': 'MS','Missouri': 'MO',
                   'Montana': 'MT','Nebraska': 'NE','Nevada': 'NV','New Hampshire': 'NH',
                   'New Jersey': 'NJ','New Mexico': 'NM','New York': 'NY',
                   'North Carolina': 'NC','North Dakota': 'ND','Ohio': 'OH',
                   'Oklahoma': 'OK','Oregon': 'OR','Pennsylvania': 'PA',
                   'Rhode Island': 'RI','South Carolina': 'SC','South Dakota': 'SD',
                   'Tennessee': 'TN','Texas': 'TX','Utah': 'UT','Vermont': 'VT',
                   'Virginia': 'VA','Washington': 'WA','West Virginia': 'WV',
                   'Wisconsin': 'WI','Wyoming': 'WY',}
#Now for the for loop to assign the value to the list based on the state (key)
for state_name in State:
    abb_state.append(us_state_abbrev[state_name])

#Next is to write all of this a new csv file
#First I put all of my lists into a single list
master_list = [Emp_ID,first_name,last_name,new_date_format,secure_SSN,abb_state]
#I need to use zip_longest to make everything uniform? i couldn't get this to work without this line i got from stack overflow
export_data = zip_longest(*master_list, fillvalue = '')
with open('analysis/employee_data_test.csv','w',newline='') as f:
    wr = csv.writer(f)
    wr.writerow(("Emp ID","First Name","Last Name",'DOB','SSN','State'))
    wr.writerows(export_data)
