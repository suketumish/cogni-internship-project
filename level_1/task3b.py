import pandas as pd

# Load the dataset
df = pd.read_csv("Dataset .csv")  # Replace with your actual file

# Strip spaces from column names (if needed)
df.columns = df.columns.str.strip()

# Define relevant column
price_column = 'Price range'  # Ensure this column exists in your dataset

# Count occurrences of each price range
price_counts = df[price_column].value_counts()

# Calculate percentage
price_percentage = (price_counts / len(df)) * 100

# Print results
print("Percentage of Restaurants in Each Price Range:")
print(price_percentage)
