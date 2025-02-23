import pandas as pd

# Load the dataset
df = pd.read_csv("Dataset .csv")  # Replace with your actual file

# Strip spaces from column names (if needed)
df.columns = df.columns.str.strip()

# Define relevant column
cuisine_column = 'Cuisines'  # Ensure this column exists in your dataset

# Count occurrences of each cuisine combination
cuisine_combinations = df[cuisine_column].value_counts()

# Display the top 10 most common cuisine combinations
print("Top 10 most common cuisine combinations:")
print(cuisine_combinations.head(10))
