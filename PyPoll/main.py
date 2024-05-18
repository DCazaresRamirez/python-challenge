import pandas as pd


#Adding file path to be able to read the csv file
file_path = 'Resources/election_data.csv'

df = pd.read_csv(file_path)

print("Election Results")
print("-----------------")

#Total number of votes cast
totalVotes = df.shape[0]
print(f"Total Votes: {totalVotes}")
print("-----------------")

#Complete list of candidates who received votes
unique_candidate = df['Candidate'].unique()

#number of votes and percentage of votes each candidate won
candidate_counts = df["Candidate"].value_counts()

for candidate in candidate_counts.index:
    candidate_percentage = (candidate_counts[candidate] / totalVotes * 100)
    print(f"{candidate}: {candidate_percentage:.3f}% ({candidate_counts[candidate]})")

#winner of the election based on popular vote
winning_candidate = candidate_counts.idxmax()
print("-----------------")
print(f"Winner: {winning_candidate}")

#exporting text file
output_file_path = 'Analysis/output.txt'
with open(output_file_path,'w') as file:
    file.write("Election Results\n")
    file.write("-----------------\n")
    file.write(f"Total Votes: {totalVotes}\n")
    file.write("-----------------\n")
    for candidate in candidate_counts.index:
        candidate_percentage = (candidate_counts[candidate] / totalVotes * 100)
        file.write(f"{candidate}: {candidate_percentage:.3f}% ({candidate_counts[candidate]})\n")
    file.write("-----------------\n")
    file.write(f"Winner: {winning_candidate}\n")