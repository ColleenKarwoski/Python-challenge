import os
import csv

#read csv file
with open ('election_data.csv', 'r') as csv_file:
    csv_reader= csv.reader(csv_file)

    csv_header=next(csv_reader)

    totalvotes = []
    candidates = []

    for row in csv_reader:
        totalvotes.append(row[0])
        candidates.append(row[2])
    
    #find unique candidates        
    uniqueCandidates=[]
    for x in candidates:
        if x not in uniqueCandidates:
            uniqueCandidates.append(x)
          

f=open("poll_analysis.txt", "w")
print("Election Results")
print("Election Results", file=f)
print("-------------------------")
print("-------------------------", file=f)
print("Total Votes:", len(totalvotes))
print("Total Votes:", len(totalvotes), file=f)
print("-------------------------")
print("-------------------------", file=f)
total_vote_count= len(totalvotes)

def printCandidateResults(unique_candidate, total_vote_number, candidates):
    candidate_votes= candidates.count(unique_candidate)
    candidate_percent= round(100 * candidate_votes / total_vote_number, 3)
    print(unique_candidate, ": ", candidate_percent, "% ",'(',candidate_votes, ')\n',sep="", end="")
    output=f'{unique_candidate}: {candidate_percent}% {candidate_votes}\n'
    print(output, file=f)

printCandidateResults(uniqueCandidates[0], total_vote_count, candidates)
printCandidateResults(uniqueCandidates[1], total_vote_count, candidates)
printCandidateResults(uniqueCandidates[2], total_vote_count, candidates)

#create dictionary for candidates and votes
votes_by_candidate = {}
for name in uniqueCandidates:
    votes = candidates.count(name)
    votes_by_candidate[name] = votes

#find winner
winner_name= list(votes_by_candidate.keys())[0]
for name in votes_by_candidate:
        if votes_by_candidate[name] > votes_by_candidate[winner_name]:
            winner_name= name

print("-------------------------")
print("-------------------------", file=f)
print(f"Winner: {winner_name}")
print(f"Winner: {winner_name}", file=f)