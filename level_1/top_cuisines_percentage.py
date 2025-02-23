import pandas as pd

# Load the dataset
df = pd.read_csv("Dataset .csv")  # Replace with your actual file

# Strip spaces from column names (if needed)
df.columns = df.columns.str.strip()

# Print column names to verify the correct name
print("Column Names:", df.columns.tolist())

# Check if 'Cuisine' exists, update if needed
cuisine_column = 'Cuisines'  # Change this if the column name is different

# Count occurrences of each cuisine
cuisine_counts = df[cuisine_column].value_counts()

# Get total restaurants
total_restaurants = len(df)

# Get the top 3 cuisines
top_cuisines = cuisine_counts.head(3)

# Calculate percentage
top_cuisine_percentages = (top_cuisines / total_restaurants) * 100

# Print results
print("Top 3 Cuisines with Percentages:")
print(top_cuisine_percentages)
