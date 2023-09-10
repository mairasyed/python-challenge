import os
import csv


#Specifying csv file address
budget_csv="Resources/budget_data.csv"


#Initializing variables to store values
net_total=0
row_count=0
greatest_increase=0
greatest_increase_date=None
greatest_decrease=0
greatest_decrease_date=None
previous_net=0
changes=[]

# Open and read the CSV file
with open(budget_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    #Skip the header
    header=next(csv_reader)
    
    #Reading the first row of the dataset
    first_row=next(csv_reader)
    row_count= row_count+1
    previous_net=int(first_row[1])
    net_total=net_total+previous_net
    
    # Calculate the number of months, net total profit/loss,average change, greatest inc. & dec. in profits along with asssociated dates
    #Using forloop
    for row in csv_reader:
        row_count=row_count+1
        profit_loss=int(row[1])
        net_total += profit_loss
        net_change=int(row[1])-previous_net
        previous_net=int(row[1])
        changes.append(net_change)
        date=row[0]
        #if condition for determining the greatest increase/decrease in profit along with associated dates
        if net_change > greatest_increase:
          greatest_increase = net_change
          greatest_increase_date = date
        if net_change < greatest_decrease:
          greatest_decrease = net_change
          greatest_decrease_date = date

#Calculating the average change
average_change=round(sum(changes)/len(changes),2)

#printing the results


Output_Text = (
f"Financial Analysis\n"
f"----------------------------\n"
f"Total Months: {row_count}\n"
f"Total: ${net_total}\n"
f"Average Change: ${average_change}\n"
f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})"

)


print(Output_Text)

#Exporting the file results

text_file = "analysis\\Output.txt"

with open(text_file, 'w') as output_file:
   output_file.write(Output_Text)