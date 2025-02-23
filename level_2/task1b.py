import pandas as pd

# Load the dataset
df = pd.read_csv("Dataset .csv")  # Replace with your actual file

# Strip spaces from column names (if needed)
df.columns = df.columns.str.strip()

# Define relevant column
votes_column = 'Votes'  # Ensure this column exists in your dataset

# Convert "Votes" column to numeric (in case of string values)
df[votes_column] = pd.to_numeric(df[votes_column], errors='coerce')

# Calculate the average number of votes
average_votes = df[votes_column].mean()

# Print result
print(f"The average number of votes received by restaurants is {average_votes:.2f}.")
