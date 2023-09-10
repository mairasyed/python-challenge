#Python challenge
 
 1. Project Name
    The challenge overall is related to Python. It has two parts; the first one being "Pybank".
    
    1.1 Brief Description
    For the "Pybank" challenge ,we have been provided with a dataset called budget_data.csv. It contains two columns called "Date" and "Profit/Losses". It requires us to write a script in Python that outputs the total number of months included in the dataset,the net total amount of profit/losses over the entire period, the changes in profit/loss over the entire period and then the average change value, the greatest increase & decrease in profits (date and amount) over the entire period. The challenge also requires that the final code/script should be such that it should both print the analysis to the terminal and export a text file with the results. All in all this project assess our knowledge of Python and writing script in visual basic.

    1.2 Key features of the Project
    In this project, I have tried to apply the key concepts learned in Python. First things first we had to import the os and csv file. Next I specified my csv file path by copying the relative path. I used the csv.reader to get my csv file read. Further I initialized all the varibales which I might be using throughout my code to store any values.I used "forloop" to iterate over the rows of my dataset. I found out the total number of months by counting the rows and increasing the row count by 1 every time a new row was reached. i also made use of the "next" function in Python to skip the header as I did not need it in my final result. I initialized an empty list with the name changes , changes=[], in order to store the net change in profit/losses. I also made use of the "if" condition to find out the greatest increase and decrease in profit/losses (date and amount). I used the average formula  sum of values/count of values to work out the average change.Lastly I made use of the output_text and write functions to get my results/analysis printed and displayed as required in the challenge.


    1.3 Key Findings of the Project
    Total Months: 86
    Total: $22564198
    Average Change: $-8311.11
    Greatest Increase in Profits: Aug-16 ($1862002)
    Greatest Decrease in Profits: Feb-14 ($-1825558)

    1.4 Usage
    The script should be able to run smoothly on any similar given dataset.

    1.5 Conclusion
    The code runs error-free and displays the required values.




    2. Project Name
    The challenge overall is related to Python. It has two parts; the first one being "Pypoll".
    
    2.1 Brief Description
    For the "Pypoll" challenge ,we have been provided with a dataset called election_data.csv. It contains three columns called "Voter ID","County" and "Candidate". It requires us to write a script in Python that outputs the total number of votes cast,a complete list of candidates who received votes, the percentage of votes each candidate won, the total number of votes each candidate won and the winner of the election based on the number of votes cast. The challenge also requires that the final code/script should be such that it should both print the analysis to the terminal and export a text file with the results. All in all this project assess our knowledge of Python and writing script in visual basic.

    2.2 Key features of the Project
    In this project, I have tried to apply the key concepts learned in Python. First things first we had to import the os and csv file. Next I specified my csv file path by copying the relative path. I used the csv.reader to get my csv file read. Further I initialized all the varibales which I might be using throughout my code to store any values.I used "forloop" to iterate over the rows of my dataset. I created an empty list [] called candidate_list in order to candidate names and two dictionaries named candidate_votes {} and percentage_votes{}. The dictionary named candidate_votes {} stores "candidate names" as 'key' against "votes" they receive as 'values' whereas the dictionary named percentage_votes{} stores "candidate names" as 'key' against "percentage of votes received" as 'values'. Winner_name is a variable that will hold the election's winner's name based on the number of votes received. I made use of the "if" condition to find out the total number of votes each candidate received. Then I used the percentage formula to find out the percentage of votes each candidate received. I used the "forloop" and "if" condition to find out the winner's name.Lastly I made use of the output_text and write functions to get my results/analysis printed and displayed as required in the challenge.

    2.3 Key Findings of the Project
    Total Votes: 369711
    Charles Casper Stockham: 23.049% (85213)
    Diana DeGette: 73.812% (272892)
    Raymon Anthony Doane: 3.139% (11606)
    Winner: Diana DeGette


    2.4 Usage
    The script should be able to run smoothly on any similar given dataset.

    2.5 Conclusion
    The code runs error-free and displays the required values.






