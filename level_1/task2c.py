import pandas as pd

# Load the dataset
df = pd.read_csv("dataset .csv")  # Replace with your actual file

# Strip spaces from column names (if needed)
df.columns = df.columns.str.strip()

# Print column names to verify
print("Column Names:", df.columns.tolist())

# Define relevant column names
city_column = 'City'
rating_column = 'Aggregate rating'  # Updated to match your dataset

# Calculate the average rating for each city
avg_ratings = df.groupby(city_column)[rating_column].mean()

# Find the city with the highest average rating
top_city = avg_ratings.idxmax()
top_rating = avg_ratings.max()

# Print result
print(f"The city with the highest average rating is {top_city} with an average rating of {top_rating:.2f}.")
