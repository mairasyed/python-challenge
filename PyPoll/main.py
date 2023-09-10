import os
import csv

#Specifying csv file path
election_csv="Resources/election_data.csv"

#Initializing the variables
row_count=0
candidates_list=[]        #empty list to store candidate names
candidate_votes={}          #empty dictionary to store "candidate names" as 'key' against "votes" they receive as 'values'
percentage_votes={}            #empty dictionary to store "candidate names" as 'key' against "percentage of votes received" as 'values'
winner_name= ""                 #variable to store the name of the winner
highest_percentage_of_votes=0

# Open and read the CSV file
with open(election_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

#Skip the header
    header=next(csv_reader)


#Counting the rows and collecting unique candidate names using "forloop" & "if" condition

    for row in csv_reader:
        row_count= row_count+1
        candidate=str(row[2])
        if candidate not in candidates_list:
            candidates_list.append(candidate)

#Calculating the number of votes each candidate received

        if candidate not in candidate_votes:
                candidate_votes[candidate]=1
        else:
                candidate_votes[candidate]+=1

#Calculating the percentage of votes each candidate received

percentage_votes = {}
for candidate,votes in candidate_votes.items():
                    percentage=(votes/row_count)*100
                    percentage_votes[candidate]=percentage

#Iterating through the percentage_votes {} dictionary

                    for candidate, percentage in percentage_votes.items():
                        if percentage>highest_percentage_of_votes:
                         highest_percentage_of_votes=percentage
                         winner_name=candidate

text_file = "analysis\\Output.txt"

with open(text_file, 'w') as output_file:



    Output_Text1 = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {row_count}\n"
    f"-------------------------\n"
    )
    print(Output_Text1)
    output_file.write(Output_Text1)



    for candidate in candidates_list:
        Output_Text2 = (f"{candidate}: {percentage_votes[candidate]:.3f}% ({candidate_votes[candidate]})\n")
        print(Output_Text2)
        output_file.write(Output_Text2)

    Output_Text3 = (
    f"-------------------------\n"
    f"Winner: {winner_name}\n"
    f"-------------------------"
    )
    print(Output_Text3)
    output_file.write(Output_Text3)