import pandas as pd

# Load the dataset
df = pd.read_csv("Dataset .csv")  # Replace with your actual file

# Strip spaces from column names (if needed)
df.columns = df.columns.str.strip()

# Define relevant columns
cuisine_column = 'Cuisines'
rating_column = 'Aggregate rating'

# Group by cuisine combinations and calculate average rating
cuisine_ratings = df.groupby(cuisine_column)[rating_column].mean()

# Sort by highest ratings
top_cuisine_ratings = cuisine_ratings.sort_values(ascending=False)

# Display the top 10 highest-rated cuisine combinations
print("Top 10 highest-rated cuisine combinations:")
print(top_cuisine_ratings.head(10))
