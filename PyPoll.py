# Add dependencies.
import csv
import os 
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    #read file object with reader function
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
# 1. the total number of votes cast
# 2. a complete list of candidates who recieved votes
# 3. the percentage of votes each candidate won
# 4. the total number of votes each candidate won
# 5. The winner of the election based on popular vote