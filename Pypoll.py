#Add our dependencies

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to the path
file_to_save = os.path.join("analysis", "election_analysis.txt")
#outfile = open(file_to_save, "w")
#outfile.write("Hello World")
#outfile.close()
total_votes = 0

#Candidate options: list
candidate_options = []

# declare the empty dictionary
candidates_votes = {} 

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers) 

    #print each row in the csv file
    for row in file_reader:
        print(row)
        total_votes += 1
        candidate_name = row[2]

        # If the candidate does not match any existing candidate:
        if candidate_name not in candidate_options:

        #Add the candidate name to the list
           candidate_options.append(candidate_name)   
        
        #Begin tracking the candidates vote count
           candidates_votes[candidate_name] = 0

        #Add a vote to the candidate's count
        candidates_votes[candidate_name] += 1   

    #Determine the percentage of votes for each candidate by looping through the counts
    #Iterate through the list
    for candidate_name in candidates_votes:
        votes = candidates_votes[candidate_name]
        votes_percentage = float(votes) / float(total_votes) * 100
         
        #Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count
        if(votes > winning_count) and (votes_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = votes_percentage
            winning_candidate = candidate_name
           # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n") 

            
    winning_candidate_summary = (
         f"-------------------------\n"
         f"Winner: {winning_candidate}\n"
         f"Winning Vote Count: {winning_count:,}\n"
         f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    print("Total number of votes: ",total_votes)
    print("Candidates list :", candidate_options)
    print("candidates_votes :", candidates_votes)
    


