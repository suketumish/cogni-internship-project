import pandas as pd

# Load the dataset
df = pd.read_csv("Dataset .csv")  # Replace with your actual file

# Strip spaces from column names (if needed)
df.columns = df.columns.str.strip()

# Print column names to verify the correct name
print("Column Names:", df.columns.tolist())

# Check if 'City' column exists, update if needed
city_column = 'City'  # Change this if the column name is different

# Count occurrences of each city
city_counts = df[city_column].value_counts()

# Get the city with the highest number of restaurants
top_city = city_counts.idxmax()
top_city_count = city_counts.max()

# Print result
print(f"The city with the highest number of restaurants is {top_city} with {top_city_count} restaurants.")
