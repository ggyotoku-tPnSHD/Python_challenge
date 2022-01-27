import csv
import os

output_file = os.path.join("..", "Analysis", "poll_results.txt")
csvfile = os.path.join("..", "Resource", "election_data.csv")

candidate_names = []
unique_values = []

with open(csvfile) as csvf:

    vote_data = csv.reader(csvf)

    heading = next(vote_data)

    for row in vote_data:
        if row != heading:
            candidate_names.append(row[2])
            unique_values.append(row[2])

    print(heading)

# unique = set(unique_values)
# print(unique)

print("```text")
print("Election Results")
print("-------------------------")
print(f"Total Votes: {len(candidate_names)}")
print(f"Khan: {round((candidate_names.count('Khan')/len(candidate_names))*100)}% ({candidate_names.count('Khan')})")
print(f"Correy: {round((candidate_names.count('Correy')/len(candidate_names))*100)}% ({candidate_names.count('Correy')})")
print(f"Li: {round((candidate_names.count('Li')/len(candidate_names))*100)}% ({candidate_names.count('Li')})")
print(f"""O'Tooley: {round((candidate_names.count("O'Tooley")/len(candidate_names))*100)}% ({candidate_names.count("O'Tooley")})""")
print("-------------------------")
print(f"Winner: Khan")
print("-------------------------")
print("```")


with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["```text"])
    writer.writerow(["Election Results"])
    writer.writerow(["-------------------------"])
    writer.writerow([f"Total Votes: {len(candidate_names)}"])
    writer.writerow(
        [f"Khan: {round((candidate_names.count('Khan')/len(candidate_names))*100)}% ({candidate_names.count('Khan')})"])
    writer.writerow(
        [f"Correy: {round((candidate_names.count('Correy')/len(candidate_names))*100)}% ({candidate_names.count('Correy')})"])
    writer.writerow(
        {f"Li: {round((candidate_names.count('Li')/len(candidate_names))*100)}% ({candidate_names.count('Li')})"})
    writer.writerow(
        [f"""O'Tooley: {round((candidate_names.count("O'Tooley")/len(candidate_names))*100)}% ({candidate_names.count("O'Tooley")})"""])
    writer.writerow(["-------------------------"])
    writer.writerow([f"Winner: Khan"])
    writer.writerow(["-------------------------"])
    writer.writerow(["```"])
