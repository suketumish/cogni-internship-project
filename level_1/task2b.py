import pandas as pd

# Load the dataset
df = pd.read_csv("Dataset .csv")  # Replace with your actual file

# Strip spaces from column names (if needed)
df.columns = df.columns.str.strip()

# Print column names to verify
print("Column Names:", df.columns.tolist())

# Define the relevant column names
city_column = 'City'
rating_column = 'Aggregate rating'  # Updated to match your dataset

# Calculate the average rating for each city
avg_ratings = df.groupby(city_column)[rating_column].mean()

# Sort by highest average rating (optional)
avg_ratings_sorted = avg_ratings.sort_values(ascending=False)

# Print results
print("Average rating for restaurants in each city:")
print(avg_ratings_sorted)
