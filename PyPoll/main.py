import csv

voter = []
candidate = []
with open("PyPoll/Resources/election_data.csv") as file:

    reader = csv.reader(file)
    next(reader)

    for row in reader:
        voter.append(row[0])
        candidate.append(row[2])
	

print("Election Results")
print("-------------------------")
print(f"Total Votes: {len(voter)}")
	

cands = list(set(candidate))
cands.sort()

Votes = []
for cand in cands:
    Votes.append(candidate.count(cand))
	

for i in range(len(cands)):
    print(f"{cands[i]}: {'{:.2%}'.format(Votes[i]/len(candidate))} ({Votes[i]})")
print("-------------------------") #is this what you want?
print(f"Winner: {cands[Votes.index(max(Votes))]}")	

	
